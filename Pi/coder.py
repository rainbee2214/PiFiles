import pi
import string
import uuid
   
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
    piIndexFilename = "Data/01Byte.dat"
    piIndex = open(piIndexFilename)

    piDictionary = {}
    for line in piIndex:
        piDictionary[line[2:3]+line[7:8]] = line[11:len(line) - 1]

    return piDictionary

def getPiWithThreeHex():
    piIndexFilename = "Data/01HalfByte.dat"
    piIndex = open(piIndexFilename)

    piDictionary = {}
    for line in piIndex:
        piDictionary[line[2:3]+line[7:8]+line[12:13]] = line[16:len(line) - 1]

    return piDictionary

def getPiWithFourHex():
    piIndexFilename = "Data/01HalfByte.dat"
    piIndex = open(piIndexFilename)

    piDictionary = {}
    for line in piIndex:
        piDictionary[line[2:3]+line[7:8]+line[12:13]] = line[16:len(line) - 1]

    return piDictionary

def encode(inputFilename, outputFilename, piDictionary, chunkSize  = 2):
    print "Chunk size:", chunkSize, "Encoding ", inputFilename, "and writing to", outputFilename
    with open(inputFilename, 'rb') as f:
        data = f.read().encode('hex').upper()
        chunks = [data[i:i+chunkSize] for i in range(0, len(data), chunkSize)]

    # outputFile = open("EncodedFiles/"+str(uuid.uuid4())+outputFilename, 'w')
    outputFile = open("EncodedFiles/"+outputFilename, 'w')

    outputFile.write("ChunkSize:"+str(chunkSize)+ "\n")
    for dataChunk in chunks:    
        baseStr = base_encode(int(piDictionary[dataChunk]))
        baseStr += ' '
        outputFile.write(baseStr)

    outputFile.close()

def decode(inputFilename, outputFilename, piDictionary, chunkSize  = 2):
    print "Chunk size:", chunkSize, "Decoding ", inputFilename, "and writing to", outputFilename
    dataChunks = []
    with open(inputFilename, 'rb') as f:
        for line in f:
            if len(line) > 20: # Only use the second line
                dataChunks = line.split()

    # outputFile = open("EncodedFiles/"+str(uuid.uuid4())+outputFilename, 'wb')
    outputFile = open("EncodedFiles/"+outputFilename, 'wb')

    newPiDictionary = {}
    for x in piDictionary:
        newPiDictionary[piDictionary.get(x)] = x

    for data in dataChunks:
        outputFile.write(newPiDictionary.get(str(base_decode(data))).decode("hex"))

def encodeMessage(inputMessage, piDictionary, chunkSize  = 2):
    inputMessage = inputMessage.encode("hex").upper()
    chunks = [inputMessage[i:i+chunkSize] for i in range(0, len(inputMessage), chunkSize)]

    outputMessage = ''
    for dataChunk in chunks:    
        baseStr = base_encode(int(piDictionary[dataChunk]))
        baseStr += ' '
        outputMessage += baseStr

    print outputMessage

    return outputMessage

def decodeMessage(inputMessage, piDictionary, chunkSize  = 2):
    chunks = inputMessage.split()

    newPiDictionary = {}
    for x in piDictionary:
        newPiDictionary[piDictionary.get(x)] = x

    outputMessage = ''
    for dataChunk in chunks:    
        outputMessage += newPiDictionary.get(str(base_decode(dataChunk))).decode("hex")

    print outputMessage

    return outputMessage
