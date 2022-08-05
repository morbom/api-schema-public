# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kentik/audit/v202208beta2/audit.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from kentik.core.v202012alpha1 import annotations_pb2 as kentik_dot_core_dot_v202012alpha1_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%kentik/audit/v202208beta2/audit.proto\x12\x19kentik.audit.v202208beta2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a+kentik/core/v202012alpha1/annotations.proto\"\xd9\x04\n\x0cRequestEvent\x12%\n\x0erequest_method\x18\x01 \x01(\tR\rrequestMethod\x12!\n\x0crequest_path\x18\x02 \x01(\tR\x0brequestPath\x12%\n\x0e\x63lient_address\x18\x03 \x01(\tR\rclientAddress\x12#\n\rresponse_code\x18\x04 \x01(\rR\x0cresponseCode\x12g\n\x10request_metadata\x18\x05 \x03(\x0b\x32<.kentik.audit.v202208beta2.RequestEvent.RequestMetadataEntryR\x0frequestMetadata\x12j\n\x11response_metadata\x18\x06 \x03(\x0b\x32=.kentik.audit.v202208beta2.RequestEvent.ResponseMetadataEntryR\x10responseMetadata\x12U\n\x10request_protocol\x18\x07 \x01(\x0e\x32*.kentik.audit.v202208beta2.RequestProtocolR\x0frequestProtocol\x1a\x42\n\x14RequestMetadataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1a\x43\n\x15ResponseMetadataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xe3\x02\n\nAuditEvent\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x1d\n\ncompany_id\x18\x02 \x01(\tR\tcompanyId\x12!\n\x0cservice_name\x18\x03 \x01(\tR\x0bserviceName\x12\x19\n\x08\x65vent_id\x18\x04 \x01(\tR\x07\x65ventId\x12\x30\n\x05\x63time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x05\x63time\x12#\n\revent_payload\x18\x06 \x01(\tR\x0c\x65ventPayload\x12%\n\x0e\x63orrelation_id\x18\x07 \x01(\tR\rcorrelationId\x12\x0e\n\x02id\x18\x08 \x01(\x04R\x02id\x12\x43\n\x07request\x18\x14 \x01(\x0b\x32\'.kentik.audit.v202208beta2.RequestEventH\x00R\x07requestB\x0c\n\nevent_type\"Y\n\x18\x43reateAuditEventsRequest\x12=\n\x06\x65vents\x18\x01 \x03(\x0b\x32%.kentik.audit.v202208beta2.AuditEventR\x06\x65vents\"\x1b\n\x19\x43reateAuditEventsResponse\"\xca\x01\n\x16ListAuditEventsRequest\x12\x39\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12\x1e\n\x06offset\x18\x0f \x01(\x04\x42\x06\x92\x41\x03:\x01\x30R\x06offset\x12\x1e\n\x05limit\x18\x10 \x01(\x04\x42\x08\x92\x41\x05:\x03\x31\x30\x30R\x05limit\"X\n\x17ListAuditEventsResponse\x12=\n\x06\x65vents\x18\x01 \x03(\x0b\x32%.kentik.audit.v202208beta2.AuditEventR\x06\x65vents\"X\n\x14GetAuditEventRequest\x12\x0e\n\x02id\x18\x01 \x01(\x03R\x02id\x12\x30\n\x05\x63time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x05\x63time\"T\n\x15GetAuditEventResponse\x12;\n\x05\x65vent\x18\x01 \x01(\x0b\x32%.kentik.audit.v202208beta2.AuditEventR\x05\x65vent*i\n\x0fRequestProtocol\x12 \n\x1cREQUEST_PROTOCOL_UNSPECIFIED\x10\x00\x12\x19\n\x15REQUEST_PROTOCOL_REST\x10\x01\x12\x19\n\x15REQUEST_PROTOCOL_GRPC\x10\x02\x32\xb9\x06\n\x0c\x41uditService\x12\x91\x02\n\x11\x43reateAuditEvents\x12\x33.kentik.audit.v202208beta2.CreateAuditEventsRequest\x1a\x34.kentik.audit.v202208beta2.CreateAuditEventsResponse\"\x90\x01\x92\x41Y\x12!Create one ore more audit events.\x1a!Create one ore more audit events.*\x11\x43reateAuditEvents\xf2\xd7\x02\x0b\x61udit:write\x82\xd3\xe4\x93\x02\x1f\"\x1a/audit/v202208beta2/events:\x01*\x12\xf2\x01\n\x0fListAuditEvents\x12\x31.kentik.audit.v202208beta2.ListAuditEventsRequest\x1a\x32.kentik.audit.v202208beta2.ListAuditEventsResponse\"x\x92\x41\x45\x12\x12List Audit Events.\x1a\x1fReturns a list of audit events.*\x0e\x41uditEventList\xf2\xd7\x02\naudit:read\x82\xd3\xe4\x93\x02\x1c\x12\x1a/audit/v202208beta2/events\x12\xf8\x01\n\rGetAuditEvent\x12/.kentik.audit.v202208beta2.GetAuditEventRequest\x1a\x30.kentik.audit.v202208beta2.GetAuditEventResponse\"\x83\x01\x92\x41\x43\x12\x12Get an Audit Event\x1a\x1eReturn a specific audit event.*\rGetAuditEvent\xf2\xd7\x02\naudit:read\x82\xd3\xe4\x93\x02)\x12\'/audit/v202208beta2/events/{id}/{ctime}\x1a%\xca\x41\x13grpc.api.kentik.com\xea\xd7\x02\x0b\x61\x64min.auditB\xd8\x02ZCgithub.com/kentik/api-schema/gen/go/kentik/audit/v202208beta2;audit\x92\x41\x8f\x02\x12Q\n\tAudit API\"7\n\x16Kentik API Engineering\x12\x1dhttps://github.com/kentik/api2\x0b\x32\x30\x32\x32\x30\x38\x62\x65ta1*\x01\x02\x32\x10\x61pplication/json:\x10\x61pplication/jsonZD\n\x1e\n\x05\x65mail\x12\x15\x08\x02\x1a\x0fX-CH-Auth-Email \x02\n\"\n\x05token\x12\x19\x08\x02\x1a\x13X-CH-Auth-API-Token \x02\x62\x16\n\t\n\x05\x65mail\x12\x00\n\t\n\x05token\x12\x00r5\n\x16More about Kentik APIs\x12\x1bhttps://docs.kentik.com/apib\x06proto3')

