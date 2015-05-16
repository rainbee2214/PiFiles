import pi
import itertools
from time import time

validHex = '0123456789ABCDEF'
# oneByte = itertools.product(validHex, repeat=4)

oneByte = [('1', '0', '3', '7'), ('1', '0', '9', 'B'), ('1', '2', '5', '4'), ('1', '3', '9', 'E'), ('1', '3', 'F', '4'), ('1', '4', '5', '3'), ('1', '4', '5', '9'), ('1', '4', 'D', 'D'), ('1', '6', 'B', 'F'), ('1', '7', '9', 'F'), ('1', '8', '7', '9'), ('1', '8', '9', '7'), ('1', 'A', '9', '6'), ('1', 'C', 'B', 'F'), ('1', 'D', '8', '7'), ('1', 'D', '9', '4'), ('1', 'F', '9', 'E'), ('1', 'F', 'C', '3'), ('1', 'F', 'D', 'D'), ('2', '0', '3', '7'), ('2', '3', 'B', '5'), ('2', '4', '0', '5'), ('2', '5', '4', '1'), ('2', '5', '4', '9'), ('2', '7', '4', 'D'), ('2', '7', '5', '2'), ('2', '7', 'E', '7'), ('2', '9', '2', 'A'), ('2', '9', '3', '3'), ('2', 'A', '1', '9'), ('2', 'B', '3', '3'), ('2', 'B', '6', '9'), ('2', 'B', 'D', 'D'), ('2', 'F', '1', 'E'), ('2', 'F', '8', '9'), ('2', 'F', 'E', '2'), ('3', '2', '2', 'C'), ('3', '5', '0', '7'), ('3', '5', '0', 'B'), ('3', '5', '1', '2'), ('3', '5', '8', '1'), ('3', '6', '2', 'D'), ('3', '6', 'C', '9'), ('3', '7', 'A', '9'), ('3', '8', '2', 'B'), ('3', '8', '7', 'B'), ('3', '8', '9', '4'), ('3', '8', '9', '7'), ('3', '8', 'B', '9'), ('3', 'A', '4', 'D'), ('3', 'B', '7', '7'), ('3', 'D', 'A', '1'), ('3', 'D', 'B', '1'), ('3', 'F', '3', '6'), ('4', '0', '0', 'D'), ('4', '1', '3', 'A'), ('4', '1', '3', 'B'), ('4', '2', '4', 'C'), ('4', '4', '6', 'C'), ('4', '4', 'D', 'C'), ('4', '6', '4', 'E'), ('4', '6', '7', 'E'), ('4', '8', '9', 'B'), ('4', '9', '0', 'C'), ('4', 'B', '3', '2'), ('4', 'B', '3', 'D'), ('4', 'B', 'B', 'E'), ('4', 'C', 'C', '3'), ('4', 'F', '3', '3'), ('4', 'F', 'D', '3'), ('5', '0', '4', '7'), ('5', '2', '6', '3'), ('5', '2', 'E', '6'), ('5', '4', '3', '7'), ('5', '4', '9', '4'), ('5', '8', '0', 'B'), ('5', '9', 'B', '4'), ('5', 'A', 'E', '4'), ('5', 'C', 'A', '4'), ('5', 'E', 'D', 'A'), ('6', '0', '4', '7'), ('6', '2', 'F', '5'), ('6', '3', '8', '7'), ('6', '5', '5', '9'), ('6', '5', '5', 'D'), ('6', '6', '0', '2'), ('6', '8', '4', '5'), ('6', '8', '5', 'F'), ('6', 'A', '9', 'D'), ('6', 'B', '3', 'B'), ('6', 'C', '6', '5'), ('6', 'E', '7', 'B'), ('7', '0', 'E', '7'), ('7', '2', '1', '1'), ('7', '3', 'B', '6'), ('7', '5', '1', '7'), ('7', '5', '4', '9'), ('7', '6', 'F', 'D'), ('7', '7', '0', 'B'), ('7', '8', '8', '6'), ('7', '8', '9', 'D'), ('7', '9', '8', '5'), ('7', 'A', 'C', '1'), ('8', '1', '4', '8'), ('8', '1', 'E', 'B'), ('8', '4', 'C', '7'), ('8', '5', '4', '3'), ('8', '5', 'E', '6'), ('8', '7', 'B', 'B'), ('8', '9', '5', '5'), ('8', 'A', '4', '9'), ('8', 'B', 'F', 'A'), ('8', 'E', '5', '6'), ('8', 'F', '7', 'D'), ('9', '0', '3', 'A'), ('9', '1', 'F', '5'), ('9', '1', 'F', 'B'), ('9', '2', '5', 'A'), ('9', '4', '4', '5'), ('9', '5', 'C', 'C'), ('9', '6', '8', 'A'), ('9', '8', '4', '5'), ('9', '8', 'E', 'F'), ('9', '9', '2', '7'), ('9', 'A', 'F', 'A'), ('9', 'C', '0', '1'), ('9', 'C', '0', '3'), ('9', 'D', '0', 'F'), ('A', '2', '1', '7'), ('A', '3', '7', 'B'), ('A', '3', 'F', 'B'), ('A', '8', 'D', 'A'), ('A', 'C', 'D', '1'), ('A', 'E', 'D', '9'), ('A', 'F', '9', '7'), ('A', 'F', 'E', 'B'), ('B', '0', 'B', '5'), ('B', '0', 'D', 'B'), ('B', '2', '5', 'F'), ('B', '7', '2', 'A'), ('B', '7', '3', '3'), ('B', '7', '5', '3'), ('B', '8', 'A', 'C'), ('B', 'A', '0', 'E'), ('B', 'A', '7', '4'), ('B', 'D', '1', '6'), ('B', 'D', 'C', 'F'), ('B', 'E', '8', '5'), ('B', 'E', '8', 'E'), ('B', 'F', 'A', '7'), ('B', 'F', 'F', 'D'), ('C', '0', '0', 'C'), ('C', '2', 'D', '5'), ('C', '2', 'F', '5'), ('C', '3', '6', 'C'), ('C', '4', 'A', 'E'), ('C', '7', '1', '7'), ('C', 'A', 'A', '7'), ('C', 'B', 'C', '1'), ('C', 'B', 'F', '2'), ('C', 'D', '1', 'E'), ('D', '0', '4', '9'), ('D', '3', '5', '1'), ('D', '4', 'A', '3'), ('D', '6', 'B', '7'), ('D', '7', 'B', '9'), ('D', '7', 'D', '3'), ('D', '8', 'B', '7'), ('D', '9', '1', '9'), ('D', 'A', '0', '4'), ('D', 'A', 'B', '5'), ('D', 'B', 'C', '9'), ('D', 'D', '2', 'A'), ('E', '1', '0', '4'), ('E', '1', '4', 'D'), ('E', '2', '7', '2'), ('E', '2', 'A', '5'), ('E', '3', '0', 'F'), ('E', '3', '1', '6'), ('E', '3', '6', '3'), ('E', '4', 'A', 'E'), ('E', '5', '6', '7'), ('E', '6', '2', 'B'), ('E', '7', '2', '9'), ('E', '7', '4', '3'), ('E', '8', '4', '9'), ('E', 'A', '6', '7'), ('E', 'A', 'C', '7'), ('E', 'B', '0', '9'), ('E', 'B', '2', 'B'), ('E', 'C', '1', '9'), ('E', 'C', '9', 'E'), ('E', 'C', 'E', '3'), ('E', 'C', 'F', 'D'), ('E', 'D', '8', '6'), ('E', 'D', 'D', 'D'), ('E', 'F', '3', 'D'), ('F', '0', '7', 'B'), ('F', '1', '0', '9'), ('F', '1', '2', '1'), ('F', '2', 'A', 'A'), ('F', '4', 'E', 'F'), ('F', '6', '5', 'F'), ('F', '7', '2', '3'), ('F', '8', '4', '3'), ('F', 'F', '7', 'E'), ('F', 'F', '9', 'E')]

foundIndices = []

startOfStrings = time()

currentString = ""
for y in range(300000, 310000, 8):
    print "index", y
    currentString += pi.getHexFromIndex(y)

endOfStrings = time()

print "length 300000 string took", endOfStrings - startOfStrings

startOfPattern = time()

notFoundCount = 0

for pattern in oneByte:
    foundAt = currentString.find(pattern[0] + pattern[1] + pattern[2] + pattern[3])
    if foundAt > -1:
        # print "found", pattern[0] + pattern[1] + pattern[2] + pattern[3], "at", foundAt
        foundIndices.append((pattern, foundAt + 300000))
    else:
        # print "didn't find", pattern[0] + pattern[1] + pattern[2] + pattern[3]
        notFoundCount += 1
        foundIndices.append((pattern, "Not found in tenthousand"))

endOfPattern = time()

print "all 2 byte patterns took", endOfPattern - startOfPattern
print "didn't find", notFoundCount

with open("02ByteMissing.dat", 'w') as f:
    data = f.write('\n'.join('%s %s' % x for x in foundIndices))
