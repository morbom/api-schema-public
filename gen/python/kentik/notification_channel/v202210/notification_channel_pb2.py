# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kentik/notification_channel/v202210/notification_channel.proto
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
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from kentik.core.v202012alpha1 import annotations_pb2 as kentik_dot_core_dot_v202012alpha1_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>kentik/notification_channel/v202210/notification_channel.proto\x12#kentik.notification_channel.v202210\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a+kentik/core/v202012alpha1/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xe7\x03\n\x13NotificationChannel\x12\x39\n\x02id\x18\x01 \x01(\tB)\x92\x41\"2 Unique identifier of the channel\xe2\x41\x01\x03R\x02id\x12>\n\x04name\x18\x02 \x01(\tB*\x92\x41#2!User selected name of the channel\xe2\x41\x01\x03R\x04name\x12h\n\x04type\x18\x03 \x01(\x0e\x32\x30.kentik.notification_channel.v202210.ChannelTypeB\"\x92\x41\x1b\x32\x19Notification channel type\xe2\x41\x01\x03R\x04type\x12\x38\n\x07\x65nabled\x18\x04 \x01(\x08\x42\x1e\x92\x41\x17\x32\x15\x41\x64ministrative status\xe2\x41\x01\x03R\x07\x65nabled\x12S\n\x05\x63\x64\x61te\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB!\x92\x41\x1a\x32\x18\x43reation timestamp (UTC)\xe2\x41\x01\x03R\x05\x63\x64\x61te\x12\\\n\x05\x65\x64\x61te\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB*\x92\x41#2!Last modification timestamp (UTC)\xe2\x41\x01\x03R\x05\x65\x64\x61te\"!\n\x1fListNotificationChannelsRequest\"\xbf\x02\n ListNotificationChannelsResponse\x12\x95\x01\n\x15notification_channels\x18\x01 \x03(\x0b\x32\x38.kentik.notification_channel.v202210.NotificationChannelB&\x92\x41\x1f\x32\x1dList of notification channels\xe2\x41\x01\x03R\x14notificationChannels\x12\x82\x01\n\rinvalid_count\x18\x02 \x01(\x05\x42]\x92\x41V2TNumber of invalid entries that were not included in the list (should be always zero)\xe2\x41\x01\x03R\x0cinvalidCount\"M\n\x1dGetNotificationChannelRequest\x12,\n\x02id\x18\x01 \x01(\tB\x1c\x92\x41\x15\x32\x13Request channel ID.\xe2\x41\x01\x03R\x02id\"\xb8\x01\n\x1eGetNotificationChannelResponse\x12\x95\x01\n\x14notification_channel\x18\x01 \x01(\x0b\x32\x38.kentik.notification_channel.v202210.NotificationChannelB(\x92\x41!2\x1f\x44\x61ta for the requested channel.\xe2\x41\x01\x03R\x13notificationChannel\"\xd3\x02\n!SearchNotificationChannelsRequest\x12\x62\n\x0cname_pattern\x18\x01 \x01(\tB?\x92\x41<2:Regular expression pattern for matching names of channels.R\x0bnamePattern\x12l\n\x05types\x18\x02 \x03(\x0e\x32\x30.kentik.notification_channel.v202210.ChannelTypeB$\x92\x41!2\x1fList of channel types to match.R\x05types\x12\\\n\x10include_disabled\x18\x03 \x01(\x08\x42\x31\x92\x41.2%Include disabled channels in results.:\x05\x66\x61lseR\x0fincludeDisabled\"\xcb\x02\n\"SearchNotificationChannelsResponse\x12\x9f\x01\n\x15notification_channels\x18\x01 \x03(\x0b\x32\x38.kentik.notification_channel.v202210.NotificationChannelB0\x92\x41)2\'List of matching notification channels.\xe2\x41\x01\x03R\x14notificationChannels\x12\x82\x01\n\rinvalid_count\x18\x02 \x01(\x05\x42]\x92\x41V2TNumber of invalid entries that were not included in the list (should be always zero)\xe2\x41\x01\x03R\x0cinvalidCount*\xea\x02\n\x0b\x43hannelType\x12\x1c\n\x18\x43HANNEL_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15\x43HANNEL_TYPE_XMATTERS\x10\x01\x12\x16\n\x12\x43HANNEL_TYPE_SLACK\x10\x02\x12\x1b\n\x17\x43HANNEL_TYPE_SERVICENOW\x10\x03\x12\x17\n\x13\x43HANNEL_TYPE_SYSLOG\x10\x04\x12\x19\n\x15\x43HANNEL_TYPE_OPSGENIE\x10\x05\x12\x1f\n\x1b\x43HANNEL_TYPE_CUSTOM_WEBHOOK\x10\x06\x12\x17\n\x13\x43HANNEL_TYPE_SPLUNK\x10\x07\x12\x18\n\x14\x43HANNEL_TYPE_MSTEAMS\x10\x08\x12\x15\n\x11\x43HANNEL_TYPE_JSON\x10\t\x12\x16\n\x12\x43HANNEL_TYPE_EMAIL\x10\n\x12\x1a\n\x16\x43HANNEL_TYPE_VICTOROPS\x10\x0b\x12\x1a\n\x16\x43HANNEL_TYPE_PAGERDUTY\x10\x0c\x32\xde\x0e\n\x1aNotificationChannelService\x12\x82\x03\n\x18ListNotificationChannels\x12\x44.kentik.notification_channel.v202210.ListNotificationChannelsRequest\x1a\x45.kentik.notification_channel.v202210.ListNotificationChannelsResponse\"\xd8\x01\x92\x41w\x12$List available notification channels\x1a\x35Returns list of all configured notification channels.*\x18ListNotificationChannels\xf2\xd7\x02\x1f\x61\x64min.notification_channel:read\x82\xd3\xe4\x93\x02\x35\x12\x33/notification_channel/v202210/notification_channels\x12\x95\x03\n\x16GetNotificationChannel\x12\x42.kentik.notification_channel.v202210.GetNotificationChannelRequest\x1a\x43.kentik.notification_channel.v202210.GetNotificationChannelResponse\"\xf1\x01\x92\x41\x8a\x01\x12,Get information about a notification channel\x1a\x42Returns information about a notification channel with specific ID.*\x16GetNotificationChannel\xf2\xd7\x02\x1f\x61\x64min.notification_channel:read\x82\xd3\xe4\x93\x02:\x12\x38/notification_channel/v202210/notification_channels/{id}\x12\xec\x07\n\x1aSearchNotificationChannels\x12\x46.kentik.notification_channel.v202210.SearchNotificationChannelsRequest\x1aG.kentik.notification_channel.v202210.SearchNotificationChannelsResponse\"\xbc\x06\x92\x41\xd0\x05\x12\x31Retrieve notification channels matching criteria.\x1a\xfe\x04Returns list of all notification channels matching request criteria. Following table lists available match criteria:\n| Request attribute | Type | Matched channel attribute | Note |\n|-------------------|------|---------------------------|------|\n| `name_pattern` | Regular expression | `name` | Empty string matches any name, otherwise the regular expression must consume all characters in the channel name |\n| `types` | List of ChannelType enum values | `type` | Empty list matches any channel type |\n\nMatch criteria are treated as a logical AND, i.e. all provider criteria must match in order for an entry to be included in the response.*\x1aSearchNotificationChannels\xf2\xd7\x02\x1f\x61\x64min.notification_channel:read\x82\xd3\xe4\x93\x02?\":/notification_channel/v202210/notification_channels/search:\x01*\x1a\x34\xca\x41\x13grpc.api.kentik.com\xea\xd7\x02\x1a\x61\x64min.notification_channelB\xb6\nZ\\github.com/kentik/api-schema/gen/go/kentik/notification_channel/v202210;notification_channel\x92\x41\xd4\t\x12\x95\x08\n\x18Notification Channel API\x12\xa8\x07# Overview\nThe Notification Channel APIs enable you to retrieve IDs for the channels in your organization\'s collection of notification channels (see [Notifications](https://kb.kentik.com/v4/Cb24.htm)). Each channel includes a channel type (e.g. email, Slack, PagerDuty, etc.) and a set of targets (recipients). Using the ID of a given channel, you can assign a set of recipients to receive notifications from Kentik alerts and synthetic tests, including those generated by the [Synthetics Monitoring APIs](https://kb.kentik.com/v0/Oa09.htm) and [BGP Monitoring APIs](https://kb.kentik.com/v0/Oa07.htm).\n\nBoth REST endpoints and gRPC RPCs are provided.\n# Limitations\nThe use of this API is currently subject to the following limitations:\n* **Read-only**: Creation, modification, and deletion of channels is not supported.\n* **No v3 channels**: No support is (or will be) provided for notification channels created in Kentik\'s v3 portal.\n\"E\n\x16Kentik API Engineering\x12+https://github.com/kentik/api-schema-public2\x07v202210*\x01\x02\x32\x10\x61pplication/json:\x10\x61pplication/jsonZD\n\x1e\n\x05\x65mail\x12\x15\x08\x02\x1a\x0fX-CH-Auth-Email \x02\n\"\n\x05token\x12\x19\x08\x02\x1a\x13X-CH-Auth-API-Token \x02\x62\x16\n\t\n\x05\x65mail\x12\x00\n\t\n\x05token\x12\x00r5\n\x16More about Kentik APIs\x12\x1bhttps://docs.kentik.com/apib\x06proto3')

