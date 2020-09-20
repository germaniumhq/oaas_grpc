# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="test.proto",
    package="",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\ntest.proto"\x14\n\x04Ping\x12\x0c\n\x04text\x18\x01 \x01(\t"!\n\x04Pong\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0b\n\x03len\x18\x02 \x01(\x05\x32%\n\x0bTestService\x12\x16\n\x04ping\x12\x05.Ping\x1a\x05.Ping"\x00\x62\x06proto3',
)


_PING = _descriptor.Descriptor(
    name="Ping",
    full_name="Ping",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="text",
            full_name="Ping.text",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=14,
    serialized_end=34,
)


_PONG = _descriptor.Descriptor(
    name="Pong",
    full_name="Pong",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="text",
            full_name="Pong.text",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="len",
            full_name="Pong.len",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=36,
    serialized_end=69,
)

DESCRIPTOR.message_types_by_name["Ping"] = _PING
DESCRIPTOR.message_types_by_name["Pong"] = _PONG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Ping = _reflection.GeneratedProtocolMessageType(
    "Ping",
    (_message.Message,),
    {
        "DESCRIPTOR": _PING,
        "__module__": "test_pb2"
        # @@protoc_insertion_point(class_scope:Ping)
    },
)
_sym_db.RegisterMessage(Ping)

Pong = _reflection.GeneratedProtocolMessageType(
    "Pong",
    (_message.Message,),
    {
        "DESCRIPTOR": _PONG,
        "__module__": "test_pb2"
        # @@protoc_insertion_point(class_scope:Pong)
    },
)
_sym_db.RegisterMessage(Pong)


_TESTSERVICE = _descriptor.ServiceDescriptor(
    name="TestService",
    full_name="TestService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=71,
    serialized_end=108,
    methods=[
        _descriptor.MethodDescriptor(
            name="ping",
            full_name="TestService.ping",
            index=0,
            containing_service=None,
            input_type=_PING,
            output_type=_PING,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_TESTSERVICE)

DESCRIPTOR.services_by_name["TestService"] = _TESTSERVICE

# @@protoc_insertion_point(module_scope)
