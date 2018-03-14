var PROTO_PATH = '../../protos/question.proto';
var grpc = require('grpc');
var protoDescriptor = grpc.load(PROTO_PATH);
console.log(protoDescriptor)
var routeguide = protoDescriptor.QuestionService;

function checkResponse(query) {
	var QuestionResponse;
	QuestionResponse = {
		name : '',
		reply : '1'
	};
	return QuestionResponse;
}

// function UnaryRequest(call, callback) {
// 	callback(null, checkResponse(call.request))
// }

function UnaryRequest(call) {
	console.log(call)
	var QuestionResponse;
	QuestionResponse = {
		name : '',
		reply : '1'
	};
	console.log(QuestionResponse)
	return QuestionResponse;
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