_CHANNELTYPE = DESCRIPTOR.enum_types_by_name['ChannelType']
ChannelType = enum_type_wrapper.EnumTypeWrapper(_CHANNELTYPE)
CHANNEL_TYPE_UNSPECIFIED = 0
CHANNEL_TYPE_XMATTERS = 1
CHANNEL_TYPE_SLACK = 2
CHANNEL_TYPE_SERVICENOW = 3
CHANNEL_TYPE_SYSLOG = 4
CHANNEL_TYPE_OPSGENIE = 5
CHANNEL_TYPE_CUSTOM_WEBHOOK = 6
CHANNEL_TYPE_SPLUNK = 7
CHANNEL_TYPE_MSTEAMS = 8
CHANNEL_TYPE_JSON = 9
CHANNEL_TYPE_EMAIL = 10
CHANNEL_TYPE_VICTOROPS = 11
CHANNEL_TYPE_PAGERDUTY = 12


_NOTIFICATIONCHANNEL = DESCRIPTOR.message_types_by_name['NotificationChannel']
_LISTNOTIFICATIONCHANNELSREQUEST = DESCRIPTOR.message_types_by_name['ListNotificationChannelsRequest']
_LISTNOTIFICATIONCHANNELSRESPONSE = DESCRIPTOR.message_types_by_name['ListNotificationChannelsResponse']
_GETNOTIFICATIONCHANNELREQUEST = DESCRIPTOR.message_types_by_name['GetNotificationChannelRequest']
_GETNOTIFICATIONCHANNELRESPONSE = DESCRIPTOR.message_types_by_name['GetNotificationChannelResponse']
_SEARCHNOTIFICATIONCHANNELSREQUEST = DESCRIPTOR.message_types_by_name['SearchNotificationChannelsRequest']
_SEARCHNOTIFICATIONCHANNELSRESPONSE = DESCRIPTOR.message_types_by_name['SearchNotificationChannelsResponse']
NotificationChannel = _reflection.GeneratedProtocolMessageType('NotificationChannel', (_message.Message,), {
  'DESCRIPTOR' : _NOTIFICATIONCHANNEL,
  '__module__' : 'kentik.notification_channel.v202210.notification_channel_pb2'
  # @@protoc_insertion_point(class_scope:kentik.notification_channel.v202210.NotificationChannel)
  })
