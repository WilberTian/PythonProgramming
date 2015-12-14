from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

html = """
<html>
<body>
   <form method="get" action="/">
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
</html>"""

def application(environ, start_response):
    print "QUERY_STRING: %s" %environ['QUERY_STRING']
    print "REQUEST_METHOD: %s" %environ['REQUEST_METHOD']

    # Returns a dictionary containing lists as values.
    d = parse_qs(environ['QUERY_STRING'])
    
    # In this idiom you must issue a list containing a default value.
    name = d.get('name', [''])[0] # Returns the first name value.
    hobbies = d.get('hobbies', []) # Returns a list of hobbies.
    
    # Always escape user input to avoid script injection
    name = escape(name)
    hobbies = [escape(hobby) for hobby in hobbies]
    
    response_body = html % (name or 'Empty',
                ', '.join(hobbies or ['No Hobbies']))
    
    status = '200 OK'
    
    # Now content type is text/html
    response_headers = [('Content-Type', 'text/html'),
                ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    
    return [response_body]

httpd = make_server('localhost', 8080, application)
# Now it is serve_forever() in instead of handle_request().
# In Windows you can kill it in the Task Manager (python.exe).
# In Linux a Ctrl-C will do it.
httpd.serve_forever()