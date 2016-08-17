def atoi (s):
	value = 0
	sign = 1
	i = 0

	if s[0] == "-":
		sign = -1
		i += 1

	for j in range(i, len(s)):
		value = ord(s[j]) - ord('0') + value*10

	print value*sign

atoi("469")
atoi("-1234")