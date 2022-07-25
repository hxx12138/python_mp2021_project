import http.server
import sys


server_address=(sys.argv[1], int(sys.argv[2]))
with http.server.ThreadingHTTPServer(server_address, http.server.SimpleHTTPRequestHandler) as httpd:
	httpd.serve_forever()