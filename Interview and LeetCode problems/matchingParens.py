
def isPair(char1, char2):
	if char1 == '(' and char2 == ')':
		return True
	elif char1 == '{' and char2 == '}':
		return True
	elif char1 == '[' and char2 == ']':
		return True

	return False

def matchingParens(niceStr):
	niceString = list(niceStr)
	stack = []

	for character in niceString:
		if character == '(' or character == '{' or character == '[':
			stack.append(character)

		elif character == '}' or character == ']' or character == ')':
			if not stack:
				return False

			stackChar = stack.pop()
			if not isPair(stackChar, character):
				return False
		else:
			return False

	return not len(stack)

if matchingParens("{sdfsdf[]d"):
	print ":))))"
	#this should not print
if matchingParens("}[asdf[a[fsdf]sfsf]dfsf]"):
	print "smile" 
	#this should not print
if matchingParens("{{a{[[b]ddd]c}}}")
	print "nicki minaj"
	#this should print
if matchingParens("[]"):
	print "beyonce"
	#this should print