_sym_db.RegisterMessage(NotificationChannel)

ListNotificationChannelsRequest = _reflection.GeneratedProtocolMessageType('ListNotificationChannelsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTNOTIFICATIONCHANNELSREQUEST,
  '__module__' : 'kentik.notification_channel.v202210.notification_channel_pb2'
  # @@protoc_insertion_point(class_scope:kentik.notification_channel.v202210.ListNotificationChannelsRequest)
  })
_sym_db.RegisterMessage(ListNotificationChannelsRequest)

ListNotificationChannelsResponse = _reflection.GeneratedProtocolMessageType('ListNotificationChannelsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTNOTIFICATIONCHANNELSRESPONSE,
  '__module__' : 'kentik.notification_channel.v202210.notification_channel_pb2'
  # @@protoc_insertion_point(class_scope:kentik.notification_channel.v202210.ListNotificationChannelsResponse)
  })
_sym_db.RegisterMessage(ListNotificationChannelsResponse)

GetNotificationChannelRequest = _reflection.GeneratedProtocolMessageType('GetNotificationChannelRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETNOTIFICATIONCHANNELREQUEST,
  '__module__' : 'kentik.notification_channel.v202210.notification_channel_pb2'
  # @@protoc_insertion_point(class_scope:kentik.notification_channel.v202210.GetNotificationChannelRequest)
  })
