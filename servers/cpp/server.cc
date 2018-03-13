// A test server written in C++ 

#include <iostream>
#include <memory>
#include <string>
#include <grpc++/grpc++.h>

using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::Status;
using question::QuestionRequest;
using question::QuestionResponse;
using question::QuestionService;

class QuestionServiceImpl final : public QuestionService::Service {
	Status UnaryRequest(ServerContext* context, const QuestionRequest* request, 
			QuestionResponse* response) override {
		std::string prefix("Test response ");
		reply->set_message(prefix + request->name());
		return Status::OK;
	}
}

void RunServer() {
	// Code largely copied from grpc examples
	std::string server_address("0.0.0.0:50051");
	QuestionServiceImpl service;

	ServerBuilder builder; 
	builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
	builder.RegisterService(&service);
	std::unique_ptr<Server> server(builder.BuildAndStart());
	std::cout << "Server listening on " << server_address << std::endl; 
	server->Wait();
}

int main(int argc, char** argv) {
	RunServer();
	return 0;
}