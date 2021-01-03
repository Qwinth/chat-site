#!/usr/bin/env python3
import os
import cgi
form = cgi.FieldStorage()
nick = str(form.getfirst("nick"))
dir_path = os.getcwd() + '/' + nick
os.mkdir(dir_path)
path = dir_path + '\\messages.txt'
file_messages = open(path,'w')
file_messages.close()
html_code = '''
<head>
<meta http-equiv="refresh" content="1;URL=http://82.193.114.39:7000" />
</head>'''
print(html_code)
