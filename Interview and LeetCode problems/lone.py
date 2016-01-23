#n is the given array
#all numbers are duplicates except 1, find the 1 lone number

r = 0
def lone (arr):
	for i = 0 to range(len(arr)):
    	r = r xor arr[i]
   	print r

   	