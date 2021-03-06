#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
import os
import tempfile
import zipfile
from abc import ABC, abstractmethod
from typing import Text, Dict, Any
from pathlib import Path
import oss2

from ai_flow.util.file_util.zip_file_util import make_dir_zipfile


class BlobManager(ABC):
    """
    A BlobManager is responsible for uploading and downloading files and resource for an execution of an ai flow project.
    """
    @abstractmethod
    def upload_blob(self, workflow_id: Text, prj_pkg_path: Text) -> Text:
        """
        upload a given project to blob server for remote execution.

        :param workflow_id: a unique identity for this workflow in a ai flow project execution.
        :param prj_pkg_path: the path of this project.
        :return the uri of the uploaded project file in blob server.
        """
        pass

    @abstractmethod
    def download_blob(self, workflow_id, remote_path: Text) -> Text:
        """
        download the needed resource from remote blob server to local process for remote execution.

        :param workflow_id: a unique identity for this workflow in a ai flow project execution.
        :param remote_path: the remote path of the blob server.
        :return a local path for downloaded project directory.
        """
        pass

    def clean_blob(self, workflow_id, remote_path: Text):
        """
        clean up the project files downloaded or created during this execution.
        :param workflow_id: a unique identity for this workflow in a ai flow project execution.
        :param remote_path:
        """
        pass


class LocalBlobManager(BlobManager):
    def upload_blob(self, workflow_id: Text, prj_pkg_path: Text) -> Text:
        return prj_pkg_path

    def download_blob(self, workflow_id, remote_path: Text) -> Text:
        return remote_path

    def clean_blob(self, workflow_id, remote_path: Text):
        pass


class OssBlobManager(BlobManager):
    def __init__(self, project_config: Dict[str, Any]):
        ack_id = project_config.get('blob_server.access_key_id', None)
        ack_secret = project_config.get('blob_server.access_key_secret', None)
        endpoint = project_config.get('blob_server.endpoint', None)
        bucket_name = project_config.get('blob_server.bucket', None)
        auth = oss2.Auth(ack_id, ack_secret)
        self.bucket = oss2.Bucket(auth, endpoint, bucket_name)

    def upload_blob(self, workflow_id: Text, prj_pkg_path: Text) -> Text:
        with tempfile.TemporaryDirectory() as temp_dir:
            zip_file_name = 'workflow_{}_project.zip'.format(workflow_id)
            temp_dir_path = Path(temp_dir)
            zip_file_path = temp_dir_path / zip_file_name
            make_dir_zipfile(prj_pkg_path, zip_file_path)
            object_key = 'ai-flow-k8s/' + zip_file_name
            self.bucket.put_object_from_file(key=object_key, filename=str(zip_file_path))
        return object_key

    def download_blob(self, workflow_id, remote_path: Text, local_path: Text = None) -> Text:
        local_zip_file_name = 'workflow_{}_project'.format(workflow_id)
        oss_object_key = remote_path
        if local_path is None:
            tmp_dir = Path(tempfile.gettempdir())
        else:
            tmp_dir = Path(local_path)
        local_zip_file_path = str(tmp_dir / local_zip_file_name) + '.zip'
        self.bucket.get_object_to_file(oss_object_key, filename=local_zip_file_path)
        with zipfile.ZipFile(local_zip_file_path, 'r') as zip_ref:
            top_dir = os.path.split(zip_ref.namelist()[0])[0]
            extract_path = str(tmp_dir / local_zip_file_name)
            zip_ref.extractall(extract_path)
        downloaded_local_path = Path(extract_path) / top_dir
        return str(downloaded_local_path)


class BlobManagerFactory:
    @staticmethod
    def get_blob_manager(project_config: Dict[str, str]) -> BlobManager:
        blob_server_type = project_config.get('blob_server.type', 'local')
        blob_manager = LocalBlobManager()
        if blob_server_type == 'local':
            return blob_manager
        elif blob_server_type == 'oss':
            return OssBlobManager(project_config)
        return blob_manager

