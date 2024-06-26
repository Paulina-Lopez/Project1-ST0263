# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63onfig.proto\"#\n\x0eGetFileRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\"P\n\x0fGetFileResponse\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x13\n\x0btotal_parts\x18\x02 \x01(\x05\x12\x15\n\x05parts\x18\x03 \x03(\x0b\x32\x06.Parts\"9\n\x05Parts\x12\x0f\n\x07part_id\x18\x01 \x01(\x05\x12\x11\n\tpart_name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"J\n\x0fSaveFileRequest\x12\x13\n\x0bglobal_name\x18\x01 \x01(\t\x12\x11\n\tfile_name\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\x0c\"5\n\x10SaveFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x11\n\tfile_name\x18\x02 \x01(\t\"^\n\x14ReplicateFileRequest\x12\x12\n\nfile_parts\x18\x01 \x03(\t\x12\x18\n\x10source_directory\x18\x02 \x01(\t\x12\x18\n\x10target_directory\x18\x03 \x01(\t\"(\n\x15ReplicateFileResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"O\n\x10\x43loneFileRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x12\n\nrecieve_ip\x18\x02 \x01(\t\x12\x14\n\x0crecieve_port\x18\x03 \x01(\t\"6\n\x11\x43loneFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x11\n\tfile_name\x18\x02 \x01(\t2\xe8\x01\n\x0b\x46ileService\x12.\n\x07getFile\x12\x0f.GetFileRequest\x1a\x10.GetFileResponse\"\x00\x12\x31\n\x08saveFile\x12\x10.SaveFileRequest\x1a\x11.SaveFileResponse\"\x00\x12\x34\n\tcloneFile\x12\x11.CloneFileRequest\x1a\x12.CloneFileResponse\"\x00\x12@\n\rReplicateFile\x12\x15.ReplicateFileRequest\x1a\x16.ReplicateFileResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETFILEREQUEST']._serialized_start=16
  _globals['_GETFILEREQUEST']._serialized_end=51
  _globals['_GETFILERESPONSE']._serialized_start=53
  _globals['_GETFILERESPONSE']._serialized_end=133
  _globals['_PARTS']._serialized_start=135
  _globals['_PARTS']._serialized_end=192
  _globals['_SAVEFILEREQUEST']._serialized_start=194
  _globals['_SAVEFILEREQUEST']._serialized_end=268
  _globals['_SAVEFILERESPONSE']._serialized_start=270
  _globals['_SAVEFILERESPONSE']._serialized_end=323
  _globals['_REPLICATEFILEREQUEST']._serialized_start=325
  _globals['_REPLICATEFILEREQUEST']._serialized_end=419
  _globals['_REPLICATEFILERESPONSE']._serialized_start=421
  _globals['_REPLICATEFILERESPONSE']._serialized_end=461
  _globals['_CLONEFILEREQUEST']._serialized_start=463
  _globals['_CLONEFILEREQUEST']._serialized_end=542
  _globals['_CLONEFILERESPONSE']._serialized_start=544
  _globals['_CLONEFILERESPONSE']._serialized_end=598
  _globals['_FILESERVICE']._serialized_start=601
  _globals['_FILESERVICE']._serialized_end=833
# @@protoc_insertion_point(module_scope)
