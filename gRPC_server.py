import time
from concurrent import futures
import grpc
import my_module
import my_service_pb2 as my_service_pb2
import my_service_pb2_grpc as my_service_pb2_grpc
import psycopg2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

conn = None
number_of_pages = 1

class gRPCServer(my_service_pb2_grpc.MyServiceServicer):
    def __init__(self):
        print('initialization')

    def MyMethod1(self, request, context):
        print(request.filename)
        print(request.count)
        return my_service_pb2.MyResponse(filename=request.filename, count=123)

    def MyMethod2(self, request, context):
        cur = conn.cursor()
        cur.execute("select * from dev_page_name_counts")
        rows = cur.fetchall()
        global number_of_pages
        number_of_pages = request.number_of_pages
        return my_service_pb2.InitialResponse(count=len(rows))

    def MyMethod3(self, request_iterator, context):
        for req in request_iterator:
            # print(req)
            total_count = my_module.wordcount(req.filetext)
            yield my_service_pb2.MyResponse(filename=req.filename, filetext=req.filetext, count=total_count)

    def MyMethod4(self, request_iterator, context):
        cur = conn.cursor()
        for req in request_iterator:
            offset = req.offset
            cur.execute("select * from dev_page_name_counts limit %s offset %s", (number_of_pages, offset))
            rows = cur.fetchall()
            page_names = []
            page_count = []
            for i in rows:
                page_names.append(i[0])
                page_count.append(i[1])
            yield my_service_pb2.QueryResponse(page_names=page_names, page_count=page_count)
        

def serve():
    print("hello world")
    try:
        global conn
        conn = psycopg2.connect(database="bhlindex", user="bhl", password="grpc2BHL", host="172.22.247.14", port ="5432")
    except:
        print("Unable to connect to db")

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