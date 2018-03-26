from concurrent import futures
import time
import grpc 
import question_pb2
import question_pb2_grpc
import questionstream_pb2
import questionstream_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class QuestionService(question_pb2_grpc.QuestionServiceServicer):

    def UnaryRequest(self, request, context):
        return question_pb2.QuestionResponse(message='Hello, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    question_pb2_grpc.add_QuestionServiceServicer_to_server(QuestionService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
