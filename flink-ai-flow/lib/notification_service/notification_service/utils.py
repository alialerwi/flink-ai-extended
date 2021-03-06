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
from notification_service.base_notification import BaseEvent
from notification_service.proto import notification_service_pb2


def event_to_proto(event: BaseEvent):
    result_event_proto = notification_service_pb2.EventProto(key=event.key,
                                                             version=event.version,
                                                             value=event.value,
                                                             event_type=event.event_type,
                                                             create_time=event.create_time,
                                                             id=event.id)
    return result_event_proto


def event_list_to_proto(event_list):
    event_proto_list = []
    for event_model in event_list:
        event_proto = event_to_proto(event_model)
        event_proto_list.append(event_proto)
    return event_proto_list


def event_proto_to_event(event_proto):
    return BaseEvent(id=event_proto.id,
                     key=event_proto.key,
                     value=event_proto.value,
                     event_type=event_proto.event_type,
                     version=event_proto.version,
                     create_time=event_proto.create_time)
