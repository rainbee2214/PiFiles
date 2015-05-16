import sys
import string
import pi
import itertools
from time import time

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

#Takes a list of numbers as strings, checks for duplicates, returns true or false
def CheckForDuplicates(filename):
    openFile = open(filename, 'r')
    lines = []
    for line in openFile:
        lines.append(line[8:22])

    print "Number of lines: ", len(lines)
    lines.sort()
    lines = set(lines)
    print "Number of lines: ", len(lines)
    # for line in lines:
    #     print line
    return True

def getCombinations(repeat = 2, validHex = '0123456789ABCDEF'):
    return itertools.product(validHex, repeat=repeat)


def main(argv):
    DATA_PATH = "Data/"
    
    piChunks = {}
    oneHexFile = open(DATA_PATH+"oneHex.dat")

    for line in oneHexFile:
        key = line[:1]
        token = line[2:4]
        piChunks[key] = token

    oneHexBit = getCombinations(7)

    filename = DATA_PATH+"sevenHexCombinations.dat"
    dupFound = False
    with open(filename, 'w') as f:
        for bit in oneHexBit:
            dChunk = ''.join(bit)
            piChunk = piChunks[bit[0]]
            piChunk += piChunks[bit[1]]
            piChunk += piChunks[bit[2]]
            piChunk += piChunks[bit[3]]
            piChunk += piChunks[bit[4]]
            piChunk += piChunks[bit[5]]
            piChunk += piChunks[bit[6]]
            encodedChunk = base_encode(int(piChunk))
            f.write(dChunk+","+piChunk+","+encodedChunk+"\n")

        
    dupFound = CheckForDuplicates(filename)
    
    print "Duplicates found:", dupFound 

if __name__ == "__main__":
   main(sys.argv[1:])

# validHex = '0123456789ABCDEF'
# repeat = 1
# threeBit = itertools.product(validHex, repeat=repeat)
# chunks = []
# piecesOfPi = []
# i = 0
# for x in threeBit:
#     chunks.append(x[0])
#     i += 1
# i = 0
# for line in oneHexFile:
#     piecesOfPi.append(x[0])
#     i += 1