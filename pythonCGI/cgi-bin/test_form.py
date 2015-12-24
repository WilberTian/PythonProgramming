import cgi
 
form = cgi.FieldStorage()
comments = form["comments"].value
 
print "Content-type: text/html"

print """
The form input is below...<br/>"""
print comments