_REQUESTPROTOCOL = DESCRIPTOR.enum_types_by_name['RequestProtocol']
RequestProtocol = enum_type_wrapper.EnumTypeWrapper(_REQUESTPROTOCOL)
REQUEST_PROTOCOL_UNSPECIFIED = 0
REQUEST_PROTOCOL_REST = 1
REQUEST_PROTOCOL_GRPC = 2


_REQUESTEVENT = DESCRIPTOR.message_types_by_name['RequestEvent']
_REQUESTEVENT_REQUESTMETADATAENTRY = _REQUESTEVENT.nested_types_by_name['RequestMetadataEntry']
_REQUESTEVENT_RESPONSEMETADATAENTRY = _REQUESTEVENT.nested_types_by_name['ResponseMetadataEntry']
_AUDITEVENT = DESCRIPTOR.message_types_by_name['AuditEvent']
_CREATEAUDITEVENTSREQUEST = DESCRIPTOR.message_types_by_name['CreateAuditEventsRequest']
_CREATEAUDITEVENTSRESPONSE = DESCRIPTOR.message_types_by_name['CreateAuditEventsResponse']
_LISTAUDITEVENTSREQUEST = DESCRIPTOR.message_types_by_name['ListAuditEventsRequest']
_LISTAUDITEVENTSRESPONSE = DESCRIPTOR.message_types_by_name['ListAuditEventsResponse']
_GETAUDITEVENTREQUEST = DESCRIPTOR.message_types_by_name['GetAuditEventRequest']
_GETAUDITEVENTRESPONSE = DESCRIPTOR.message_types_by_name['GetAuditEventResponse']
RequestEvent = _reflection.GeneratedProtocolMessageType('RequestEvent', (_message.Message,), {

  'RequestMetadataEntry' : _reflection.GeneratedProtocolMessageType('RequestMetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _REQUESTEVENT_REQUESTMETADATAENTRY,
    '__module__' : 'kentik.audit.v202208beta2.audit_pb2'
    # @@protoc_insertion_point(class_scope:kentik.audit.v202208beta2.RequestEvent.RequestMetadataEntry)
    })
  ,

  'ResponseMetadataEntry' : _reflection.GeneratedProtocolMessageType('ResponseMetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _REQUESTEVENT_RESPONSEMETADATAENTRY,
    '__module__' : 'kentik.audit.v202208beta2.audit_pb2'
    # @@protoc_insertion_point(class_scope:kentik.audit.v202208beta2.RequestEvent.ResponseMetadataEntry)
    })
  ,
  'DESCRIPTOR' : _REQUESTEVENT,
  '__module__' : 'kentik.audit.v202208beta2.audit_pb2'
  # @@protoc_insertion_point(class_scope:kentik.audit.v202208beta2.RequestEvent)
  })
