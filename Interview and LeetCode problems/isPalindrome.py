#Checks if a string is a palindrome and prints out whether it's true or not

def isPalindrome (strstr):
	meanList = list(strstr)
	niceList = list(reversed(strstr))

	if niceList == meanList:
		return True

	else:
		return False
	#return strstr[::-1] == strstr

if isPalindrome ("abba"):
	print "true"
if isPalindrome ("nah"):
	print "nah"

