class packets:

    def LOGON(email):
        packet = 'LOGON\r\n'
        packet += 'Client-ID: Kryis-Bot\r\n'
        ##packet += 'Operator: OSX_CLIENT\r\n'
        ##packet += 'app-type: Apple/Intel\r\n'
        packet += 'Operator: SERVER\r\n'
        packet += 'app-type: Palringo/bot\r\n'
        packet += 'capabilities: 4\r\n'
        packet += 'name: '+email+'\r\n'
        packet += 'protocol-version: 2.4\r\n'
        ##packet += 'client-version: 2.6.6 r\r\n'
        ##packet += 'fw: win 6.1\r\n'
        ##packet += 'last: 1\r\n'
        ##packet += 'affiliate-id: winpc\r\n'
        ##packet += 'app-identifier: 00000\r\n'
        packet += '\r\n'
        rawPacket = packet.encode('raw-unicode-escape')
        return rawPacket

    def AUTH(encryptedPassword):
        packet = 'AUTH\r\n'
        packet += 'Encryption-Type: 1\r\n'
        packet += 'Online-Status: 1\r\n'
        packet += 'Last: 1\r\n'
        packet += 'Content-Length: 32\r\n'
        packet += '\r\n'
        packet += encryptedPassword
        rawPacket = packet.encode('raw-unicode-escape')
        return rawPacket

    def PING():
        return b'P\r\n\r\n'
    '''
    def GROUPMESG(intt, stringg):
        packet = 'MESG\r\n'
        packet += 'Content-length: '+str(len(stringg))+'\r\n'
        packet += 'content-type: text/plain\r\n'
        packet += 'last: 1\r\n'
        packet += 'mesg-id: 666\r\n'
        packet += 'mesg-target: 1\r\n'
        packet += 'target-id: '+str(intt)+'\r\n'
        packet += '\r\n'
        packet += stringg
        rawPacket = packet.encode('raw-unicode-escape')
        return rawPacket
    '''
    '''
    def GROUPMESG(intt, stringg):
        packet = 'MESG\r\n\
        Content-length: '+str(len(stringg))+'\r\n\
        content-type: text/plain\r\n\
        last: 1\r\n\
        mesg-id: 666\r\n\
        mesg-target: 1\r\n\
        target-id: '+str(intt)+'\r\n\
        \r\n'
        + stringg
        rawPacket = packet.encode('raw-unicode-escape')
        return rawPacket
    '''
    '''
    def GROUPMESG(intt, stringg):
        packet = 'MESG\r\n\
Content-length: %s\r\n\
content-type: text/plain\r\n\
last: 1\r\n\
mesg-id: 666\r\n\
mesg-target: 1\r\n\
target-id: %s\r\n\r\n%s' % (str(len(stringg)), str(intt), stringg )
        rawPacket = packet.encode('utf-8')
        return rawPacket
    '''


    def MESGPACK(intt, stringg):
        packet = ''.join(
        ["MESG\r\n", 
        "Content-length: %s\r\n" % (str(len(stringg))),
        "content-type: image/jpeghtml\r\n",
        "last: 1\r\n",
        "mesg-id: 666\r\n",
        "Timestamp: 1402632927.955511",
        "mesg-target: 1\r\n",
        "target-id: %s\r\n\r\n%s"]) % (str(intt), stringg )
        rawPacket = packet.encode('utf-8')
        return rawPacket
    
    def GROUPMESG(intt, stringg):
        packet = ''.join(
        ["MESG\r\n", 
        "Content-length: %s\r\n" % (str(len(stringg))),
        "content-type: text/plain\r\n",
        "last: 1\r\n",
        "mesg-id: 666\r\n",
        "mesg-target: 1\r\n",
        "target-id: %s\r\n\r\n%s"]) % (str(intt), stringg )
        rawPacket = packet.encode('utf-8')
        return rawPacket
    

    def PRIVATEMESG(intt, stringg):
        packet = 'MESG\r\n'
        packet += 'Content-length: '+str(len(stringg)) + '\r\n'
        packet += 'content-type: text/plain\r\n'
        packet += 'last: 1\r\n'
        packet += 'mesg-id: 666\r\n'
        packet += 'mesg-target: 0\r\n'
        packet += 'target-id: '+str(intt)+'\r\n'
        packet += '\r\n'
        packet += stringg
        rawPacket = packet.encode('raw-unicode-escape')
        return rawPacket

    def JOINGROUP(groupname):
        packet = 'GROUP SUBSCRIBE\r\n'
        packet += 'last: 1\r\n'
        packet += 'mesg-id: 686\r\n'
        packet += 'name: '+groupname+'\r\n'
        packet += '\r\n'
        rawPacket = packet.encode('raw-unicode-escape')
        return rawPacket

    def LEAVEGROUP(groupid):
        packet = 'GROUP UNSUB\r\n'
        packet += 'group-id: '+str(groupid)+'\r\n'
        packet += 'last: 1\r\n'
        packet += 'mesg-id: 666\r\n'
        rawPacket = packet.encode('raw-unicode-escape')
        return rawPacket
    '''
     def GROUPMESG(intt, stringg):
        packet = ''.join(
        ["MESG\r\n", 
        "Content-length: %s\r\n" % (str(len(stringg))),
        "content-type: text/plain\r\n",
        "last: 1\r\n",
        "mesg-id: 666\r\n",
        "mesg-target: 1\r\n",
        "target-id: %s\r\n\r\n%s"]) % (str(intt), stringg )
        rawPacket = packet.encode('utf-8')
        return rawPacket
    '''

    
    def SENDIMAGEHEADER(data, intt, inttt):
        packet = ''.join(
        ["MESG\r\n",
        "content-length: 512\r\n",
        "content-type: image/jpeg\r\n",
        "mesg-id: 1337\r\n",
        "mesg-target: 1\r\n",
        "target-id: %s\r\n" % (str(intt)),
        "total-Length: %s\r\n\r\n"]) %(str(inttt))
        rawPacket = packet.encode('raw-unicode-escape')
        return rawPacket+data

    def SENDIMAGEBODY(data, intt):
        packet = ''.join(
        ["MESG\r\n",
        "content-length: %s\r\n" % (str(len(data))),
        "content-type: image/jpeg\r\n",
        "correlation-id: 1337\r\n",
        "mesg-id: 1337\r\n",
        "mesg-target: 1\r\n",
        "target-id: %s\r\n\r\n"]) % (str(intt))
        rawPacket = packet.encode('raw-unicode-escape')
        return rawPacket+data

    def SENDIMAGEFINAL(data, intt):
        packet = 'MESG\r\n'
        packet += 'content-length: ' + str(len(data))+'\r\n'
        packet += 'content-type: image/jpeg\r\n'
        packet += 'correlation-id: 1337\r\n'
        packet += 'last: 1\r\n'
        packet += 'mesg-id: 1337\r\n'
        packet += 'mesg-target: 1\r\n'
        packet += 'target-id: '+str(intt)+'\r\n'
        packet += '\r\n'
        test = packet.encode('raw-unicode-escape')
        #packet += data
        test += data
        return test


