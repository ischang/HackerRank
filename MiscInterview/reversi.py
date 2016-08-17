#reverse a string recursively and iteratively

def reverseIt (s):
	reverseS = ""

	for i in range(len(s)-1, -1, -1):
		reverseS = reverseS + s[i]

	print reverseS

reverseIt("panama")

def reverseRec (s):
	if s == "":
		return s
	else:
		return reverseRec(s[1:]) + s[0]

print reverseRec("panama a canal")

#single line
print "hello"[::-1]

#reverse a string in place

def reverseInPlace (s):
	# strings are immutable in py, so make it a list
	inPlace = list(s)

	for i in range(0, len(inPlace)/2):
		inPlace[i], inPlace[len(inPlace)-i-1] = inPlace[len(inPlace)-i-1], inPlace[i]

	print ''.join(inPlace)

reverseInPlace ("hello world")

# reverse words

def reverseWords (s):
	wordS = s.split()
	wordReverse = ' '.join(wordS[::-1])
	print wordReverse

reverseWords("hello world")