_sym_db.RegisterMessage(RequestEvent)
_sym_db.RegisterMessage(RequestEvent.RequestMetadataEntry)
_sym_db.RegisterMessage(RequestEvent.ResponseMetadataEntry)

AuditEvent = _reflection.GeneratedProtocolMessageType('AuditEvent', (_message.Message,), {
  'DESCRIPTOR' : _AUDITEVENT,
  '__module__' : 'kentik.audit.v202208beta2.audit_pb2'
  # @@protoc_insertion_point(class_scope:kentik.audit.v202208beta2.AuditEvent)
  })
_sym_db.RegisterMessage(AuditEvent)

CreateAuditEventsRequest = _reflection.GeneratedProtocolMessageType('CreateAuditEventsRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEAUDITEVENTSREQUEST,
  '__module__' : 'kentik.audit.v202208beta2.audit_pb2'
  # @@protoc_insertion_point(class_scope:kentik.audit.v202208beta2.CreateAuditEventsRequest)
  })
_sym_db.RegisterMessage(CreateAuditEventsRequest)

CreateAuditEventsResponse = _reflection.GeneratedProtocolMessageType('CreateAuditEventsResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEAUDITEVENTSRESPONSE,
  '__module__' : 'kentik.audit.v202208beta2.audit_pb2'
  # @@protoc_insertion_point(class_scope:kentik.audit.v202208beta2.CreateAuditEventsResponse)
  })
_sym_db.RegisterMessage(CreateAuditEventsResponse)

ListAuditEventsRequest = _reflection.GeneratedProtocolMessageType('ListAuditEventsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTAUDITEVENTSREQUEST,
  '__module__' : 'kentik.audit.v202208beta2.audit_pb2'
  # @@protoc_insertion_point(class_scope:kentik.audit.v202208beta2.ListAuditEventsRequest)
  })
_sym_db.RegisterMessage(ListAuditEventsRequest)

ListAuditEventsResponse = _reflection.GeneratedProtocolMessageType('ListAuditEventsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTAUDITEVENTSRESPONSE,
  '__module__' : 'kentik.audit.v202208beta2.audit_pb2'
  # @@protoc_insertion_point(class_scope:kentik.audit.v202208beta2.ListAuditEventsResponse)
  })
_sym_db.RegisterMessage(ListAuditEventsResponse)

GetAuditEventRequest = _reflection.GeneratedProtocolMessageType('GetAuditEventRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETAUDITEVENTREQUEST,
  '__module__' : 'kentik.audit.v202208beta2.audit_pb2'
  # @@protoc_insertion_point(class_scope:kentik.audit.v202208beta2.GetAuditEventRequest)
  })
_sym_db.RegisterMessage(GetAuditEventRequest)

GetAuditEventResponse = _reflection.GeneratedProtocolMessageType('GetAuditEventResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETAUDITEVENTRESPONSE,
  '__module__' : 'kentik.audit.v202208beta2.audit_pb2'
  # @@protoc_insertion_point(class_scope:kentik.audit.v202208beta2.GetAuditEventResponse)
  })
_sym_db.RegisterMessage(GetAuditEventResponse)

