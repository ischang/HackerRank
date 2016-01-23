# Find the first non-repeated character in a String
# "call me ishmael" -- should be 'c'
# "albus percival wulfric brian dumbledore" - should be 's'
def nonRepeatChar(arr):
	repeatDict = {}

	for item in arr:
		if item in repeatDict.keys():
			repeatDict[item] += 1
		else:
			repeatDict[item] = 1

	for item in arr:
		if repeatDict[item] == 1:
			return item

	return -1

print nonRepeatChar("call me ishmael")
print nonRepeatChar("albus percival wulfric brian dumbledore")