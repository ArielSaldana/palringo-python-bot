'''
convert all dictionary keys and values to lowercase
so we don't come into ambiguity issues 
'''


from PacketTemplate import *
from Salsa20 import *
from urllib.request import urlopen
#from PIL import Image
import io
import time
import locale



class Parser(object):
    def __init__(self):
        global command
        global payload
        global sourceID
        global targetID
        self.command = ""
        self.payload = ""
    ## global variables

    
    ##command = ""
    sourceID = 0
    targetID = 0
    #global command
    #global payload
    sock = object()
    debug = False

    def bind(self, obj, boolean):
        global sock
        global debug
        sock = obj
        debug = boolean
    def ParsePacket( self, param1 ):
        
        myDict = { }
            
        ## splits the data by headers and payload

        try:
            Parse = param1.decode('raw-unicode-escape').split('\r\n\r\n')
            #global payload
            self.payload = Parse[1]
        except:
            pass

        ## splits the headers
        try:
            Headers = str(Parse[0]).split('\r\n')

            ## the command is the first index and we remove it from the list
            self.command = Headers[0]
            Headers.pop(0)
        except:
            pass
       
        ## splits the Headers in the dictionary
        try:
            for x in range (0, int(len(Headers))):
                holder = Headers[x].split(':')
                myDict.update({holder[0]:holder[1]})
        except:
            pass

        ## assignment

        

        if ( "Target-Id" in myDict):
            self.sourceID = myDict['Source-Id']
            self.targetID = myDict['Target-Id']
            self.command = "GroupMESG"



        elif ( "SOURCE-ID" in myDict):
            self.sourceID = myDict['SOURCE-ID']
            self.command = "PrivMESG"

        

        ## Clear our dictionary so it doesn't hold old values
        myDict.clear()
        



    ## Getter methods
    def getSourceID(self):
        return int(self.sourceID)
    def getTargetID(self):
        return int(self.targetID)
    def getPayload(self):
        return self.payload
    def getCommand(self):
        return self.command
    



    ## send methods
    def sendGroupMessage(self, i, s):
        sock.sendall(packets.GROUPMESG(str(i), s))
    def sendPrivateMessage(self, i, s):
        sock.sendall(packets.PRIVATEMESG(str(i), s))
    def Send(self, pack):
        sock.sendall()
    def sendLogon(self, email):
        sock.sendall(packets.LOGON(email))
    def sendAuth(self, password):
        sock.sendall(packets.AUTH(PalringoAuth(password.encode('raw-unicode-escape'), self.payload.encode('raw-unicode-escape'))))

    def sendPing(self):
        sock.sendall(packets.PING())
    def sendImage(self, boolean, path, group):
        if (boolean):
            try:
                pic = Image.open(path)
                dat = io.BytesIO()
                if (pic.format == "JPEG"):
                    pic.save(dat, format='JPEG')
                else:
                    pic.load()
                    try:
                        holder = Image.new("RGB", pic.size, (255, 255, 255))
                        try:
                            holder.paste(pic, mask=pic.split()[3]) # 3 is the alpha channel
                            holder.save(dat, format='JPEG')
                        except:
                            pic.save(dat, format='JPEG')
                    except:
                        pass
                data = dat.getvalue()

                packetsize = int(len(data)/512)
                if (len(data) % 512 > 0):
                    packetsize = packetsize + 1

                chunks = Parser.split_by_length(data, 512)

                
                sock.sendall(packets.SENDIMAGEHEADER(chunks[0], group, len(data)))

                for x in range(1, (packetsize - 1)):
                    sock.sendall(packets.SENDIMAGEBODY(chunks[x], group))

                sock.sendall(packets.SENDIMAGEFINAL(chunks[packetsize-1], group))

                
                del dat, pic
            except:
                #raise Exception('Error')
                pass
                
        else:
            try:
                data = urlopen(path).read()

                packetsize = int(len(data)/512)
                if (len(data) % 512 > 0):
                    packetsize = packetsize + 1

                chunks = Parser.split_by_length(data, 512)

                
                sock.sendall(packets.SENDIMAGEHEADER(chunks[0], group, len(data)))

                for x in range(1, (packetsize - 1)):
                    sock.sendall(packets.SENDIMAGEBODY(chunks[x], group))

                sock.sendall(packets.SENDIMAGEFINAL(chunks[packetsize-1], group))

            except:
                pass
    
    
    def split_by_length(s,block_size):
        w=[]
        n=len(s)
        for i in range(0,n,block_size):
            w.append(s[i:i+block_size])
        return w
        
if __name__ == '__main__':
    Parser()
        
        
            


        
           
        