_AUDITSERVICE = DESCRIPTOR.services_by_name['AuditService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZCgithub.com/kentik/api-schema/gen/go/kentik/audit/v202208beta2;audit\222A\217\002\022Q\n\tAudit API\"7\n\026Kentik API Engineering\022\035https://github.com/kentik/api2\013202208beta1*\001\0022\020application/json:\020application/jsonZD\n\036\n\005email\022\025\010\002\032\017X-CH-Auth-Email \002\n\"\n\005token\022\031\010\002\032\023X-CH-Auth-API-Token \002b\026\n\t\n\005email\022\000\n\t\n\005token\022\000r5\n\026More about Kentik APIs\022\033https://docs.kentik.com/api'
  _REQUESTEVENT_REQUESTMETADATAENTRY._options = None
  _REQUESTEVENT_REQUESTMETADATAENTRY._serialized_options = b'8\001'
  _REQUESTEVENT_RESPONSEMETADATAENTRY._options = None
  _REQUESTEVENT_RESPONSEMETADATAENTRY._serialized_options = b'8\001'
  _LISTAUDITEVENTSREQUEST.fields_by_name['offset']._options = None
  _LISTAUDITEVENTSREQUEST.fields_by_name['offset']._serialized_options = b'\222A\003:\0010'
  _LISTAUDITEVENTSREQUEST.fields_by_name['limit']._options = None
  _LISTAUDITEVENTSREQUEST.fields_by_name['limit']._serialized_options = b'\222A\005:\003100'
  _AUDITSERVICE._options = None
  _AUDITSERVICE._serialized_options = b'\312A\023grpc.api.kentik.com\352\327\002\013admin.audit'
  _AUDITSERVICE.methods_by_name['CreateAuditEvents']._options = None
  _AUDITSERVICE.methods_by_name['CreateAuditEvents']._serialized_options = b'\222AY\022!Create one ore more audit events.\032!Create one ore more audit events.*\021CreateAuditEvents\362\327\002\013audit:write\202\323\344\223\002\037\"\032/audit/v202208beta2/events:\001*'
  _AUDITSERVICE.methods_by_name['ListAuditEvents']._options = None
  _AUDITSERVICE.methods_by_name['ListAuditEvents']._serialized_options = b'\222AE\022\022List Audit Events.\032\037Returns a list of audit events.*\016AuditEventList\362\327\002\naudit:read\202\323\344\223\002\034\022\032/audit/v202208beta2/events'
  _AUDITSERVICE.methods_by_name['GetAuditEvent']._options = None
  _AUDITSERVICE.methods_by_name['GetAuditEvent']._serialized_options = b'\222AC\022\022Get an Audit Event\032\036Return a specific audit event.*\rGetAuditEvent\362\327\002\naudit:read\202\323\344\223\002)\022\'/audit/v202208beta2/events/{id}/{ctime}'
  _REQUESTPROTOCOL._serialized_start=1802
  _REQUESTPROTOCOL._serialized_end=1907
  _REQUESTEVENT._serialized_start=250
  _REQUESTEVENT._serialized_end=851
  _REQUESTEVENT_REQUESTMETADATAENTRY._serialized_start=716
  _REQUESTEVENT_REQUESTMETADATAENTRY._serialized_end=782
  _REQUESTEVENT_RESPONSEMETADATAENTRY._serialized_start=784
  _REQUESTEVENT_RESPONSEMETADATAENTRY._serialized_end=851
  _AUDITEVENT._serialized_start=854
  _AUDITEVENT._serialized_end=1209
  _CREATEAUDITEVENTSREQUEST._serialized_start=1211
  _CREATEAUDITEVENTSREQUEST._serialized_end=1300
  _CREATEAUDITEVENTSRESPONSE._serialized_start=1302
  _CREATEAUDITEVENTSRESPONSE._serialized_end=1329
  _LISTAUDITEVENTSREQUEST._serialized_start=1332
  _LISTAUDITEVENTSREQUEST._serialized_end=1534
  _LISTAUDITEVENTSRESPONSE._serialized_start=1536
  _LISTAUDITEVENTSRESPONSE._serialized_end=1624
  _GETAUDITEVENTREQUEST._serialized_start=1626
  _GETAUDITEVENTREQUEST._serialized_end=1714
  _GETAUDITEVENTRESPONSE._serialized_start=1716
  _GETAUDITEVENTRESPONSE._serialized_end=1800
  _AUDITSERVICE._serialized_start=1910
  _AUDITSERVICE._serialized_end=2735
# @@protoc_insertion_point(module_scope)