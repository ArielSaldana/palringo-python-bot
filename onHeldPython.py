
import io
import sys
import socket
import threading
import time
import datetime
import re ##regex 
import urllib
import json

def open_socket(counter):
  sockets = []
  for i in range(counter):
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     server_address = ('192.168.200.128',12345);
     s.connect(server_address)
     sockets.append(s)
  time.sleep(20)

def main():

    #open_socket(5000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #server_address = ('24.186.25.10',12345);
    server_address = ('192.168.200.128',12345);
    #server_address = ('80.69.129.11', 80);
    
    print('Attempting to connect to the server')
    try:
        sock.connect(server_address)
    except:
        raise Exception('Error Connecting to the server')

    print('Connected succesfully')
    try:
        amount_received = 0
        #sock.send('meow'.encode('utf-8'))
        sock.sendall("{\"packet\":\"login\",\"headers\":{ \"user\":\"medo\",\"pass\":\"meow\",\"device\":\"\",\"version\":\"\"}}".encode('utf-8'))
        while True:
            data = sock.recv(65535)

            if len(data) <= 0:
                print(len(data.decode("utf-8")))
                break
            
            print(data)

            if data.decode("utf-8") == "P\r\n":
                time.sleep(30)
                print("Sending ping")
                sock.sendall("P\r\n".encode('utf-8'))
            else :
                print("sending ping")
                sock.sendall("P\r\n".encode('utf-8'))

            #else:
            #    sock.sendall("{\"packet\":\"login\",\"headers\":{ \"user\":\"ariel\",\"pass\":\"meo\",\"device\":\"\",\"version\":\"\"}}".encode('utf-8'))
             
    finally:
        print('closing the socket')
        sock.close()

        

if __name__ == '__main__':
    main()
