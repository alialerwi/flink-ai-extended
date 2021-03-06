/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
package com.aiflow.entity;

import com.aiflow.proto.Message.ProjectProto;
import com.aiflow.proto.MetadataServiceOuterClass.ProjectListProto;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class ProjectMeta {

    private Long uuid;
    private String name;
    private String projectType;
    private String uri;
    private String user;
    private String password;
    private Map<String, String> properties;

    public ProjectMeta() {
    }

    public ProjectMeta(Long uuid, String name, String projectType, String uri, String user, String password, Map<String, String> properties) {
        this.uuid = uuid;
        this.name = name;
        this.projectType = projectType;
        this.uri = uri;
        this.user = user;
        this.password = password;
        this.properties = properties;
    }

    public Long getUuid() {
        return uuid;
    }

    public void setUuid(Long uuid) {
        this.uuid = uuid;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getProjectType() {
        return projectType;
    }

    public void setProjectType(String projectType) {
        this.projectType = projectType;
    }

    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }

    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public Map<String, String> getProperties() {
        return properties;
    }

    public void setProperties(Map<String, String> properties) {
        this.properties = properties;
    }

    @Override
    public String toString() {
        return "ProjectMeta{" +
                "uuid=" + uuid +
                ", name='" + name + '\'' +
                ", projectType='" + projectType + '\'' +
                ", uri='" + uri + '\'' +
                ", user='" + user + '\'' +
                ", password='" + password + '\'' +
                ", properties=" + properties +
                '}';
    }

    public static ProjectMeta buildProjectMeta(ProjectProto projectProto) {
        return projectProto == null ? null : new ProjectMeta(projectProto.getUuid(),
                projectProto.getName(),
                projectProto.getProjectType().getValue(),
                projectProto.getUri().getValue(),
                projectProto.getUser().getValue(),
                projectProto.getPassword().getValue(),
                projectProto.getPropertiesMap());
    }

    public static List<ProjectMeta> buildProjectMetas(ProjectListProto projectListProto) {
        if (projectListProto == null) {
            return null;
        } else {
            List<ProjectMeta> projectMetas = new ArrayList<>();
            for (ProjectProto projectProto : projectListProto.getProjectsList()) {
                projectMetas.add(buildProjectMeta(projectProto));
            }
            return projectMetas;
        }
    }
}

