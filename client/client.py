# Test gRPC Client written in Python
# The client asks each server a question, receives an answer from each server, and then concatenates their answers. 

import grpc 
import question_pb2 as q
import question_pb2_grpc as qgrpc

def run(): 
	channel = grpc.insecure_channel('localhost:50051')
	stub = qgrpc.QuestionServiceStub(channel)
	response = stub.UnaryRequest(q.QuestionRequest(query="Hello?"))
	if not response:
		print("Server connection has failed")
	else:
		print("Server response received: " + str(response))

if __name__ == '__main__':
	run()