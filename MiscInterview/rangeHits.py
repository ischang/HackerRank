#You are given an array with distinct numbers between 1 to 100.
#You have to return a string which says the number's range which are not in
#the given array separated by comma. Eg: Input: [50,75] Output: (0-49,51-74,76-100)

#solve base case first, then deal with edge cases
def rangeHits (arr):
	rangeList = []
	minRange = 0
	maxRange = 0
	hitsRange = " "

	arr.sort()

	# if a value is 1, then 0 cannot be a range
	# start with 2
	if arr[0] == 1:
		minRange = 2

	print arr
	for i in range(len(arr)):
		# if there's consecutive ranges to look out for
		# make sure to skip and set appropriate min range
		if arr[i]-1 == arr[i-1]:
			# if there's only two numbers that are consecutive
			# sets the same number as the last if check
			# however, if there are multiple consecutive number
			# sets the minRange as the number after
			minRange = arr[i]+1
			continue

		# set the max range
		maxRange = arr[i]-1

		# if the min range and the max range are the same number
		# just append one value to the list of ranges
		# and set the min range as the next number
		if minRange == maxRange:
			rangeList.append(str(maxRange))
			minRange = arr[i]+1

		# otherwise, set ranges normally
		else:
			hitsRange = str(minRange) + "-" + str(maxRange)
			rangeList.append(hitsRange)
			minRange = arr[i] + 1

		# if number is 100 or greater, break
		# can't break earlier, since need to append from before 100
		if arr[i] >= 100:
			break

		# if it's the last number, make sure to set the last value for
		# x - 100
		elif i == len(arr)-1:
			hitsRange = str(minRange) + "-" + str(100)
			rangeList.append(hitsRange)

		# if there are consecutive numbers, make sure to set minRange as one up
		# and skip appropriately
		elif i != len(arr)-1 and arr[i]+1 == arr[i+1]:
			minRange = arr[i+1] + 1

	return rangeList

# 0-49, 51-74, 76-100
print rangeHits([50, 75])
# 0-11, 13-49, 52-74, 76-100
print rangeHits([75, 50,51,12])
#0-49, 51, 53-100
print rangeHits([50, 52])
#0-49, 51-99
print rangeHits([50, 100])
# 0-11, 13-49, 53-74, 76-100
print rangeHits([50,51,52,12,75])