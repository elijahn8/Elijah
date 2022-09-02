# server.py.......................................................
import socket
"""
this is the code for the tcp server in the web
"""
#setting the requirements for the tcp connections 
ip="127.0.0.1"
port=2000
address=(ip,port)
#creating the  tcp function object
server=socket.socket()
server.bind(address)
server.listen(2)
while True:
     addr, msg= server.accept()
     print("connected to this -> " , addr)
     print("elijah sent you this msg",msg)
server.close()

