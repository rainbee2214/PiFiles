import pi
import string
import uuid
import os
from twilio.rest import TwilioRestClient
 
def sendSMS(message):
    # Your Account Sid and Auth Token from twilio.com/user/account
    fromNumber = "+19027019415"
    toNumber = "+19028188219"
    account_sid = "AC159a87ecb340d7f1791f2959c9a951fa"
    auth_token  = "d96192096e44d9dd87c3f4e8aaafa8cd"
    client = TwilioRestClient(account_sid, auth_token)
     
    message = client.messages.create(body=message,
        to=toNumber,    
        from_=fromNumber) 

BASE_LIST = string.digits + string.letters + string.punctuation
BASE_DICT = dict((c, i) for i, c in enumerate(BASE_LIST))

def base_decode(string, reverse_base=BASE_DICT):
    length = len(reverse_base)
    ret = 0
    for i, c in enumerate(string[::-1]):
        ret += (length ** i) * reverse_base[c]

    return ret

def base_encode(integer, base=BASE_LIST):
    length = len(base)
    ret = ''
    while integer != 0:
        ret = base[integer % length] + ret
        integer /= length

    return ret
    
#Return a dictionary with the data chunks : index in file
def getPiWithTwoHex():
    piIndexFilename = os.path.join(os.path.dirname(__file__),"Data/01Byte.dat")
    piIndex = open(piIndexFilename)

    piDictionary = {}
    for line in piIndex:
        piDictionary[line[2:3]+line[7:8]] = line[11:len(line) - 1]

    return piDictionary

def getPiWithThreeHex():
    piIndexFilename = os.path.join(os.path.dirname(__file__),"Data/01HalfByte.dat")
    piIndex = open(piIndexFilename)

    piDictionary = {}
    for line in piIndex:
        piDictionary[line[2:3]+line[7:8]+line[12:13]] = line[16:len(line) - 1]

    return piDictionary

def getPiWithFourHex():
    piIndexFilename = os.path.join(os.path.dirname(__file__),"Data/01HalfByte.dat")
    piIndex = open(piIndexFilename)

    piDictionary = {}
    for line in piIndex:
        piDictionary[line[2:3]+line[7:8]+line[12:13]] = line[16:len(line) - 1]

    return piDictionary

def encode(inputFilename, outputFilename, piDictionary, chunkSize  = 2):
    with open(inputFilename, 'rb') as f:
        data = f.read().encode('hex').upper()
        chunks = [data[i:i+chunkSize] for i in range(0, len(data), chunkSize)]

    outputFile = open("EncodedFiles/"+str(uuid.uuid4())+outputFilename, 'w')

    outputFile.write("ChunkSize:"+str(chunkSize)+ "\n")
    for dataChunk in chunks:    
        baseStr = base_encode(int(piDictionary[dataChunk]))
        baseStr += ' '
        outputFile.write(baseStr)

    outputFile.close()

def decode(inputFilename, outputFilename, piDictionary, chunkSize  = 2):
    dataChunks = []
    with open(inputFilename, 'rb') as f:
        for line in f:
            if len(line) > 20: # Only use the second line
                dataChunks = line.split()

    outputFile = open("EncodedFiles/"+str(uuid.uuid4())+outputFilename, 'wb')

    newPiDictionary = {}
    for x in piDictionary:
        newPiDictionary[piDictionary.get(x)] = x
        # print x, piDictionary.get(x)

    for data in dataChunks:
        # print newPiDictionary.get(str(base_decode(data)))
        outputFile.write(newPiDictionary.get(str(base_decode(data))).decode("hex"))

def encodeMessage(inputMessage, piDictionary, chunkSize  = 2, sendToSMS = False):
    inputMessage = inputMessage.encode("hex").upper()
    chunks = [inputMessage[i:i+chunkSize] for i in range(0, len(inputMessage), chunkSize)]

    outputMessage = ''
    for dataChunk in chunks:    
        baseStr = base_encode(int(piDictionary[dataChunk]))
        baseStr += ' '
        outputMessage += baseStr

    print outputMessage

    if eval(sendToSMS):
        sendSMS(outputMessage)

    return outputMessage

def decodeMessage(inputMessage, piDictionary, chunkSize  = 2, sendToSMS = False):
    chunks = inputMessage.split()

    newPiDictionary = {}
    for x in piDictionary:
        newPiDictionary[piDictionary.get(x)] = x
        
    outputMessage = ''
    for dataChunk in chunks:    
        outputMessage += newPiDictionary.get(str(base_decode(dataChunk))).decode("hex")

    print outputMessage

    if eval(sendToSMS):
        sendSMS(outputMessage)
        
    return outputMessage
