string1 =input()
#For Davis Algorithm Hackathon
#Given a string of multiple helloworlds and other words, find how many substrings and print
#e.g. helloworldishelloworld would have 3
#e.g. worldhello would have 0

i = 0
helloCount = 0
count = 0
#while i < len(string1):
helloList = []
hello = ""

for i in string1:
	hello = hello + i
	if i == 'h':
		hello = 'h'
	elif i == 'w':
		hello = 'w'
	elif hello == 'hello':
		helloCount += 1
		hello = ""
	elif hello == 'world':
		count = count +helloCount 
		hello = ""

print(count)
	 
#while i < len(string1):
