import pi
import itertools
from time import time

validHex = '0123456789ABCDEF'

repeat = 4
fourBit = itertools.product(validHex, repeat=repeat)
foundIndices = []

start = time()

for x in fourBit:
    # print "Searching for", x
    found = False
    index = 0
    while not found:
        test = pi.getHexFromIndex(index)
        if x[0] == test[0] and x[1] == test[1] and x[2] == test[2] and x[3] == test[3]:
            # print "Match!", x, test, index
            found = True
            foundIndices.append((x, index))
        elif x[0] == test[3] and x[1] == test[2] and x[2] == test[1] and x[3] == test[0]:
            found = True
            foundIndices.append((x, str(index)+'R'))
        else:
            index += 1

end = time()

print "four took", (end - start)/60, ":", (end - start)%60

with open("02Byte.dat", 'w') as f:
    data = f.write('\n'.join('%s %s' % x for x in foundIndices))
