# Test gRPC Client written in Python
# The client asks each server a question, receives an answer from each server, and then concatenates their answers. 

import grpc 
import sys, time
import os, pprint
from collections import defaultdict
from os import listdir
from os.path import isfile, join
import question_pb2 as q
import question_pb2_grpc as qgrpc
import questionstream_pb2 as q1
import questionstream_pb2_grpc as qgrpc1

pp = pprint.PrettyPrinter(indent=4)

def run(): 
	channel = grpc.insecure_channel('localhost:50051')
	stub = qgrpc.QuestionServiceStub(channel)
	response = stub.UnaryRequest(q.QuestionRequest(query="Hello?"))
	if not response:
		print("Server connection has failed")
	else:
		print("Server response received: " + str(response))

def generate_stream(files):
	for file in files:
		with open(file, 'r') as my_file:
			file_data = my_file.read().replace('\n','')
			yield q1.QuestionRequest(query = file_data)

#Creates a stream of requests, should be able to use this with any server
# Due to some weird issues with node, I'm not able to generate the protobuf code, so as a workaround, the answer you get back and the message you send have the same field nanmed 'query'. Hacky, but i'm looking at how to fix it
def run_stream(files): 
	channel = grpc.insecure_channel('localhost:50051')
	stub = qgrpc1.QuestionServiceStub(channel)

	answers = stub.UnaryRequest(generate_stream(files))
	word_count = defaultdict(int)

	i = 0
	try:
		for answer in answers:
			word_count[files[i]] = answer.query
			i += 1	
	except grpc._channel._Rendezvous as err:
		print(err)

	pp.pprint(word_count)

if __name__ == '__main__':
	directory = sys.argv[1]
	directory = os.path.abspath(directory)

	files = []
	for root, directories, filenames in os.walk(directory):
		for filename in filenames:
			files.append(os.path.join(root,filename))

	run_stream(files)