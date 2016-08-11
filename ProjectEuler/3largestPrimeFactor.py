#not done

def largestPrime (val, i, primes):
	firstPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
	if i > len(firstPrimes):
		return primes

	elif val % firstPrimes[i] == 0:
		if firstPrimes[i] not in prime:
			primes.push(item)

		val = val/item
		return largestPrime(val, i, primes)

	else:
		i = i+1
		return largestPrime(val, i, primes)


i = 0
val = 600851475143
primes = []
largestPrime(val, i, primes)
print primes