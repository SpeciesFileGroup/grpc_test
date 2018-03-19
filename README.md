CS 492 GRPC Test code

Requires an installation of grpc and protoc. Installation instructions will depend Operating System and which grpc language you are using. See the grpc guides. 

To compile the .proto files: 
Navigate to grpc_test/protos and run: 

python -m grpc_tools.protoc -I. --python_out=../client --grpc_python_out=../client question.proto

General instructions for the protoc compiler can be found here: 

https://developers.google.com/protocol-buffers/docs/proto3#generating

The grpc installation also adds specific grpc options, which take the form --grpc_(language)_out=DST_DIR
