var PROTO_PATH = '../../protos/question.proto';
var grpc = require('grpc');
var protoDescriptor = grpc.load(PROTO_PATH);
var routeguide = protoDescriptor.QuestionService;

function checkResponse(query) {
	var QuestionResponse;
	QuestionResponse = {
		reply : '1'
	};
	return QuestionResponse;
}

function UnaryRequest(call, callback) {
	callback(null, checkResponse(call.request))
}

function getServer() {
	var server = new grpc.Server();
  	server.addProtoService(routeguide.service, {
    	UnaryRequest : UnaryRequest
  	});
  return server;
}

var routeServer = getServer();
routeServer.bind('0.0.0.0:50051', grpc.ServerCredentials.createInsecure());
routeServer.start();