# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: questionstream.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='questionstream.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x14questionstream.proto\" \n\x0fQuestionRequest\x12\r\n\x05query\x18\x01 \x01(\t\"!\n\x10QuestionResponse\x12\r\n\x05reply\x18\x01 \x01(\t2J\n\x0fQuestionService\x12\x37\n\x0cUnaryRequest\x12\x10.QuestionRequest\x1a\x11.QuestionResponse\"\x00\x30\x01\x62\x06proto3')
)




_QUESTIONREQUEST = _descriptor.Descriptor(
  name='QuestionRequest',
  full_name='QuestionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='QuestionRequest.query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=56,
)


_QUESTIONRESPONSE = _descriptor.Descriptor(
  name='QuestionResponse',
  full_name='QuestionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply', full_name='QuestionResponse.reply', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=91,
)

DESCRIPTOR.message_types_by_name['QuestionRequest'] = _QUESTIONREQUEST
DESCRIPTOR.message_types_by_name['QuestionResponse'] = _QUESTIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QuestionRequest = _reflection.GeneratedProtocolMessageType('QuestionRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUESTIONREQUEST,
  __module__ = 'questionstream_pb2'
  # @@protoc_insertion_point(class_scope:QuestionRequest)
  ))
_sym_db.RegisterMessage(QuestionRequest)

QuestionResponse = _reflection.GeneratedProtocolMessageType('QuestionResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUESTIONRESPONSE,
  __module__ = 'questionstream_pb2'
  # @@protoc_insertion_point(class_scope:QuestionResponse)
  ))
_sym_db.RegisterMessage(QuestionResponse)



_QUESTIONSERVICE = _descriptor.ServiceDescriptor(
  name='QuestionService',
  full_name='QuestionService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=93,
  serialized_end=167,
  methods=[
  _descriptor.MethodDescriptor(
    name='UnaryRequest',
    full_name='QuestionService.UnaryRequest',
    index=0,
    containing_service=None,
    input_type=_QUESTIONREQUEST,
    output_type=_QUESTIONRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUESTIONSERVICE)

DESCRIPTOR.services_by_name['QuestionService'] = _QUESTIONSERVICE

# @@protoc_insertion_point(module_scope)
