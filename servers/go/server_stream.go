package main

import (
	"fmt"
	"io"
	"log"
	"net"

	streaming "github.com/SpeciesFileGroup/grpc_test/servers/go/stream"
	//"github.com/golang/protobuf/proto"
	grpc "google.golang.org/grpc"
)

type StreamingServer struct {
}

func (ss StreamingServer) UnaryRequest(stream streaming.QuestionService_UnaryRequestServer) error {
	for {
		in, err := stream.Recv()
		if err == io.EOF {
			return nil
		}
		if err != nil {
			return err
		}
		resp := &streaming.QuestionResponse{countWords(in.Query)}
		if err := stream.Send(resp); err != nil {
			return err
		}
	}
}

func countWords(str string) string {
	return fmt.Sprintf("%d", len(str))
}

func main() {
	server := grpc.NewServer()
	var ss StreamingServer
	streaming.RegisterQuestionServiceServer(server, ss)
	l, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatal("Could not start server: %v", err)
	}
	server.Serve(l)
}
