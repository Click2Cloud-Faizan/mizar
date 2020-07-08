# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mizar/proto/droplet.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mizar/proto/droplet.proto',
  package='mizar',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x19mizar/proto/droplet.proto\x12\x05mizar\x1a\x1bgoogle/protobuf/empty.proto\"=\n\x07\x44roplet\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x0b\n\x03mac\x18\x03 \x01(\t\x12\x0b\n\x03itf\x18\x04 \x01(\t2L\n\x0e\x44ropletService\x12:\n\x0eGetDropletInfo\x12\x16.google.protobuf.Empty\x1a\x0e.mizar.Droplet\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_DROPLET = _descriptor.Descriptor(
  name='Droplet',
  full_name='mizar.Droplet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mizar.Droplet.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='mizar.Droplet.ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mac', full_name='mizar.Droplet.mac', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='itf', full_name='mizar.Droplet.itf', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=65,
  serialized_end=126,
)

DESCRIPTOR.message_types_by_name['Droplet'] = _DROPLET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Droplet = _reflection.GeneratedProtocolMessageType('Droplet', (_message.Message,), {
  'DESCRIPTOR' : _DROPLET,
  '__module__' : 'mizar.proto.droplet_pb2'
  # @@protoc_insertion_point(class_scope:mizar.Droplet)
  })
_sym_db.RegisterMessage(Droplet)



_DROPLETSERVICE = _descriptor.ServiceDescriptor(
  name='DropletService',
  full_name='mizar.DropletService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=128,
  serialized_end=204,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetDropletInfo',
    full_name='mizar.DropletService.GetDropletInfo',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_DROPLET,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DROPLETSERVICE)

DESCRIPTOR.services_by_name['DropletService'] = _DROPLETSERVICE

# @@protoc_insertion_point(module_scope)