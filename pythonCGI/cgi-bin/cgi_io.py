import cgi
 
form = cgi.FieldStorage()
name = form["name"].value
age = form["age"].value

print "Content-type: text/html"

print """
<html><head><title>Test get value</title></head><body>
Hello, %s is %s years old
</body></html>""" %(name, age)