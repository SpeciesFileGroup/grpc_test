var PROTO_PATH = '../../protos/questionstream.proto';
var grpc = require('grpc');
var protoDescriptor = grpc.load(PROTO_PATH);
var routeguide = protoDescriptor.QuestionService;

function UnaryRequest(call) {
   console.log(call)
   call.on('data', function(file) {
      var QuestionResponse = {
        'reply': file
      };
      call.write(QuestionResponse)
   });
   call.on('end', function() {
      call.end();
   }); 
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