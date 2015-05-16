import sys
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

    piList = []
    piDictionary = {}
    for line in piIndex:
        # print line
        piDictionary[line[2:3]+line[7:8]] = line[11:len(line) - 1]
        piList.append([line[2:3]+line[7:8], line[11:len(line) - 1]])
    # print piList
    # print piDictionary
    return piDictionary

def getPiWithThreeHex():
    piIndexFilename = "Data/01HalfByte.dat"
    piIndex = open(piIndexFilename)

    piList = []
    piDictionary = {}
    for line in piIndex:
        # print line        
        piDictionary[line[2:3]+line[7:8]+line[12:13]] = line[16:len(line) - 1]
        piList.append([line[2:3]+line[7:8]+line[12:13], line[16:len(line) - 1]])


    # print piList
    # print piDictionary
    return piDictionary

def getPiWithFourHex():
    piIndexFilename = "Data/01HalfByte.dat"
    piIndex = open(piIndexFilename)

    piList = []
    piDictionary = {}
    for line in piIndex:
        # print line        
        piDictionary[line[2:3]+line[7:8]+line[12:13]] = line[16:len(line) - 1]
        piList.append([line[2:3]+line[7:8]+line[12:13], line[16:len(line) - 1]])


    # print piList
    # print piDictionary
    return piDictionary

def encode(inputFilename, outputFilename, piDictionary, chunkSize  = 2):
    with open(inputFilename, 'rb') as f:
        data = f.read().encode('hex').upper()
        chunks = [data[i:i+chunkSize] for i in range(0, len(data), chunkSize)]
    # print chunks

    outputFile = open("EncodedFiles/"+str(uuid.uuid4())+outputFilename, 'w')

    indexLength = getLengthOfLongest(piDictionary)

    outputFile.write("Index Length: "+str(indexLength)+"\n")
    for dataChunk in chunks:    
        baseStr = base_encode(int(piDictionary[dataChunk]))
        # if len(baseStr) < indexLength:
            # for i in range(indexLength-len(baseStr)-1):
        baseStr += ' '
        outputFile.write(baseStr)
        # print base_encode(int(piDictionary[dataChunk]))

    outputFile.close()

    # TODO: DONE BABY
    #   - Encode filename/type, save to outputFilename
    #   - Get indices corresponding each chunk
    #   - Save indices to outputFilename 

def decode(inputFilename, outputFilename, piDictionary, chunkSize  = 2):
    # with open(inputFilename, 'rb') as f:
    #     data = f.read()
    getLengthOfLongest(piDictionary)

    # TODO:
    #   - Decode filename/type
    #   - Get indices, compute to hex
    #   - Decode hex, save to outputDirectory


def printFile(inputFilename):
    inFile = open(inputFilename, 'rb')
    for line in inFile:
        print line

def getLengthOfLongest(piDictionary):
    length = 0
    for x in piDictionary:
        if len(piDictionary.get(x)) > length:
            length = len(piDictionary.get(x))
    return length

def main(argv):
    # print len(sys.argv)
    # if len(sys.argv) == 4:
    script, filename = sys.argv

    encode(filename, '_Encoded_2.pi', getPiWithTwoHex(), 2)
    # decode(filename, '_Decoded_2.pi', getPiWithTwoHex(), 2)    
    # encode(filename, '_Encoded_3.pi', getPiWithThreeHex(), 3)
    # decode(filename, '_Decoded_3.pi', getPiWithThreeHex(), 3)



if __name__ == "__main__":
   main(sys.argv[1:])