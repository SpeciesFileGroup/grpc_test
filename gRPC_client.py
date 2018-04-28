import random
import time
import os
import grpc
import my_service_pb2 as my_service_pb2
import my_service_pb2_grpc as my_service_pb2_grpc


class gRPCClient():
    def __init__(self):
        channel = grpc.insecure_channel('localhost:50051')
        self.stub = my_service_pb2_grpc.MyServiceStub(channel)

    def method1(self, filename, count):
        print('method 1')
        return self.stub.MyMethod1(my_service_pb2.MyRequest(filename=filename, count=count))

    def method2(self, filename, count):
        print('method 2')
        return self.stub.MyMethod2(my_service_pb2.MyRequest(filename=filename, count=count))

    def method3(self, req):
        print('method 3')
        return self.stub.MyMethod3(req)


def generateRequests():
    reqs = []

    for filename in os.listdir("data"):
        lines = [line.rstrip('\n\r') for line in open('data/' + filename)]
        if len(lines) == 0:
            continue
        reqs.append(my_service_pb2.MyRequest(filename=filename, filetext=lines[0], count=123))

    for req in reqs:
        yield req
        # time.sleep(random.uniform(1, 2))


def main():
    print('main')

    client = gRPCClient()


    res = client.method3(generateRequests())

    for re in res:
        print(re.filename, re.count)


if __name__ == '__main__':
    main()