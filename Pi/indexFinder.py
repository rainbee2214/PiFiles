import pi
import itertools

validHex = '0123456789ABCDEF'
repeat = 3

twoBit = itertools.product(validHex, repeat=repeat)
foundIndices = []

for x in twoBit:
	# print "Searching for", x
	found = False
	index = 0
	while not found:
		test = pi.getHexFromIndex(index)
		if x[0] == test[0] and x[1] == test[1] and x[2] == test[3]:
			# print "Match!", x, test, index
			found = True
			foundIndices.append((x, index))
		elif x[0] == test[2] and x[1] == test[1] and x[2] == test[0]:
			found = True
			foundIndices.append((x, str(index)+'R'))
		else:
			index += 1

with open("output" + str(repeat), 'w') as f:
        data = f.write('\n'.join('%s %s' % x for x in foundIndices))

