import os
import base64
import binascii
from urllib.request import urlopen
def main():

    #with open ('test.png', 'rb') as f:
        #data = f.read()
    

    #with open ('picture_out.png', 'wb') as f:
     #   f.write(data)
    
     
    url = "http://i50.tinypic.com/34g8vo5.jpg"

    data = urlopen(url).read()

    w = split_by_length(data, 512)
    print("Length of data: " + str(len(data)))
    print("Number of packets required to send all the data = " + str( int((len(data)/512) ) ) )
    print(len(data) % 512 )
    print(w[0])
    print(type(w[0]))





    '''
    f = open("test.png", "rb")
    ##b = os.path.getsize("test.png")
    ima = f.read()
    f.close()
    imgdata = base64.b64decode(ima)
    filename = 'some_image.png'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)
    '''

    '''
    f = open("test.png", "rb")
    b = os.path.getsize("test.png")
    ima = f.read(b)

    ima = base64.b64decode(ima)

    w = split_by_length(ima,512)

    print(w)
    ##print(ima.decode('utf-32'))
    '''

def split_by_len(text, chunksize):
    return [text[i:(i+chunksize)] for i in range(len(text)-chunksize+1)]


def split_by_length(s,block_size):
    w=[]
    n=len(s)
    for i in range(0,n,block_size):
        w.append(s[i:i+block_size])
    return w

if __name__ == '__main__':
    main()

        