_sym_db.RegisterMessage(GetNotificationChannelRequest)

GetNotificationChannelResponse = _reflection.GeneratedProtocolMessageType('GetNotificationChannelResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETNOTIFICATIONCHANNELRESPONSE,
  '__module__' : 'kentik.notification_channel.v202210.notification_channel_pb2'
  # @@protoc_insertion_point(class_scope:kentik.notification_channel.v202210.GetNotificationChannelResponse)
  })
_sym_db.RegisterMessage(GetNotificationChannelResponse)

SearchNotificationChannelsRequest = _reflection.GeneratedProtocolMessageType('SearchNotificationChannelsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHNOTIFICATIONCHANNELSREQUEST,
  '__module__' : 'kentik.notification_channel.v202210.notification_channel_pb2'
  # @@protoc_insertion_point(class_scope:kentik.notification_channel.v202210.SearchNotificationChannelsRequest)
  })
_sym_db.RegisterMessage(SearchNotificationChannelsRequest)

SearchNotificationChannelsResponse = _reflection.GeneratedProtocolMessageType('SearchNotificationChannelsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHNOTIFICATIONCHANNELSRESPONSE,
  '__module__' : 'kentik.notification_channel.v202210.notification_channel_pb2'
  # @@protoc_insertion_point(class_scope:kentik.notification_channel.v202210.SearchNotificationChannelsResponse)
  })
_sym_db.RegisterMessage(SearchNotificationChannelsResponse)

