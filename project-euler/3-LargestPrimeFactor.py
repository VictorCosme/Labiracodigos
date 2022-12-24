def largestPrimeFactor(number):
	factors = []
	
	f = 2
	while f <= number:
		if number % f == 0:
			factors.append(f)
			number //= f
		f += 1

	return factors

a = largestPrimeFactor(1_600_851_475_143)
print(a)
