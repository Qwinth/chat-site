from http.server import ThreadingHTTPServer, CGIHTTPRequestHandler
import pause                #підключення бібліотеки "pause"
import socket
import os
PORT = 80
IP = ''
c = ('')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("google.com",80))
IP = (s.getsockname()[0])
s.close()
settings_mode = ('none')#режим налаштування
check = os.path.isfile('server.properties')

if check == True:
    open_file = open('server.properties','r')
    read = open_file.read()
    if read == 'settings_mode = true':
        settings_mode = ('true')
    else:
        settings_mode = ('false')
else:
    settings_mode = ('false')
if settings_mode == 'true':   #перевірка якщо режим надаштування = true
    c=input('Введіть режим: ') #ввід данних у змінну "с" settings_mode-це теж змінна

if settings_mode == 'false':
    print('Server started')
    print('IP:', IP)
    print('PORT:', PORT)
    print('----------------------------------------')
    print('HTTP Requests')
    server_address=(IP,PORT)
    httpd = ThreadingHTTPServer(server_address, CGIHTTPRequestHandler)
    httpd.serve_forever()

if c == 'a':                                       #якщо змінна "c" = a
    print('Режим змінений на AUTOMATIC')
    print('Server started')
    print('IP:', IP)
    print('PORT:', PORT)
    print('----------------------------------------')
    print('HTTP Requests')
    server_address=(IP,PORT)
    httpd = ThreadingHTTPServer(server_address, CGIHTTPRequestHandler)
    httpd.serve_forever()
if c == 'l':
    print('Режим змінений на lOCAL')
    print('Server started')
    print('IP:', IP)
    print('PORT:', PORT)
    print('----------------------------------------')
    print('HTTP Requests')
    server_address=('localhost',PORT)
    httpd = ThreadingHTTPServer(server_address, CGIHTTPRequestHandler)
    httpd.serve_forever()

if c == 'u':
    print('Режим змінений на USER')
    IP=input('Введіть IP: ')
    print('IP успішно змінено')
    print('Server started')
    print('IP:', IP)
    print('PORT:', PORT)
    print('----------------------------------------')
    print('HTTP Requests')
    server_address=(IP,PORT)
    httpd = ThreadingHTTPServer(server_address, CGIHTTPRequestHandler)
    httpd.serve_forever()
else:                                           #інакше
    print('Немає такого режиму')
    pause.milliseconds(1000)    #пауза перед закриттям програми (можна міняти цифри)
    
