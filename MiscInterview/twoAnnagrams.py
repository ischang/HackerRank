#determine if two strings are annagrams

def twoAnnagrams (str1, str2):
	# up to 30, just to be safe
	# use lists not dictionaries to keep track of number of characters
	# keeps track of order, so iterating over will be easier

	anna1 = [0] * 256
	anna2 = [0] * 256

	for char1 in str1:
		print ord(char1)
		anna1[ord(char1)] += 1

	for char2 in str2:
		anna2[ord(char2)] += 1

	if len(char1) != len(char2):
		return False

	for i in range(len(anna1)):
		if anna1[i] != anna2[i]:
			return False

	return True


print twoAnnagrams("hello", "olleh")
print twoAnnagrams("batee", "tab")