_NOTIFICATIONCHANNELSERVICE = DESCRIPTOR.services_by_name['NotificationChannelService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\\github.com/kentik/api-schema/gen/go/kentik/notification_channel/v202210;notification_channel\222A\324\t\022\225\010\n\030Notification Channel API\022\250\007# Overview\nThe Notification Channel APIs enable you to retrieve IDs for the channels in your organization\'s collection of notification channels (see [Notifications](https://kb.kentik.com/v4/Cb24.htm)). Each channel includes a channel type (e.g. email, Slack, PagerDuty, etc.) and a set of targets (recipients). Using the ID of a given channel, you can assign a set of recipients to receive notifications from Kentik alerts and synthetic tests, including those generated by the [Synthetics Monitoring APIs](https://kb.kentik.com/v0/Oa09.htm) and [BGP Monitoring APIs](https://kb.kentik.com/v0/Oa07.htm).\n\nBoth REST endpoints and gRPC RPCs are provided.\n# Limitations\nThe use of this API is currently subject to the following limitations:\n* **Read-only**: Creation, modification, and deletion of channels is not supported.\n* **No v3 channels**: No support is (or will be) provided for notification channels created in Kentik\'s v3 portal.\n\"E\n\026Kentik API Engineering\022+https://github.com/kentik/api-schema-public2\007v202210*\001\0022\020application/json:\020application/jsonZD\n\036\n\005email\022\025\010\002\032\017X-CH-Auth-Email \002\n\"\n\005token\022\031\010\002\032\023X-CH-Auth-API-Token \002b\026\n\t\n\005email\022\000\n\t\n\005token\022\000r5\n\026More about Kentik APIs\022\033https://docs.kentik.com/api'
  _NOTIFICATIONCHANNEL.fields_by_name['id']._options = None
  _NOTIFICATIONCHANNEL.fields_by_name['id']._serialized_options = b'\222A\"2 Unique identifier of the channel\342A\001\003'
  _NOTIFICATIONCHANNEL.fields_by_name['name']._options = None
  _NOTIFICATIONCHANNEL.fields_by_name['name']._serialized_options = b'\222A#2!User selected name of the channel\342A\001\003'
  _NOTIFICATIONCHANNEL.fields_by_name['type']._options = None
  _NOTIFICATIONCHANNEL.fields_by_name['type']._serialized_options = b'\222A\0332\031Notification channel type\342A\001\003'
  _NOTIFICATIONCHANNEL.fields_by_name['enabled']._options = None
  _NOTIFICATIONCHANNEL.fields_by_name['enabled']._serialized_options = b'\222A\0272\025Administrative status\342A\001\003'
  _NOTIFICATIONCHANNEL.fields_by_name['cdate']._options = None
  _NOTIFICATIONCHANNEL.fields_by_name['cdate']._serialized_options = b'\222A\0322\030Creation timestamp (UTC)\342A\001\003'
  _NOTIFICATIONCHANNEL.fields_by_name['edate']._options = None
  _NOTIFICATIONCHANNEL.fields_by_name['edate']._serialized_options = b'\222A#2!Last modification timestamp (UTC)\342A\001\003'
  _LISTNOTIFICATIONCHANNELSRESPONSE.fields_by_name['notification_channels']._options = None
  _LISTNOTIFICATIONCHANNELSRESPONSE.fields_by_name['notification_channels']._serialized_options = b'\222A\0372\035List of notification channels\342A\001\003'
  _LISTNOTIFICATIONCHANNELSRESPONSE.fields_by_name['invalid_count']._options = None
  _LISTNOTIFICATIONCHANNELSRESPONSE.fields_by_name['invalid_count']._serialized_options = b'\222AV2TNumber of invalid entries that were not included in the list (should be always zero)\342A\001\003'
  _GETNOTIFICATIONCHANNELREQUEST.fields_by_name['id']._options = None
  _GETNOTIFICATIONCHANNELREQUEST.fields_by_name['id']._serialized_options = b'\222A\0252\023Request channel ID.\342A\001\003'
  _GETNOTIFICATIONCHANNELRESPONSE.fields_by_name['notification_channel']._options = None
  _GETNOTIFICATIONCHANNELRESPONSE.fields_by_name['notification_channel']._serialized_options = b'\222A!2\037Data for the requested channel.\342A\001\003'
  _SEARCHNOTIFICATIONCHANNELSREQUEST.fields_by_name['name_pattern']._options = None
  _SEARCHNOTIFICATIONCHANNELSREQUEST.fields_by_name['name_pattern']._serialized_options = b'\222A<2:Regular expression pattern for matching names of channels.'
  _SEARCHNOTIFICATIONCHANNELSREQUEST.fields_by_name['types']._options = None
  _SEARCHNOTIFICATIONCHANNELSREQUEST.fields_by_name['types']._serialized_options = b'\222A!2\037List of channel types to match.'
  _SEARCHNOTIFICATIONCHANNELSREQUEST.fields_by_name['include_disabled']._options = None
  _SEARCHNOTIFICATIONCHANNELSREQUEST.fields_by_name['include_disabled']._serialized_options = b'\222A.2%Include disabled channels in results.:\005false'
  _SEARCHNOTIFICATIONCHANNELSRESPONSE.fields_by_name['notification_channels']._options = None
  _SEARCHNOTIFICATIONCHANNELSRESPONSE.fields_by_name['notification_channels']._serialized_options = b'\222A)2\'List of matching notification channels.\342A\001\003'
  _SEARCHNOTIFICATIONCHANNELSRESPONSE.fields_by_name['invalid_count']._options = None
  _SEARCHNOTIFICATIONCHANNELSRESPONSE.fields_by_name['invalid_count']._serialized_options = b'\222AV2TNumber of invalid entries that were not included in the list (should be always zero)\342A\001\003'
  _NOTIFICATIONCHANNELSERVICE._options = None
  _NOTIFICATIONCHANNELSERVICE._serialized_options = b'\312A\023grpc.api.kentik.com\352\327\002\032admin.notification_channel'
  _NOTIFICATIONCHANNELSERVICE.methods_by_name['ListNotificationChannels']._options = None
  _NOTIFICATIONCHANNELSERVICE.methods_by_name['ListNotificationChannels']._serialized_options = b'\222Aw\022$List available notification channels\0325Returns list of all configured notification channels.*\030ListNotificationChannels\362\327\002\037admin.notification_channel:read\202\323\344\223\0025\0223/notification_channel/v202210/notification_channels'
  _NOTIFICATIONCHANNELSERVICE.methods_by_name['GetNotificationChannel']._options = None
  _NOTIFICATIONCHANNELSERVICE.methods_by_name['GetNotificationChannel']._serialized_options = b'\222A\212\001\022,Get information about a notification channel\032BReturns information about a notification channel with specific ID.*\026GetNotificationChannel\362\327\002\037admin.notification_channel:read\202\323\344\223\002:\0228/notification_channel/v202210/notification_channels/{id}'
  _NOTIFICATIONCHANNELSERVICE.methods_by_name['SearchNotificationChannels']._options = None
  _NOTIFICATIONCHANNELSERVICE.methods_by_name['SearchNotificationChannels']._serialized_options = b'\222A\320\005\0221Retrieve notification channels matching criteria.\032\376\004Returns list of all notification channels matching request criteria. Following table lists available match criteria:\n| Request attribute | Type | Matched channel attribute | Note |\n|-------------------|------|---------------------------|------|\n| `name_pattern` | Regular expression | `name` | Empty string matches any name, otherwise the regular expression must consume all characters in the channel name |\n| `types` | List of ChannelType enum values | `type` | Empty list matches any channel type |\n\nMatch criteria are treated as a logical AND, i.e. all provider criteria must match in order for an entry to be included in the response.*\032SearchNotificationChannels\362\327\002\037admin.notification_channel:read\202\323\344\223\002?\":/notification_channel/v202210/notification_channels/search:\001*'
  _CHANNELTYPE._serialized_start=2107
  _CHANNELTYPE._serialized_end=2469
  _NOTIFICATIONCHANNEL._serialized_start=318
  _NOTIFICATIONCHANNEL._serialized_end=805
  _LISTNOTIFICATIONCHANNELSREQUEST._serialized_start=807
  _LISTNOTIFICATIONCHANNELSREQUEST._serialized_end=840
  _LISTNOTIFICATIONCHANNELSRESPONSE._serialized_start=843
  _LISTNOTIFICATIONCHANNELSRESPONSE._serialized_end=1162
  _GETNOTIFICATIONCHANNELREQUEST._serialized_start=1164
  _GETNOTIFICATIONCHANNELREQUEST._serialized_end=1241
  _GETNOTIFICATIONCHANNELRESPONSE._serialized_start=1244
  _GETNOTIFICATIONCHANNELRESPONSE._serialized_end=1428
  _SEARCHNOTIFICATIONCHANNELSREQUEST._serialized_start=1431
  _SEARCHNOTIFICATIONCHANNELSREQUEST._serialized_end=1770
  _SEARCHNOTIFICATIONCHANNELSRESPONSE._serialized_start=1773
  _SEARCHNOTIFICATIONCHANNELSRESPONSE._serialized_end=2104
  _NOTIFICATIONCHANNELSERVICE._serialized_start=2472
  _NOTIFICATIONCHANNELSERVICE._serialized_end=4358
# @@protoc_insertion_point(module_scope)