import time
from concurrent import futures

import grpc
import my_module
import my_service_pb2 as my_service_pb2
import my_service_pb2_grpc as my_service_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class gRPCServer(my_service_pb2_grpc.MyServiceServicer):
    def __init__(self):
        print('initialization')

    def MyMethod1(self, request, context):
        print(request.filename)
        print(request.count)
        return my_service_pb2.MyResponse(filename=request.filename, count=123)

    def MyMethod2(self, request, context):
        print(request.filename)
        print(request.count * 12)
        return my_service_pb2.MyResponse(filename=request.filename, count=1234)

    def MyMethod3(self, request_iterator, context):
        for req in request_iterator:
            # print(req)
            total_count = my_module.wordcount(req.filetext)
            yield my_service_pb2.MyResponse(filename=req.filename, filetext=req.filetext, count=total_count)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    my_service_pb2_grpc.add_MyServiceServicer_to_server(
        gRPCServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()