def unsortedArray(arr):
	dupHash = dict()
	cleanList = []

	for integer in arr:
		if integer not in dupHash:
			dupHash[integer] = integer
		if integer in dupHash:
			continue

	for integer in dupHash:
		cleanList.append(integer)

	print "duplicates removed and sorted", cleanList

arr = [1,5,2,6,8,9,1,1,10,3,2,4,1,3,11,3]
print "original array", arr
unsortedArray(arr)