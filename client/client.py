# Test gRPC Client written in Python
# The client asks each server a question, receives an answer from each server, and then concatenates their answers. 

import grpc 
import sys, time
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

def generate_stream():
	# files = [f for f in listdir(directory) if isfile(join(directory, f))]

	files = ['a','b','c']
	for file in files:
		yield q1.QuestionRequest(query = str(file))
		time.sleep(0.2)

def run_stream(directory): 
	channel = grpc.insecure_channel('localhost:50051')
	stub = qgrpc1.QuestionServiceStub(channel)
	
	answers = stub.UnaryRequest(generate_stream())

	try:
		for answer in answers:
			print(str(answer))
	except grpc._channel._Rendezvous as err:
		print(err)

if __name__ == '__main__':
	directory = sys.argv[1]
	run_stream(directory)