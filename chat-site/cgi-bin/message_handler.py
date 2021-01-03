#!/usr/bin/env python3
import cgi
import os
form = cgi.FieldStorage()
from_mes = str(form.getfirst("from"))
to = str(form.getfirst("to"))
message = str(form.getfirst("message"))
name = from_mes + '-' + to
name2 = to + '-' + from_mes
path = os.getcwd() + '\\' + from_mes + '\\' + name + '.txt'
path2 = os.getcwd() + '\\' + to + '\\' + name2 + '.txt'
check_file = os.path.exists(path)
if check_file == True:
    file = open(path,'a')
    enter = '''
'''
    file.write('(' + from_mes + ')' + message + enter)
    file.close()

check_file = os.path.exists(path2)
if check_file == True:
    file = open(path2,'a')
    file.write('(' + from_mes + ')' + message + enter)
    file.close()
print("Content-type: text/html")
print()
html_form_code = '''
<body>
	<form name="test" method="post" action="chat.py">
		<input type="hidden" name="nick" value=''' + to + '''>
		<input type="hidden" name="my_nick" value=''' + from_mes + '''>
		<p><input type="submit" value="back">
	</form>
</body>'''
print(html_form_code)
file.close()
