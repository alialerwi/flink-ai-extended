# -*- coding: utf-8 -*-
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
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: deploy_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='deploy_service.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\n\020com.aiflow.proto\210\001\001\220\001\001'),
  serialized_pb=_b('\n\x14\x64\x65ploy_service.proto\x1a\x1cgoogle/api/annotations.proto\"4\n\x0fWorkflowRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x15\n\rworkflow_json\x18\x02 \x01(\t\"I\n\x10ScheduleResponse\x12\x13\n\x0breturn_code\x18\x01 \x01(\x03\x12\x12\n\nreturn_msg\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t\"!\n\x13MasterConfigRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"\xa1\x01\n\x14MasterConfigResponse\x12\x13\n\x0breturn_code\x18\x01 \x01(\x03\x12\x12\n\nreturn_msg\x18\x02 \x01(\t\x12\x31\n\x06\x63onfig\x18\x03 \x03(\x0b\x32!.MasterConfigResponse.ConfigEntry\x1a-\n\x0b\x43onfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\xb2\x04\n\rDeployService\x12h\n\x15startScheduleWorkflow\x12\x10.WorkflowRequest\x1a\x11.ScheduleResponse\"*\x82\xd3\xe4\x93\x02$\"\x1f/aiflow/deployer/workflow/start:\x01*\x12\x66\n\x14stopScheduleWorkflow\x12\x10.WorkflowRequest\x1a\x11.ScheduleResponse\")\x82\xd3\xe4\x93\x02#\"\x1e/aiflow/deployer/workflow/stop:\x01*\x12n\n\x1agetWorkflowExecutionResult\x12\x10.WorkflowRequest\x1a\x11.ScheduleResponse\"+\x82\xd3\xe4\x93\x02%\" /aiflow/deployer/workflow/result:\x01*\x12k\n\x18isWorkflowExecutionAlive\x12\x10.WorkflowRequest\x1a\x11.ScheduleResponse\"*\x82\xd3\xe4\x93\x02$\"\x1f/aiflow/deployer/workflow/alive:\x01*\x12r\n\x0fgetMasterConfig\x12\x14.MasterConfigRequest\x1a\x15.MasterConfigResponse\"2\x82\xd3\xe4\x93\x02,\"\'/aiflow/deployer/workflow/master_config:\x01*B\x18\n\x10\x63om.aiflow.proto\x88\x01\x01\x90\x01\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_WORKFLOWREQUEST = _descriptor.Descriptor(
  name='WorkflowRequest',
  full_name='WorkflowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WorkflowRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workflow_json', full_name='WorkflowRequest.workflow_json', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=106,
)


_SCHEDULERESPONSE = _descriptor.Descriptor(
  name='ScheduleResponse',
  full_name='ScheduleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='return_code', full_name='ScheduleResponse.return_code', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='return_msg', full_name='ScheduleResponse.return_msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='ScheduleResponse.data', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=181,
)


_MASTERCONFIGREQUEST = _descriptor.Descriptor(
  name='MasterConfigRequest',
  full_name='MasterConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='MasterConfigRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=183,
  serialized_end=216,
)


_MASTERCONFIGRESPONSE_CONFIGENTRY = _descriptor.Descriptor(
  name='ConfigEntry',
  full_name='MasterConfigResponse.ConfigEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='MasterConfigResponse.ConfigEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='MasterConfigResponse.ConfigEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=335,
  serialized_end=380,
)

_MASTERCONFIGRESPONSE = _descriptor.Descriptor(
  name='MasterConfigResponse',
  full_name='MasterConfigResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='return_code', full_name='MasterConfigResponse.return_code', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='return_msg', full_name='MasterConfigResponse.return_msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='MasterConfigResponse.config', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MASTERCONFIGRESPONSE_CONFIGENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=380,
)

_MASTERCONFIGRESPONSE_CONFIGENTRY.containing_type = _MASTERCONFIGRESPONSE
_MASTERCONFIGRESPONSE.fields_by_name['config'].message_type = _MASTERCONFIGRESPONSE_CONFIGENTRY
DESCRIPTOR.message_types_by_name['WorkflowRequest'] = _WORKFLOWREQUEST
DESCRIPTOR.message_types_by_name['ScheduleResponse'] = _SCHEDULERESPONSE
DESCRIPTOR.message_types_by_name['MasterConfigRequest'] = _MASTERCONFIGREQUEST
DESCRIPTOR.message_types_by_name['MasterConfigResponse'] = _MASTERCONFIGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WorkflowRequest = _reflection.GeneratedProtocolMessageType('WorkflowRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWREQUEST,
  '__module__' : 'deploy_service_pb2'
  # @@protoc_insertion_point(class_scope:WorkflowRequest)
  })
