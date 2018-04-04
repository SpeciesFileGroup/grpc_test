CS 492 GRPC Test code

Requires an installation of grpc and protoc. Installation instructions will depend Operating System and which grpc language you are using. See the grpc guides. 

To run the project:
* Navigate to the `protos` directory and run `make -B all`
* Run the client as `python3 client/client.py <directory where /bhl/ocr data is stored>`
* To run the node server, run '`node servers/nodejs/server_stream.js`
