# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='config.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0c\x63onfig.proto\"$\n\x06\x43onfig\x12\x1a\n\x08\x63ontrols\x18\x01 \x03(\x0b\x32\x08.Control\"\xa0\x01\n\x07\x43ontrol\x12(\n\x0etactile_switch\x18\x01 \x01(\x0b\x32\x0e.TactileSwitchH\x00\x12(\n\x0erotary_encoder\x18\x02 \x01(\x0b\x32\x0e.RotaryEncoderH\x00\x12\x31\n\x13\x64ual_rotary_encoder\x18\x03 \x01(\x0b\x32\x12.DualRotaryEncoderH\x00\x42\x0e\n\x0c\x63ontrol_type\"A\n\rTactileSwitch\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03pin\x18\x02 \x01(\x05\x12\x15\n\rpush_event_id\x18\x03 \x01(\x05\"\x9b\x01\n\rRotaryEncoder\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63lk_pin\x18\x02 \x01(\x05\x12\x0e\n\x06\x64t_pin\x18\x03 \x01(\x05\x12\x0e\n\x06sw_pin\x18\x04 \x01(\x05\x12\x19\n\x11increase_event_id\x18\x05 \x01(\x05\x12\x19\n\x11\x64\x65\x63rease_event_id\x18\x06 \x01(\x05\x12\x15\n\rpush_event_id\x18\x07 \x01(\x05\"\xa6\x02\n\x11\x44ualRotaryEncoder\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rlarge_clk_pin\x18\x02 \x01(\x05\x12\x14\n\x0clarge_dt_pin\x18\x03 \x01(\x05\x12\x15\n\rsmall_clk_pin\x18\x04 \x01(\x05\x12\x14\n\x0csmall_dt_pin\x18\x05 \x01(\x05\x12\x0e\n\x06sw_pin\x18\x06 \x01(\x05\x12\x1f\n\x17large_increase_event_id\x18\x07 \x01(\x05\x12\x1f\n\x17large_decrease_event_id\x18\x08 \x01(\x05\x12\x1f\n\x17small_increase_event_id\x18\t \x01(\x05\x12\x1f\n\x17small_decrease_event_id\x18\n \x01(\x05\x12\x15\n\rpush_event_id\x18\x0b \x01(\x05\x62\x06proto3')
)




_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='controls', full_name='Config.controls', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=16,
  serialized_end=52,
)


_CONTROL = _descriptor.Descriptor(
  name='Control',
  full_name='Control',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tactile_switch', full_name='Control.tactile_switch', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rotary_encoder', full_name='Control.rotary_encoder', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dual_rotary_encoder', full_name='Control.dual_rotary_encoder', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='control_type', full_name='Control.control_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=55,
  serialized_end=215,
)


_TACTILESWITCH = _descriptor.Descriptor(
  name='TactileSwitch',
  full_name='TactileSwitch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='TactileSwitch.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pin', full_name='TactileSwitch.pin', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='push_event_id', full_name='TactileSwitch.push_event_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=217,
  serialized_end=282,
)


_ROTARYENCODER = _descriptor.Descriptor(
  name='RotaryEncoder',
  full_name='RotaryEncoder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='RotaryEncoder.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clk_pin', full_name='RotaryEncoder.clk_pin', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dt_pin', full_name='RotaryEncoder.dt_pin', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sw_pin', full_name='RotaryEncoder.sw_pin', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='increase_event_id', full_name='RotaryEncoder.increase_event_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='decrease_event_id', full_name='RotaryEncoder.decrease_event_id', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='push_event_id', full_name='RotaryEncoder.push_event_id', index=6,
      number=7, type=5, cpp_type=1, label=1,
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
  serialized_start=285,
  serialized_end=440,
)


