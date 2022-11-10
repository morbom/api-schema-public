# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: kentik/user/v202211/user.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.protobuf.timestamp_pb2
import protoc_gen_openapiv2.options.annotations_pb2
import kentik.core.v202012alpha1.annotations_pb2
import kentik.user.v202211.user_pb2


class UserServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ListUsers(self, stream: 'grpclib.server.Stream[kentik.user.v202211.user_pb2.ListUsersRequest, kentik.user.v202211.user_pb2.ListUsersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetUser(self, stream: 'grpclib.server.Stream[kentik.user.v202211.user_pb2.GetUserRequest, kentik.user.v202211.user_pb2.GetUserResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateUser(self, stream: 'grpclib.server.Stream[kentik.user.v202211.user_pb2.CreateUserRequest, kentik.user.v202211.user_pb2.CreateUserResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateUser(self, stream: 'grpclib.server.Stream[kentik.user.v202211.user_pb2.UpdateUserRequest, kentik.user.v202211.user_pb2.UpdateUserResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteUser(self, stream: 'grpclib.server.Stream[kentik.user.v202211.user_pb2.DeleteUserRequest, kentik.user.v202211.user_pb2.DeleteUserResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ResetApiToken(self, stream: 'grpclib.server.Stream[kentik.user.v202211.user_pb2.ResetApiTokenRequest, kentik.user.v202211.user_pb2.ResetApiTokenResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ResetActiveSessions(self, stream: 'grpclib.server.Stream[kentik.user.v202211.user_pb2.ResetActiveSessionsRequest, kentik.user.v202211.user_pb2.ResetActiveSessionsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/kentik.user.v202211.UserService/ListUsers': grpclib.const.Handler(
                self.ListUsers,
                grpclib.const.Cardinality.UNARY_UNARY,
                kentik.user.v202211.user_pb2.ListUsersRequest,
                kentik.user.v202211.user_pb2.ListUsersResponse,
            ),
            '/kentik.user.v202211.UserService/GetUser': grpclib.const.Handler(
                self.GetUser,
                grpclib.const.Cardinality.UNARY_UNARY,
                kentik.user.v202211.user_pb2.GetUserRequest,
                kentik.user.v202211.user_pb2.GetUserResponse,
            ),
            '/kentik.user.v202211.UserService/CreateUser': grpclib.const.Handler(
                self.CreateUser,
                grpclib.const.Cardinality.UNARY_UNARY,
                kentik.user.v202211.user_pb2.CreateUserRequest,
                kentik.user.v202211.user_pb2.CreateUserResponse,
            ),
            '/kentik.user.v202211.UserService/UpdateUser': grpclib.const.Handler(
                self.UpdateUser,
                grpclib.const.Cardinality.UNARY_UNARY,
                kentik.user.v202211.user_pb2.UpdateUserRequest,
                kentik.user.v202211.user_pb2.UpdateUserResponse,
            ),
            '/kentik.user.v202211.UserService/DeleteUser': grpclib.const.Handler(
                self.DeleteUser,
                grpclib.const.Cardinality.UNARY_UNARY,
                kentik.user.v202211.user_pb2.DeleteUserRequest,
                kentik.user.v202211.user_pb2.DeleteUserResponse,
            ),
            '/kentik.user.v202211.UserService/ResetApiToken': grpclib.const.Handler(
                self.ResetApiToken,
                grpclib.const.Cardinality.UNARY_UNARY,
                kentik.user.v202211.user_pb2.ResetApiTokenRequest,
                kentik.user.v202211.user_pb2.ResetApiTokenResponse,
            ),
            '/kentik.user.v202211.UserService/ResetActiveSessions': grpclib.const.Handler(
                self.ResetActiveSessions,
                grpclib.const.Cardinality.UNARY_UNARY,
                kentik.user.v202211.user_pb2.ResetActiveSessionsRequest,
                kentik.user.v202211.user_pb2.ResetActiveSessionsResponse,
            ),
        }


class UserServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListUsers = grpclib.client.UnaryUnaryMethod(
            channel,
            '/kentik.user.v202211.UserService/ListUsers',
            kentik.user.v202211.user_pb2.ListUsersRequest,
            kentik.user.v202211.user_pb2.ListUsersResponse,
        )
        self.GetUser = grpclib.client.UnaryUnaryMethod(
            channel,
            '/kentik.user.v202211.UserService/GetUser',
            kentik.user.v202211.user_pb2.GetUserRequest,
            kentik.user.v202211.user_pb2.GetUserResponse,
        )
        self.CreateUser = grpclib.client.UnaryUnaryMethod(
            channel,
            '/kentik.user.v202211.UserService/CreateUser',
            kentik.user.v202211.user_pb2.CreateUserRequest,
            kentik.user.v202211.user_pb2.CreateUserResponse,
        )
        self.UpdateUser = grpclib.client.UnaryUnaryMethod(
            channel,
            '/kentik.user.v202211.UserService/UpdateUser',
            kentik.user.v202211.user_pb2.UpdateUserRequest,
            kentik.user.v202211.user_pb2.UpdateUserResponse,
        )
        self.DeleteUser = grpclib.client.UnaryUnaryMethod(
            channel,
            '/kentik.user.v202211.UserService/DeleteUser',
            kentik.user.v202211.user_pb2.DeleteUserRequest,
            kentik.user.v202211.user_pb2.DeleteUserResponse,
        )
        self.ResetApiToken = grpclib.client.UnaryUnaryMethod(
            channel,
            '/kentik.user.v202211.UserService/ResetApiToken',
            kentik.user.v202211.user_pb2.ResetApiTokenRequest,
            kentik.user.v202211.user_pb2.ResetApiTokenResponse,
        )
        self.ResetActiveSessions = grpclib.client.UnaryUnaryMethod(
            channel,
            '/kentik.user.v202211.UserService/ResetActiveSessions',
            kentik.user.v202211.user_pb2.ResetActiveSessionsRequest,
            kentik.user.v202211.user_pb2.ResetActiveSessionsResponse,
        )
