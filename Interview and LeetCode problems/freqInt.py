#Find the most frequent integer in an array

def freqInt (arr):
	newDict = {}
	maxVal = -1
	maxKey = 0

	for item in arr:
		if item in newDict.keys():
			newDict[item] +=1
		else:
			newDict[item] = 1

	for key, value in newDict.items():
		if value > maxVal:
			maxVal = value
			maxKey = key

	return maxKey

print freqInt([1, 3, 2, 5, 1, 8, 11, 212, 1, 8, 9, 8, 1, 4, 1, 1])
print freqInt([2, 2, 615, 1, 1, -200, -200, -2, -1, 7, 7, 6, 0, 2, 1, 'a', 6, 12, 7, 7, 7, 7, 7, 7, 7])
