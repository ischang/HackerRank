def fib():
	fibEvenSum = 0
	a = 0
	b = 1

	while a < 4000000:
		a, b = b, a+b

		if a % 2 == 0:
			fibEvenSum = fibEvenSum + a

	return fibEvenSum

print fib()
