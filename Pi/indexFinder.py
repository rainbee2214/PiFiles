import pi
import itertools
from time import time

validHex = '0123456789ABCDEF'
repeat = 1

threeBit = itertools.product(validHex, repeat=repeat)
foundIndices = []

start = time()

for x in threeBit:
    # print "Searching for", x
    found = False
    index = 0
    while not found:
        test = pi.getHexFromIndex(index)
        if x[0] == test[0] and x[1] == test[1]:
            # print "Match!", x, test, index
            found = True
            foundIndices.append((x, index))
        else:
            index += 1

end = time()

print "one byte took", (end - start)/60, ":", (end - start)%60

with open("01byte.dat", 'w') as f:
    data = f.write('\n'.join('%s %s' % x for x in foundIndices))