_DUALROTARYENCODER = _descriptor.Descriptor(
  name='DualRotaryEncoder',
  full_name='DualRotaryEncoder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='DualRotaryEncoder.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='large_clk_pin', full_name='DualRotaryEncoder.large_clk_pin', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='large_dt_pin', full_name='DualRotaryEncoder.large_dt_pin', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='small_clk_pin', full_name='DualRotaryEncoder.small_clk_pin', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='small_dt_pin', full_name='DualRotaryEncoder.small_dt_pin', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sw_pin', full_name='DualRotaryEncoder.sw_pin', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='large_increase_event_id', full_name='DualRotaryEncoder.large_increase_event_id', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='large_decrease_event_id', full_name='DualRotaryEncoder.large_decrease_event_id', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='small_increase_event_id', full_name='DualRotaryEncoder.small_increase_event_id', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='small_decrease_event_id', full_name='DualRotaryEncoder.small_decrease_event_id', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='push_event_id', full_name='DualRotaryEncoder.push_event_id', index=10,
      number=11, type=5, cpp_type=1, label=1,
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
  serialized_start=443,
  serialized_end=737,
)

_CONFIG.fields_by_name['controls'].message_type = _CONTROL
_CONTROL.fields_by_name['tactile_switch'].message_type = _TACTILESWITCH
_CONTROL.fields_by_name['rotary_encoder'].message_type = _ROTARYENCODER
_CONTROL.fields_by_name['dual_rotary_encoder'].message_type = _DUALROTARYENCODER
_CONTROL.oneofs_by_name['control_type'].fields.append(
  _CONTROL.fields_by_name['tactile_switch'])
_CONTROL.fields_by_name['tactile_switch'].containing_oneof = _CONTROL.oneofs_by_name['control_type']
_CONTROL.oneofs_by_name['control_type'].fields.append(
  _CONTROL.fields_by_name['rotary_encoder'])
_CONTROL.fields_by_name['rotary_encoder'].containing_oneof = _CONTROL.oneofs_by_name['control_type']
_CONTROL.oneofs_by_name['control_type'].fields.append(
  _CONTROL.fields_by_name['dual_rotary_encoder'])
_CONTROL.fields_by_name['dual_rotary_encoder'].containing_oneof = _CONTROL.oneofs_by_name['control_type']
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['Control'] = _CONTROL
DESCRIPTOR.message_types_by_name['TactileSwitch'] = _TACTILESWITCH
DESCRIPTOR.message_types_by_name['RotaryEncoder'] = _ROTARYENCODER
DESCRIPTOR.message_types_by_name['DualRotaryEncoder'] = _DUALROTARYENCODER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'config_pb2'
  # @@protoc_insertion_point(class_scope:Config)
  ))
_sym_db.RegisterMessage(Config)

Control = _reflection.GeneratedProtocolMessageType('Control', (_message.Message,), dict(
  DESCRIPTOR = _CONTROL,
  __module__ = 'config_pb2'
  # @@protoc_insertion_point(class_scope:Control)
  ))
_sym_db.RegisterMessage(Control)

TactileSwitch = _reflection.GeneratedProtocolMessageType('TactileSwitch', (_message.Message,), dict(
  DESCRIPTOR = _TACTILESWITCH,
  __module__ = 'config_pb2'
  # @@protoc_insertion_point(class_scope:TactileSwitch)
  ))
_sym_db.RegisterMessage(TactileSwitch)

RotaryEncoder = _reflection.GeneratedProtocolMessageType('RotaryEncoder', (_message.Message,), dict(
  DESCRIPTOR = _ROTARYENCODER,
  __module__ = 'config_pb2'
  # @@protoc_insertion_point(class_scope:RotaryEncoder)
  ))
_sym_db.RegisterMessage(RotaryEncoder)

DualRotaryEncoder = _reflection.GeneratedProtocolMessageType('DualRotaryEncoder', (_message.Message,), dict(
  DESCRIPTOR = _DUALROTARYENCODER,
  __module__ = 'config_pb2'
  # @@protoc_insertion_point(class_scope:DualRotaryEncoder)
  ))
_sym_db.RegisterMessage(DualRotaryEncoder)


# @@protoc_insertion_point(module_scope)
