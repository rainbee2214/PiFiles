import pi
from time import time
from sys import argv

script, startIndex, length = argv
print 'script, length', script, length

endIndex = int(startIndex) + int(length)
print 'end', endIndex

startOfStrings = time()

currentString = ""
for y in range(int(startIndex), endIndex, 8):
    print "index", y
    currentString += pi.getHexFromIndex(y)

endOfStrings = time()

print "string of pi from", startIndex, 'to', endIndex, 'took', endOfStrings - startOfStrings, 'seconds'

with open("Data/Pi_"+startIndex+"_"+str(endIndex)+".txt", 'w') as f:
    data = f.write(currentString)
