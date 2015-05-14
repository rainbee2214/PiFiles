import pi
import itertools
from time import time

validHex = '0123456789ABCDEF'
threeByte = itertools.product(validHex, repeat=6)

foundIndices = []
sectionsOfPi = []

startOfStrings = time()

index = 0
for x in range(1000):
	currentString = ""
	for y in range(1000):
	    if y % 8 == 0:
	        currentString += pi.getHexFromIndex(index)
	    index += 1
	sectionsOfPi.append(currentString)

endOfStrings = time()

print "1000 strings of 1000 length of pi took", endOfStrings - startOfStrings

startOfPattern = time()

for pattern in threeByte:
	foundAt = -1
	index = 0
	for string in sectionsOfPi:
		foundAt = string.find(pattern[0] + pattern[1] + pattern[2] + pattern[3] + pattern[4] + pattern[5])
		if foundAt > -1:
			foundIndices.append((pattern, foundAt + (index * 1000)))
			break
		index += 1
	if foundAt == -1:
		foundIndices.append((pattern), "Not found in a million")

endOfPattern = time()

print "all 2.5 byte patterns took", endOfPattern - startOfPattern

with open("03byte.dat", 'w') as f:
    data = f.write('\n'.join('%s %s' % x for x in foundIndices))
