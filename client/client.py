# Test gRPC Client written in Python
# The client asks each server a question, receives an answer from each server, and then concatenates their answers. 

import grpc 
import question_pb2.py as q
import question_pb2_grpc.py as qgrpc

def run(): 
	channel = grpc.insecure_channel('localhost:50051')
	stub = qgrpc.QuestionServiceStub(cannel)
	response = stub.UnaryRequest(q.UnaryRequest(query="Hello?"))
	print("Server response received: " + response.message)

if __name__ == '__main__':
	run()