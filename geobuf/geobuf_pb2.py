# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: geobuf.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cgeobuf.proto\"\xde\x07\n\x04\x44\x61ta\x12\x0c\n\x04keys\x18\x01 \x03(\t\x12\x12\n\ndimensions\x18\x02 \x01(\r\x12\x11\n\tprecision\x18\x03 \x01(\r\x12\x35\n\x12\x66\x65\x61ture_collection\x18\x04 \x01(\x0b\x32\x17.Data.FeatureCollectionH\x00\x12 \n\x07\x66\x65\x61ture\x18\x05 \x01(\x0b\x32\r.Data.FeatureH\x00\x12\"\n\x08geometry\x18\x06 \x01(\x0b\x32\x0e.Data.GeometryH\x00\x1a\xa2\x01\n\x07\x46\x65\x61ture\x12 \n\x08geometry\x18\x01 \x01(\x0b\x32\x0e.Data.Geometry\x12\x0c\n\x02id\x18\x0b \x01(\tH\x00\x12\x10\n\x06int_id\x18\x0c \x01(\x12H\x00\x12\x1b\n\x06values\x18\r \x03(\x0b\x32\x0b.Data.Value\x12\x12\n\nproperties\x18\x0e \x03(\r\x12\x19\n\x11\x63ustom_properties\x18\x0f \x03(\rB\t\n\x07id_type\x1a\xdd\x02\n\x08Geometry\x12!\n\x04type\x18\x01 \x01(\x0e\x32\x13.Data.Geometry.Type\x12\x0f\n\x07lengths\x18\x02 \x03(\r\x12\x0e\n\x06\x63oords\x18\x03 \x03(\x12\x12\"\n\ngeometries\x18\x04 \x03(\x0b\x32\x0e.Data.Geometry\x12\x1b\n\x06values\x18\r \x03(\x0b\x32\x0b.Data.Value\x12\x19\n\x11\x63ustom_properties\x18\x0f \x03(\r\"\xb0\x01\n\x04Type\x12\x0e\n\nTYPE_EMPTY\x10\x00\x12\x0e\n\nTYPE_POINT\x10\x01\x12\x13\n\x0fTYPE_MULTIPOINT\x10\x02\x12\x13\n\x0fTYPE_LINESTRING\x10\x03\x12\x18\n\x14TYPE_MULTILINESTRING\x10\x04\x12\x10\n\x0cTYPE_POLYGON\x10\x05\x12\x15\n\x11TYPE_MULTIPOLYGON\x10\x06\x12\x1b\n\x17TYPE_GEOMETRYCOLLECTION\x10\x07\x1al\n\x11\x46\x65\x61tureCollection\x12\x1f\n\x08\x66\x65\x61tures\x18\x01 \x03(\x0b\x32\r.Data.Feature\x12\x1b\n\x06values\x18\r \x03(\x0b\x32\x0b.Data.Value\x12\x19\n\x11\x63ustom_properties\x18\x0f \x03(\r\x1a\xa3\x01\n\x05Value\x12\x16\n\x0cstring_value\x18\x01 \x01(\tH\x00\x12\x16\n\x0c\x64ouble_value\x18\x02 \x01(\x01H\x00\x12\x17\n\rpos_int_value\x18\x03 \x01(\x04H\x00\x12\x17\n\rneg_int_value\x18\x04 \x01(\x04H\x00\x12\x14\n\nbool_value\x18\x05 \x01(\x08H\x00\x12\x14\n\njson_value\x18\x06 \x01(\x0cH\x00\x42\x0c\n\nvalue_typeB\x0b\n\tdata_typeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'geobuf_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DATA']._serialized_start=17
  _globals['_DATA']._serialized_end=1007
  _globals['_DATA_FEATURE']._serialized_start=204
  _globals['_DATA_FEATURE']._serialized_end=366
  _globals['_DATA_GEOMETRY']._serialized_start=369
  _globals['_DATA_GEOMETRY']._serialized_end=718
  _globals['_DATA_GEOMETRY_TYPE']._serialized_start=542
  _globals['_DATA_GEOMETRY_TYPE']._serialized_end=718
  _globals['_DATA_FEATURECOLLECTION']._serialized_start=720
  _globals['_DATA_FEATURECOLLECTION']._serialized_end=828
  _globals['_DATA_VALUE']._serialized_start=831
  _globals['_DATA_VALUE']._serialized_end=994
# @@protoc_insertion_point(module_scope)
