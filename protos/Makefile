all: client server

client:
	@echo "Generating Python client files"
	python -m grpc_tools.protoc -I. --python_out=../client --grpc_python_out=../client question.proto
	python -m grpc_tools.protoc -I. --python_out=../client --grpc_python_out=../client questionstream.proto
	@echo ""

server:
	@echo "Generating Node server files"
	#Node file generation goes here
	@echo ""
	#Similarly for other server languages
