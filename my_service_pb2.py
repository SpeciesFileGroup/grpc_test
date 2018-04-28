# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: my_service.proto

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
  name='my_service.proto',
  package='handson',
  syntax='proto3',
  serialized_pb=_b('\n\x10my_service.proto\x12\x07handson\">\n\tMyRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x10\n\x08\x66iletext\x18\x02 \x01(\t\x12\r\n\x05\x63ount\x18\x03 \x01(\x05\"?\n\nMyResponse\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x10\n\x08\x66iletext\x18\x02 \x01(\t\x12\r\n\x05\x63ount\x18\x03 \x01(\x05\x32\xf3\x01\n\tMyService\x12\x36\n\tMyMethod1\x12\x12.handson.MyRequest\x1a\x13.handson.MyResponse\"\x00\x12\x36\n\tMyMethod2\x12\x12.handson.MyRequest\x1a\x13.handson.MyResponse\"\x00\x12:\n\tMyMethod3\x12\x12.handson.MyRequest\x1a\x13.handson.MyResponse\"\x00(\x01\x30\x01\x12:\n\tMyMethod4\x12\x12.handson.MyRequest\x1a\x13.handson.MyResponse\"\x00(\x01\x30\x01\x42\x32\n\x18\x63om.alexandreesl.handsonB\x0eMyServiceProtoP\x01\xa2\x02\x03HLWb\x06proto3')
)




_MYREQUEST = _descriptor.Descriptor(
  name='MyRequest',
  full_name='handson.MyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='handson.MyRequest.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filetext', full_name='handson.MyRequest.filetext', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='handson.MyRequest.count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=29,
  serialized_end=91,
)


_MYRESPONSE = _descriptor.Descriptor(
  name='MyResponse',
  full_name='handson.MyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='handson.MyResponse.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filetext', full_name='handson.MyResponse.filetext', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='handson.MyResponse.count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=93,
  serialized_end=156,
)

DESCRIPTOR.message_types_by_name['MyRequest'] = _MYREQUEST
DESCRIPTOR.message_types_by_name['MyResponse'] = _MYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MyRequest = _reflection.GeneratedProtocolMessageType('MyRequest', (_message.Message,), dict(
  DESCRIPTOR = _MYREQUEST,
  __module__ = 'my_service_pb2'
  # @@protoc_insertion_point(class_scope:handson.MyRequest)
  ))
_sym_db.RegisterMessage(MyRequest)

MyResponse = _reflection.GeneratedProtocolMessageType('MyResponse', (_message.Message,), dict(
  DESCRIPTOR = _MYRESPONSE,
  __module__ = 'my_service_pb2'
  # @@protoc_insertion_point(class_scope:handson.MyResponse)
  ))
_sym_db.RegisterMessage(MyResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030com.alexandreesl.handsonB\016MyServiceProtoP\001\242\002\003HLW'))

_MYSERVICE = _descriptor.ServiceDescriptor(
  name='MyService',
  full_name='handson.MyService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=159,
  serialized_end=402,
  methods=[
  _descriptor.MethodDescriptor(
    name='MyMethod1',
    full_name='handson.MyService.MyMethod1',
    index=0,
    containing_service=None,
    input_type=_MYREQUEST,
    output_type=_MYRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MyMethod2',
    full_name='handson.MyService.MyMethod2',
    index=1,
    containing_service=None,
    input_type=_MYREQUEST,
    output_type=_MYRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MyMethod3',
    full_name='handson.MyService.MyMethod3',
    index=2,
    containing_service=None,
    input_type=_MYREQUEST,
    output_type=_MYRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MyMethod4',
    full_name='handson.MyService.MyMethod4',
    index=3,
    containing_service=None,
    input_type=_MYREQUEST,
    output_type=_MYRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MYSERVICE)

DESCRIPTOR.services_by_name['MyService'] = _MYSERVICE

# @@protoc_insertion_point(module_scope)
