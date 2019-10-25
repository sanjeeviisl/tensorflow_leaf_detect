# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/flexible_grid_anchor_generator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_detection/protos/flexible_grid_anchor_generator.proto',
  package='object_detection.protos',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n<object_detection/protos/flexible_grid_anchor_generator.proto\x12\x17object_detection.protos\"|\n\x1b\x46lexibleGridAnchorGenerator\x12\x38\n\x0b\x61nchor_grid\x18\x01 \x03(\x0b\x32#.object_detection.protos.AnchorGrid\x12#\n\x15normalize_coordinates\x18\x02 \x01(\x08:\x04true\"\x97\x01\n\nAnchorGrid\x12\x12\n\nbase_sizes\x18\x01 \x03(\x02\x12\x15\n\raspect_ratios\x18\x02 \x03(\x02\x12\x15\n\rheight_stride\x18\x03 \x01(\r\x12\x14\n\x0cwidth_stride\x18\x04 \x01(\r\x12\x18\n\rheight_offset\x18\x05 \x01(\r:\x01\x30\x12\x17\n\x0cwidth_offset\x18\x06 \x01(\r:\x01\x30')
)




_FLEXIBLEGRIDANCHORGENERATOR = _descriptor.Descriptor(
  name='FlexibleGridAnchorGenerator',
  full_name='object_detection.protos.FlexibleGridAnchorGenerator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='anchor_grid', full_name='object_detection.protos.FlexibleGridAnchorGenerator.anchor_grid', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='normalize_coordinates', full_name='object_detection.protos.FlexibleGridAnchorGenerator.normalize_coordinates', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=213,
)


_ANCHORGRID = _descriptor.Descriptor(
  name='AnchorGrid',
  full_name='object_detection.protos.AnchorGrid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_sizes', full_name='object_detection.protos.AnchorGrid.base_sizes', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aspect_ratios', full_name='object_detection.protos.AnchorGrid.aspect_ratios', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height_stride', full_name='object_detection.protos.AnchorGrid.height_stride', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width_stride', full_name='object_detection.protos.AnchorGrid.width_stride', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height_offset', full_name='object_detection.protos.AnchorGrid.height_offset', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width_offset', full_name='object_detection.protos.AnchorGrid.width_offset', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=367,
)

_FLEXIBLEGRIDANCHORGENERATOR.fields_by_name['anchor_grid'].message_type = _ANCHORGRID
DESCRIPTOR.message_types_by_name['FlexibleGridAnchorGenerator'] = _FLEXIBLEGRIDANCHORGENERATOR
DESCRIPTOR.message_types_by_name['AnchorGrid'] = _ANCHORGRID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FlexibleGridAnchorGenerator = _reflection.GeneratedProtocolMessageType('FlexibleGridAnchorGenerator', (_message.Message,), dict(
  DESCRIPTOR = _FLEXIBLEGRIDANCHORGENERATOR,
  __module__ = 'object_detection.protos.flexible_grid_anchor_generator_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.FlexibleGridAnchorGenerator)
  ))
_sym_db.RegisterMessage(FlexibleGridAnchorGenerator)

AnchorGrid = _reflection.GeneratedProtocolMessageType('AnchorGrid', (_message.Message,), dict(
  DESCRIPTOR = _ANCHORGRID,
  __module__ = 'object_detection.protos.flexible_grid_anchor_generator_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.AnchorGrid)
  ))
_sym_db.RegisterMessage(AnchorGrid)


# @@protoc_insertion_point(module_scope)
