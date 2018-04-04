// Code generated by protoc-gen-go. DO NOT EDIT.
// source: question.proto

/*
Package unary is a generated protocol buffer package.

It is generated from these files:
	question.proto

It has these top-level messages:
	QuestionRequest
	QuestionResponse
*/
package unary

import proto "github.com/golang/protobuf/proto"
import fmt "fmt"
import math "math"

import (
	context "golang.org/x/net/context"
	grpc "google.golang.org/grpc"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion2 // please upgrade the proto package

type QuestionRequest struct {
	Query string `protobuf:"bytes,1,opt,name=query" json:"query,omitempty"`
}

func (m *QuestionRequest) Reset()                    { *m = QuestionRequest{} }
func (m *QuestionRequest) String() string            { return proto.CompactTextString(m) }
func (*QuestionRequest) ProtoMessage()               {}
func (*QuestionRequest) Descriptor() ([]byte, []int) { return fileDescriptor0, []int{0} }

func (m *QuestionRequest) GetQuery() string {
	if m != nil {
		return m.Query
	}
	return ""
}

type QuestionResponse struct {
	Reply string `protobuf:"bytes,1,opt,name=reply" json:"reply,omitempty"`
}

func (m *QuestionResponse) Reset()                    { *m = QuestionResponse{} }
func (m *QuestionResponse) String() string            { return proto.CompactTextString(m) }
func (*QuestionResponse) ProtoMessage()               {}
func (*QuestionResponse) Descriptor() ([]byte, []int) { return fileDescriptor0, []int{1} }

func (m *QuestionResponse) GetReply() string {
	if m != nil {
		return m.Reply
	}
	return ""
}

func init() {
	proto.RegisterType((*QuestionRequest)(nil), "QuestionRequest")
	proto.RegisterType((*QuestionResponse)(nil), "QuestionResponse")
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConn

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion4

// Client API for QuestionService service

type QuestionServiceClient interface {
	UnaryRequest(ctx context.Context, in *QuestionRequest, opts ...grpc.CallOption) (*QuestionResponse, error)
}

type questionServiceClient struct {
	cc *grpc.ClientConn
}

func NewQuestionServiceClient(cc *grpc.ClientConn) QuestionServiceClient {
	return &questionServiceClient{cc}
}

func (c *questionServiceClient) UnaryRequest(ctx context.Context, in *QuestionRequest, opts ...grpc.CallOption) (*QuestionResponse, error) {
	out := new(QuestionResponse)
	err := grpc.Invoke(ctx, "/QuestionService/UnaryRequest", in, out, c.cc, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// Server API for QuestionService service

type QuestionServiceServer interface {
	UnaryRequest(context.Context, *QuestionRequest) (*QuestionResponse, error)
}

func RegisterQuestionServiceServer(s *grpc.Server, srv QuestionServiceServer) {
	s.RegisterService(&_QuestionService_serviceDesc, srv)
}

func _QuestionService_UnaryRequest_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(QuestionRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(QuestionServiceServer).UnaryRequest(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/QuestionService/UnaryRequest",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(QuestionServiceServer).UnaryRequest(ctx, req.(*QuestionRequest))
	}
	return interceptor(ctx, in, info, handler)
}

var _QuestionService_serviceDesc = grpc.ServiceDesc{
	ServiceName: "QuestionService",
	HandlerType: (*QuestionServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "UnaryRequest",
			Handler:    _QuestionService_UnaryRequest_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "question.proto",
}

func init() { proto.RegisterFile("question.proto", fileDescriptor0) }

var fileDescriptor0 = []byte{
	// 129 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xe2, 0xe2, 0x2b, 0x2c, 0x4d, 0x2d,
	0x2e, 0xc9, 0xcc, 0xcf, 0xd3, 0x2b, 0x28, 0xca, 0x2f, 0xc9, 0x57, 0x52, 0xe7, 0xe2, 0x0f, 0x84,
	0x8a, 0x04, 0xa5, 0x82, 0xe5, 0x84, 0x44, 0xb8, 0x58, 0x0b, 0x4b, 0x53, 0x8b, 0x2a, 0x25, 0x18,
	0x15, 0x18, 0x35, 0x38, 0x83, 0x20, 0x1c, 0x25, 0x0d, 0x2e, 0x01, 0x84, 0xc2, 0xe2, 0x82, 0xfc,
	0xbc, 0xe2, 0x54, 0x90, 0xca, 0xa2, 0xd4, 0x82, 0x1c, 0xb8, 0x4a, 0x30, 0xc7, 0xc8, 0x03, 0x61,
	0x64, 0x70, 0x6a, 0x51, 0x59, 0x66, 0x72, 0xaa, 0x90, 0x29, 0x17, 0x4f, 0x68, 0x5e, 0x62, 0x51,
	0x25, 0xcc, 0x0a, 0x01, 0x3d, 0x34, 0x4b, 0xa5, 0x04, 0xf5, 0xd0, 0x4d, 0x57, 0x62, 0x48, 0x62,
	0x03, 0xbb, 0xd1, 0x18, 0x10, 0x00, 0x00, 0xff, 0xff, 0xde, 0x3e, 0x3c, 0x1a, 0xb5, 0x00, 0x00,
	0x00,
}