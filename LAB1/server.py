# create an INET, STREAMing socket
import socket
from urllib.parse import urlparse


from flask import request

host , port = '0.0.0.0' , 80


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind the socket to a public host, and a well-known port
serversocket.bind((host, port))
# become a server socket
serversocket.listen(1)

print('servidor en el puerto', port)

while True: 
    connection, address = serversocket.accept()
    request = connection.recv(1024).decode('utf-8')
    print(request)

    string_list = request.split(' ')
    method = string_list[0]
    requesting_file = string_list[1]
    o = urlparse(requesting_file)
    print("Scheme: ", o.scheme)
    print("Netloc: ", o.netloc)
    print("Path: ", o.path)
    print("Params: ", o.params)
    print("Query: ", o.query)
    print("Fragment: ", o.fragment)
    print('Client request', requesting_file)

    myfile = requesting_file.split('?')[0]
    myfile = myfile.lstrip('/')

    if(myfile == ''):
        myfile = 'index.html'

    try:
        file = open(myfile , 'rb')
        response = file.read()
        file.close()

        header = 'HTTP/1.1 200 OK\n'

        if(myfile.endswith('.jpg')):
            mimetype = 'image/jpg'
        elif(myfile.endswith('.css')):
            mimetype = 'text/css'
        elif(myfile.endswith('.pdf')):
            mimetype = 'application/pdf'
        else:
            mimetype = 'text/html'
        header += 'Conten-Type: ' + str(mimetype) + '\n\n'

    except Exception as e:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body>Error 404: Archivo no encontrado</body><//html>'.encode('utf-8')

    final_response = header.encode('utf-8')
    final_response += response
    #print(response.decode('utf-8'))
    connection.send(final_response)
    connection.close()