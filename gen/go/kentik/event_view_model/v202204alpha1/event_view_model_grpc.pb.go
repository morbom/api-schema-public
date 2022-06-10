// Code generated by protoc-gen-go-grpc. DO NOT EDIT.

package event_view_model

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// EventViewModelServiceClient is the client API for EventViewModelService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type EventViewModelServiceClient interface {
	GetViewModel(ctx context.Context, in *GetViewModelRequest, opts ...grpc.CallOption) (*GetViewModelResponse, error)
}

type eventViewModelServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewEventViewModelServiceClient(cc grpc.ClientConnInterface) EventViewModelServiceClient {
	return &eventViewModelServiceClient{cc}
}

func (c *eventViewModelServiceClient) GetViewModel(ctx context.Context, in *GetViewModelRequest, opts ...grpc.CallOption) (*GetViewModelResponse, error) {
	out := new(GetViewModelResponse)
	err := c.cc.Invoke(ctx, "/kentik.event_view_model.v202204alpha1.EventViewModelService/GetViewModel", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// EventViewModelServiceServer is the server API for EventViewModelService service.
// All implementations should embed UnimplementedEventViewModelServiceServer
// for forward compatibility
type EventViewModelServiceServer interface {
	GetViewModel(context.Context, *GetViewModelRequest) (*GetViewModelResponse, error)
}

// UnimplementedEventViewModelServiceServer should be embedded to have forward compatible implementations.
type UnimplementedEventViewModelServiceServer struct {
}

func (UnimplementedEventViewModelServiceServer) GetViewModel(context.Context, *GetViewModelRequest) (*GetViewModelResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetViewModel not implemented")
}

// UnsafeEventViewModelServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to EventViewModelServiceServer will
// result in compilation errors.
type UnsafeEventViewModelServiceServer interface {
	mustEmbedUnimplementedEventViewModelServiceServer()
}

func RegisterEventViewModelServiceServer(s grpc.ServiceRegistrar, srv EventViewModelServiceServer) {
	s.RegisterService(&EventViewModelService_ServiceDesc, srv)
}

func _EventViewModelService_GetViewModel_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetViewModelRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EventViewModelServiceServer).GetViewModel(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/kentik.event_view_model.v202204alpha1.EventViewModelService/GetViewModel",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EventViewModelServiceServer).GetViewModel(ctx, req.(*GetViewModelRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// EventViewModelService_ServiceDesc is the grpc.ServiceDesc for EventViewModelService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var EventViewModelService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "kentik.event_view_model.v202204alpha1.EventViewModelService",
	HandlerType: (*EventViewModelServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "GetViewModel",
			Handler:    _EventViewModelService_GetViewModel_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "kentik/event_view_model/v202204alpha1/event_view_model.proto",
}
