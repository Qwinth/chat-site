from http.server import ThreadingHTTPServer, CGIHTTPRequestHandler
import time
import socket
import os
PORT = 80
IP = ''
c = ('')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("google.com",80))
IP = (s.getsockname()[0])
s.close()
settings_mode = ('none')
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
if settings_mode == 'true':
    c=input('Введіть режим: ')

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
else:
    print('Немає такого режиму')
    time.sleep(1)
    
