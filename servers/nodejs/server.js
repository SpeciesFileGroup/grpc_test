var PROTO_PATH = '../../protos/question.proto';
var grpc = require('grpc');
var protoDescriptor = grpc.load(PROTO_PATH);
var routeguide = protoDescriptor.routeguide;

function checkResponse(query) {
	var QuestionResponse;
	feature = {
		name : '',
		reply : '1'
	};
	return feature;
}

function UnaryRequest(call, callback) {
	callback(null, checkResponse(call.request))
}

function getServer() {
	var server = new grpc.Server();
  	server.addProtoService(routeguide.RouteGuide.service, {
    	UnaryRequest : UnaryRequest
  	});
  return server;
}

function main() {
	var routeServer = getServer();
	routeServer.bind('0.0.0.0:50051', grpc.ServerCredentials.createInsecure());
	routeServer.start();
}