_sym_db.RegisterMessage(WorkflowRequest)

ScheduleResponse = _reflection.GeneratedProtocolMessageType('ScheduleResponse', (_message.Message,), {
  'DESCRIPTOR' : _SCHEDULERESPONSE,
  '__module__' : 'deploy_service_pb2'
  # @@protoc_insertion_point(class_scope:ScheduleResponse)
  })
_sym_db.RegisterMessage(ScheduleResponse)

MasterConfigRequest = _reflection.GeneratedProtocolMessageType('MasterConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _MASTERCONFIGREQUEST,
  '__module__' : 'deploy_service_pb2'
  # @@protoc_insertion_point(class_scope:MasterConfigRequest)
  })
_sym_db.RegisterMessage(MasterConfigRequest)

MasterConfigResponse = _reflection.GeneratedProtocolMessageType('MasterConfigResponse', (_message.Message,), {

  'ConfigEntry' : _reflection.GeneratedProtocolMessageType('ConfigEntry', (_message.Message,), {
    'DESCRIPTOR' : _MASTERCONFIGRESPONSE_CONFIGENTRY,
    '__module__' : 'deploy_service_pb2'
    # @@protoc_insertion_point(class_scope:MasterConfigResponse.ConfigEntry)
    })
  ,
  'DESCRIPTOR' : _MASTERCONFIGRESPONSE,
  '__module__' : 'deploy_service_pb2'
  # @@protoc_insertion_point(class_scope:MasterConfigResponse)
  })
_sym_db.RegisterMessage(MasterConfigResponse)
_sym_db.RegisterMessage(MasterConfigResponse.ConfigEntry)


DESCRIPTOR._options = None
_MASTERCONFIGRESPONSE_CONFIGENTRY._options = None

_DEPLOYSERVICE = _descriptor.ServiceDescriptor(
  name='DeployService',
  full_name='DeployService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=383,
  serialized_end=945,
  methods=[
  _descriptor.MethodDescriptor(
    name='startScheduleWorkflow',
    full_name='DeployService.startScheduleWorkflow',
    index=0,
    containing_service=None,
    input_type=_WORKFLOWREQUEST,
    output_type=_SCHEDULERESPONSE,
    serialized_options=_b('\202\323\344\223\002$\"\037/aiflow/deployer/workflow/start:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='stopScheduleWorkflow',
    full_name='DeployService.stopScheduleWorkflow',
    index=1,
    containing_service=None,
    input_type=_WORKFLOWREQUEST,
    output_type=_SCHEDULERESPONSE,
    serialized_options=_b('\202\323\344\223\002#\"\036/aiflow/deployer/workflow/stop:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='getWorkflowExecutionResult',
    full_name='DeployService.getWorkflowExecutionResult',
    index=2,
    containing_service=None,
    input_type=_WORKFLOWREQUEST,
    output_type=_SCHEDULERESPONSE,
    serialized_options=_b('\202\323\344\223\002%\" /aiflow/deployer/workflow/result:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='isWorkflowExecutionAlive',
    full_name='DeployService.isWorkflowExecutionAlive',
    index=3,
    containing_service=None,
    input_type=_WORKFLOWREQUEST,
    output_type=_SCHEDULERESPONSE,
    serialized_options=_b('\202\323\344\223\002$\"\037/aiflow/deployer/workflow/alive:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='getMasterConfig',
    full_name='DeployService.getMasterConfig',
    index=4,
    containing_service=None,
    input_type=_MASTERCONFIGREQUEST,
    output_type=_MASTERCONFIGRESPONSE,
    serialized_options=_b('\202\323\344\223\002,\"\'/aiflow/deployer/workflow/master_config:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_DEPLOYSERVICE)

DESCRIPTOR.services_by_name['DeployService'] = _DEPLOYSERVICE

DeployService = service_reflection.GeneratedServiceType('DeployService', (_service.Service,), dict(
  DESCRIPTOR = _DEPLOYSERVICE,
  __module__ = 'deploy_service_pb2'
  ))

DeployService_Stub = service_reflection.GeneratedServiceStubType('DeployService_Stub', (DeployService,), dict(
  DESCRIPTOR = _DEPLOYSERVICE,
  __module__ = 'deploy_service_pb2'
  ))


# @@protoc_insertion_point(module_scope)