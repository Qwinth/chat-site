import cgi
import os
form = cgi.FieldStorage()
my_nick = str(form.getfirst("my_nick"))
nick = str(form.getfirst("nick"))
html_form_code = '''
<body>
	<form name="test" method="post" action="message_handler.py">
		<input type="hidden" name="to" value=''' + nick + '''>
		<input type="hidden" name="from" value=''' + my_nick + '''>
                <input type="text" name="message" placeholder="message">
		<p><input type="submit" value="submit">
	</form>
	<form name="test" method="post" action="menu.py">
	        <input type="hidden" name="nick" value=''' + my_nick + '''
                <p><input type="submit" value="menu">
        </form>
	
</body>'''
check_file = os.path.exists(os.getcwd() + '\\' + my_nick + '\\' + 'messages.txt')
if check_file == True:
    check_file = os.path.exists(os.getcwd() + '\\' + my_nick + '\\' + 'messages.txt')
    if check_file == True:
        check_file = os.path.exists(os.getcwd() + '\\' + my_nick + '\\' + nick + '.txt')
        if not check_file == True:
            file = open(os.getcwd() + '\\' + my_nick + '\\' + 'messages.txt','a')
            file.write(nick + ', ')
            file.close
            file = open(os.getcwd() + '\\' + my_nick + '\\' + nick + '.txt','w')
            file.close
    check_file = os.path.exists(os.getcwd() + '\\' + my_nick + '\\' + 'messages.txt')
    if not check_file == True:
        file_messages = open(os.getcwd() + '\\' + my_nick + '\\' + 'messages.txt','w')
        file_messages.close()
    name1 = my_nick + '-' + nick + '.txt'
    name2 = nick + '-' + my_nick + '.txt'
    check_file = os.path.exists(os.getcwd() + '\\' + my_nick + '\\' + name1)
    if not check_file == True:
        file_message = open(os.getcwd() + '\\' + my_nick + '\\' + name1,'w')
        file_message.close()
    check_file = os.path.exists(os.getcwd() + '\\' + nick + '\\' + name2)
    if not check_file == True:
        file_message = open(os.getcwd() + '\\' + nick + '\\' + name2,'w')
        file_message.close
    check_file = os.path.exists(os.getcwd() + '\\' + my_nick + '\\' + name1)
    if check_file == True:
        out_messages = open(os.getcwd() + '\\' + my_nick + '\\' + name1,'r')
    mess_out = out_messages.readline()
    print("Content-type: text/html")
    print()
    while True:
        print(mess_out + '<br>')
        mess_out = out_messages.readline()
        if not mess_out:
            break
    print(html_form_code)
