# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cserver.proto\"\x1c\n\x07GetFile\x12\x11\n\tfile_name\x18\x01 \x01(\t\"K\n\nFileResult\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x13\n\x0btotal_parts\x18\x02 \x01(\x05\x12\x15\n\x05parts\x18\x03 \x03(\x0b\x32\x06.Parts\"\x15\n\x05Parts\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x32\x31\n\x0b\x46ileService\x12\"\n\x07getFile\x12\x08.GetFile\x1a\x0b.FileResult\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'server_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETFILE']._serialized_start=16
  _globals['_GETFILE']._serialized_end=44
  _globals['_FILERESULT']._serialized_start=46
  _globals['_FILERESULT']._serialized_end=121
  _globals['_PARTS']._serialized_start=123
  _globals['_PARTS']._serialized_end=144
  _globals['_FILESERVICE']._serialized_start=146
  _globals['_FILESERVICE']._serialized_end=195
# @@protoc_insertion_point(module_scope)