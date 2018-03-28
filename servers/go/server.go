package main

import (
    "log"
	"net"

	"github.com/SpeciesFileGroup/grpc_test/servers/go/unary"
	//"github.com/golang/protobuf/proto"
	context "golang.org/x/net/context"
	grpc "google.golang.org/grpc"
)

type QuestionServiceServer struct {
}

func (qss QuestionServiceServer) UnaryRequest(context.Context, *unary.QuestionRequest) (*unary.QuestionResponse, error) {
    return &unary.QuestionResponse{Reply:"33"}, nil
}

func main() {
	server := grpc.NewServer()
	var qss QuestionServiceServer
	unary.RegisterQuestionServiceServer(server, qss)
	l, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatal("Could not start server: %v", err)
	}
	server.Serve(l)
}
