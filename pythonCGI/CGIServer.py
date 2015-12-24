import BaseHTTPServer
import CGIHTTPServer
# BaseHTTPServer provides a simple web server and CGIHTTPServer provides us with a request handler
import cgitb
cgitb.enable()  ## This line enables CGI error reporting
 
# create a server and a request handler
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler

server_address = ("localhost", 8000)
handler.cgi_directories = ["/cgi-bin"]
 
httpd = server(server_address, handler)
print "Start CGI server on %s:%d" %server_address
httpd.serve_forever()
