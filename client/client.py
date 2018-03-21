# Test gRPC Client written in Python
# The client asks each server a question, receives an answer from each server, and then concatenates their answers. 

import grpc 
import question_pb2 as q
import question_pb2_grpc as qgrpc
import questionstream_pb2 as q1
import questionstream_pb2_grpc as qgrpc1

def run(): 
	channel = grpc.insecure_channel('localhost:50051')
	stub = qgrpc.QuestionServiceStub(channel)
	response = stub.UnaryRequest(q.QuestionRequest(query="Hello?"))
	if not response:
		print("Server connection has failed")
	else:
		print("Server response received: " + str(response))

def run_stream(): 
	channel = grpc.insecure_channel('localhost:50051')
	stub = qgrpc1.QuestionServiceStub(channel)
	
	question = q1.QuestionRequest(query="Hello?")
	answers = stub.UnaryRequest(question)
	print(answers)

	for answer in answers:
		print("Server response received: " + str(answer))

if __name__ == '__main__':
	run_stream()