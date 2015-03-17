#!/usr/bin/python3.4
##from PIL import Image
import io
import sys
import socket
import threading
from PacketTemplate import *
import Parser
import time
import datetime
import re ##regex 
import urllib
import json

def clock():
    while True:
        parser = Parser.Parser()
        print("test working")
        try:
            #parser.sendMessage(4154538, str(datetime.datetime.now()))
            parser.sendMessage(10634115, "!typing")
        except:
            pass
        time.sleep(10)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    htmlsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('80.69.129.117', 8080);

    print('Attempting to connect to the server')
    try:
        sock.connect(server_address)
        #htmlsock.connect(htmlserver_address)
    except:
        raise Exception('Error Connecting to the server')

    print('Connected succesfully')
    #thr2 = threading.Thread(target=clock)
    #thr2.start()
    try:
        parser = Parser.Parser()
        parser.bind(sock, False)
        ##LOGON INFORMATION HERE ===================================
        parser.sendLogon('email@domain.ltd')
        passwd = "password"
        ## ---------------------------------------------------------

        amount_received = 0

        while True:
            data = sock.recv(65535)
            #print(data)
            thr = threading.Thread(group=None, target=parser.ParsePacket, name=None, args=[(data)])
            ## pass our socket object to the parser class
            thr.start()
            #thr.is_alive() # will return whether foo is running currently
            #thr.join() # will wait till "foo" is donedef foo():

            if len(data) == 0:
                break
        
            else:
                ## GROUP MESSAGES
                if ( parser.getCommand() == 'GroupMESG'):
                    
                    ## if someone talks
                    #if ( parser.getSourceID() != 0 ):
                    #    parser.sendGroupMessage(parser.getTargetID(), "hello")
                    #parser.sendGroupMessage(parser.getTargetID(), "shut up")

                    #typing bot cheat
                    m = re.search('<p class="dictionary_word">(.*?)</p>', parser.getPayload())
                    l = re.search('    (.*?)    ', parser.getPayload())
                    if m:
                        parser.sendGroupMessage(parser.getTargetID(), m.group(1))
                    if l:
                        parser.sendGroupMessage(parser.getTargetID(), l.group(1))

  

                #private message
                elif ( parser.getCommand() == 'PrivMESG'):
                    parser.sendPrivateMessage(parser.getSourceID(), "Do NOT message me here!")
                    
                #logon auth command
                elif (parser.getCommand() == 'AUTH'):
                    print("auth requested")
                    parser.sendAuth(passwd)
                #ping - pong response 
                elif ( parser.getCommand() == 'P'):
                    parser.sendPing()
             
    finally:
        print('closing the socket')
        sock.close()

        

if __name__ == '__main__':
    main()
