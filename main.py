'''
Palringo Python Bot Developed by Ariel Saldana (Palringo ID 2015666)
'''

#!/usr/bin/python3.4
#from PIL import Image PIL IMAGE
import io
#import speex
import sys
import socket
import threading
from PacketTemplate import *
from Salsa20 import *
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
            parser.sendGroupMessage(4154538, str(datetime.datetime.now()))
        except:
            pass
        time.sleep(10)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('80.69.129.4',12345);
    print('Attempting to connect to the server')
    try:
        sock.connect(server_address)
    except:
        raise Exception('Error Connecting to the server')

    print('Connected succesfully')
    #thr2 = threading.Thread(target=clock)
    #thr2.start()
    try:
        parser = Parser.Parser()
        parser.bind(sock, False)
        parser.sendLogon('bot-email@bot.com')
        passwd = "password"

        amount_received = 0

        while True:
            data = sock.recv(65535)
            thr = threading.Thread(group=None, target=parser.ParsePacket, name=None, args=[(data)])
            ## pass our socket object to the parser class
            ## parse our data
            #parser.ParsePacket(data)
            thr.start()
            #e = speex.Encoder()
            #thr.is_alive() # will return whether foo is running currently
            #thr.join() # will wait till "foo" is donedef foo():

            if len(data) == 0:
                break
        
            else:
                if ( parser.getCommand() == 'GroupMESG'):
                    
                    '''
                    s = ''.join(
                        ["MESG\r\n",
                         "Content-length: %s\r\n" % (str(len(parser.getPayload()))),
                         "Content-type: image/jpeghtml\r\n",
                         "mesg-id: 666\r\n",
                         "mesg-target: 1\r\n",
                         "target-id: %s\r\n\r\n%s"]) % (str(parser.getTargetID()), parser.getPayload())
                    rawPacket = s.encode('raw-unicode-escape')

                    sock.sendall(rawPacket)
                    '''
                        


                    
                    
                    if (parser.getPayload().lower() == 'about'):
                        parser.sendGroupMessage(parser.getTargetID(), 'to download this bot\'s source code to go: http://ahhriel.com/blog/2015/03/15/Palringo-python-bot/')

                    if ("lol" in parser.getPayload().lower()):
                        parser.sendGroupMessage(parser.getTargetID(), 'stop laughing bitch nigga')
                        
                    
                    ## if jesse talks
                    #if ( parser.getSourceID() == 4604623 ):
                        #print("Jesse")
                   
                    m = re.search('<p class="dictionary_word">(.*?)</p>', parser.getPayload())
                    l = re.search('    (.*?)    ', parser.getPayload())
                    if m:
                        parser.sendGroupMessage(parser.getTargetID(), m.group(1))
                    if l:
                        parser.sendGroupMessage(parser.getTargetID(), l.group(1))
                        


                elif ( parser.getCommand() == 'PrivMESG'):
                    parser.sendPrivateMessage(parser.getSourceID(), "Do NOT message me here!")
                    
                elif (parser.getCommand() == 'AUTH'):
                    parser.sendAuth(passwd)

                elif ( parser.getCommand() == 'P'):
                    parser.sendPing()
             
    finally:
        print('closing the socket')
        sock.close()

        

if __name__ == '__main__':
    main()
