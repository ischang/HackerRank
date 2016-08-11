#array [1, 2, 3, 7, 6]
#t = 9
#given an array and target number,  return indices of one pair that adds up to the 
#number in the array

def twoSum (t, arr =[]):
	hashTable = dict()

	for i in range(len(arr)):
		hashTable[arr[i]] = i

	for i in range(len(arr)):
		difference = t-arr[i]

		if difference in hashTable:
			print hashTable[difference] 
			print hashTable[arr[i]]
			break

	print hashTable

#O(n)
l = [1,2,3,7,6]
twoSum (9, l)

#implementation below prints duplicates and if target/2 exists, then removes that possibility too
#/* Given a list of numbers and numbers and print all pairs of the numbers from the list which adds up to given number 
#Input : {1,3,4,5,6,2,2} 6
#output: 
#1,5
#2,4
#2,4
#*/#
#
#

#def numSum (arr, t):
#    hashMap = dict()
#    count = 1 
#       
#    for i in range(0, len(arr)-1):
#       if arr[i] in hashMap:
#           count += 1
#           hashMap[arr[i]] = count
#           
#       elif arr[i] not in hashMap:
#           hashMap[arr[i]] = 1 
#      
#    for j in range(0, len(arr)-1):      
#        difference = t - arr[j]
#        
#        if arr[j] == difference and hashMap[difference] == 1:
#            continue
#        
#        #two conditions
#        #if t/2 occurs in input, and only occurs once, don't print
#        #if difference occurs more than once as count, then print those duplicates#

#        if difference in hashMap:
#            if hashMap[difference] > 1:
#                for k in range(0, hashMap[difference]):
#                    print difference
#                    print arr[j]
#                    continue
#            print difference
#            print arr[j]
#            
#            