from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

html = """
<html>
<body>
   <form method="post" action="parsing_post.wsgi">
      <p>
         Name: <input type="text" name="name">
         </p>
      <p>
         Hobbies:
         <input name="hobbies" type="checkbox" value="running"> running
         <input name="hobbies" type="checkbox" value="swimming"> swimming
         <input name="hobbies" type="checkbox" value="reading"> reading
         </p>
      <p>
         <input type="submit" value="Submit">
         </p>
      </form>
   <p>
      Name: %s<br>
      Hobbies: %s
      </p>
   </body>
</html>
"""

def application(environ, start_response):
    # the environment variable CONTENT_LENGTH may be empty or missing
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0
        
    # When the method is POST the query string will be sent
    # in the HTTP request body which is passed by the WSGI server
    # in the file like wsgi.input environment variable.
    request_body = environ['wsgi.input'].read(request_body_size)
    d = parse_qs(request_body)
    
    print "wsgi.input %s" %environ['wsgi.input']
    print "request_body_size %s" %environ.get('CONTENT_LENGTH', 0)
    print "request_body %s" %request_body
    
    
    name = d.get('name', [''])[0] # Returns the first name value.
    hobbies = d.get('hobbies', []) # Returns a list of hobbies.
    
    # Always escape user input to avoid script injection
    name = escape(name)
    hobbies = [escape(hobby) for hobby in hobbies]
    
    response_body = html % (name or 'Empty',
                ', '.join(hobbies or ['No Hobbies']))
    
    status = '200 OK'
    
    response_headers = [('Content-Type', 'text/html'),
                ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    
    return [response_body]

httpd = make_server('localhost', 8080, application)
httpd.serve_forever()