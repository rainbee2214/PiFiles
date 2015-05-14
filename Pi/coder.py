import sys
import pi
import string
import uuid

chunkSize = 2
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
    piIndexFilename = "Data/01byte.dat"
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

#Takes a data chunk and finds the appropriate pi index from the current file [right now works for 01byte.dat]
def getIndex(piDictionary, dataChunk):

    return 

def encode(inputFilename, outputFilename, piDictionary):
    with open(inputFilename, 'rb') as f:
        data = f.read().encode('hex').upper()
        chunks = [data[i:i+chunkSize] for i in range(0, len(data), chunkSize)]
    print chunks

    outputFile = open("EncodedFiles/"+str(uuid.uuid4())+outputFilename, 'w')

    for dataChunk in chunks:    
        outputFile.write(base_encode(int(piDictionary[dataChunk]))+" ")
        print base_encode(int(piDictionary[dataChunk]))

    outputFile.close()



    # TODO:
    #   - Encode filename/type, save to outputFilename
    #   - Get indices corresponding each chunk
    #   - Save indices to outputFilename 

def decode(inputFilename, outputDirectory):
    with open(inputFilename, 'rb') as f:
        data = f.read()

    # TODO:
    #   - Decode filename/type
    #   - Get indices, compute to hex
    #   - Decode hex, save to outputDirectory


def convertBase(incomingHex):
    base35 = incomingHex

    return base35

def printFile(inputFilename):
    # with open(inputFilename, 'rb') as f:
    #     data = f.read().encode('hex').upper()
    #     print data

    inFile = open(inputFilename, 'rb')
    for line in inFile:
        print line

def main(argv):
    script, filename = sys.argv
                                
    printFile(filename)  
    # encode(filename, '_Encoded.pi', getPiWithTwoHex())



if __name__ == "__main__":
   main(sys.argv[1:])