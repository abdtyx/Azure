# coding=utf-8
# server.py

import socket
import json

# Define the type of socket, network communication, TCP
ListenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Binding IP and port of socket
ListenSocket.bind(('127.0.0.1', 5701))
# Start TCP listen
ListenSocket.listen(100)


# Define a http header
HttpResponseHeader = '''HTTP/1.1 200 OK
Content-Type: text/html
'''


# Turn to json to locate valid information
def json_to_info(msg):
    for i in range(len(msg)):
        if msg[i]=="{" and msg[-1]=="}":
            # Decode JSON information and return data type of Python field
            return json.loads(msg[i:])
    return None

# Execute circulately and return json
def rev_msg():
    # receive TCP connection and return new socket and IP address
    conn, addr = ListenSocket.accept()
    # receive data and decode(json in form of string)
    data = conn.recv(1024).decode(encoding='utf-8')


    # json to dict
    rev_dict=json_to_info(data)

    conn.sendall((HttpResponseHeader).encode(encoding='utf-8'))
    conn.close()
    return rev_dict
