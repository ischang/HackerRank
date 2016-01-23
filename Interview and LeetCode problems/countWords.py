import collections

#words is a function that takes in a string and finds the max string int he string
#kwords is a funciton that takes in a string and a number and finds the top k max strings
#in the string
def words (string):
	countingWords = dict()
	maxiString = ""
	maxi = 1
	splitString = string.split(" ")

	for word in splitString:
		if word in countingWords:
			countingWords[word] +=1
		else:
			countingWords[word] = 1

	for word in countingWords:
		if countingWords[word] > maxi:
			maxi = countingWords[word]
			maxiString = word

	print maxiString


#doesn't compile because it sees kList[countingWords[word]].append(word) as int???
#WHY. Will work on later

#words compiles though
def kwords (string, k):
	countingWords = dict()
	maxString = ""
	maxi = 1
	splitString = string.split(" ")

	for word in splitString:
		if word in countingWords:
			countingWords[word] +=1
		else:
			countingWords[word] = 1

	for word in countingWords:
		if countingWords[word] > maxi:
			maxi = countingWords[word]
			maxiString = word

	kList = range(maxi)
	kList.insert(maxi, maxString)

	for word in countingWords:
		if not kList[countingWords[word]]:
			kList[countingWords[word]] = [word]
		elif kList[countingWords[word]]:
			kList[countingWords[word]].append(word)

	for i in range(k):
		nice = kList.pop()
		if nice is ' '
			i -= 1
			continue
		else:
			print nice


words("this this i am a super chocolate super super super super chocolate chocolate super chocolate")
words("a crazy fox crazy crazy nice nice me")
kwords("this this i am a super chocolate super super super super chocolate chocolate super chocolate",2)
kwords("a crazy fox crazy crazy nice nice me", 2)
