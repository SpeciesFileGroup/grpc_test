CS 492 GRPC Test code

Requires an installation of grpc and protoc. Installation instructions will depend Operating System and which grpc language you are using. See the grpc guides. 

To run the project:
* Navigate to the `protos` directory and run `make -B all`
* Run the client as `python3 client/client.py <directory where /bhl/ocr data is stored>`
* To run the node server, run '`node servers/nodejs/server_stream.js`

Current sample output: <br>
`{      '/home/ankit/bhlindex/testdata/bhl/ocr/bhl1/00703camxa2200193Iix4500/naturalhistoryof00mill/naturalhistoryof00mill_0001.txt': '64',    '/home/ankit/bhlindex/testdata/bhl/ocr/bhl1/00703camxa2200193Iix4500/naturalhistoryof00mill/naturalhistoryof00mill_0002.txt': '204', '/home/ankit/bhlindex/testdata/bhl/ocr/bhl1/00703camxa2200193Iix4500/naturalhistoryof00mill/naturalhistoryof00mill_0003.txt': '0', '/home/ankit/bhlindex/testdata/bhl/ocr/bhl1/00703camxa2200193Iix4500/naturalhistoryof00mill/naturalhistoryof00mill_0004.txt': '0', '/home/ankit/bhlindex/testdata/bhl/ocr/bhl1/00703camxa2200193Iix4500/naturalhistoryof00mill/naturalhistoryof00mill_0005.txt': '0', '/home/ankit/bhlindex/testdata/bhl/ocr/bhl1/00703camxa2200193Iix4500/naturalhistoryof00mill/naturalhistoryof00mill_0006.txt': '0', '/home/ankit/bhlindex/testdata/bhl/ocr/bhl1/00703camxa2200193Iix4500/naturalhistoryof00mill/naturalhistoryof00mill_0007.txt': '0', '/home/ankit/bhlindex/testdata/bhl/ocr/bhl1/00703camxa2200193Iix4500/naturalhistoryof00mill/naturalhistoryof00mill_0008.txt': '49', '/home/ankit/bhlindex/testdata/bhl/ocr/bhl1/00703camxa2200193Iix4500/naturalhistoryof00mill/naturalhistoryof00mill_0009.txt': '985',...
}
`
