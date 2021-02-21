#!/usr/bin/env python3
import cgi
import os
form = cgi.FieldStorage()
nick = str(form.getfirst("nick"))
path = os.getcwd() + '/' + nick + '/messages.txt'
file_messages = open(path,'r')
messages_read = file_messages.read()
file_messages.close()
print("Content-type: text/html")
print()
print(messages_read)
html_code = '''
<body>
	<form name="test" method="post" action="chat.py">
		<input type="text" name="nick" placeholder="input chat">
		<input type="hidden" name="my_nick" placeholder="input your nick" value=''' + nick + '''>
		<p><input type="submit" value="choise">
	</form>
	
</body>'''
print(html_code)
