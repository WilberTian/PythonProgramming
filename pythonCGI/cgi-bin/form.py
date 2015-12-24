print "Content-type: text/html"

print """
<form method="post" action="test_form.py">
<textarea name="comments" cols="40" rows="5">
Enter comments here...
</textarea>
<br/>
<input type="submit" value="Submit">
</form>"""