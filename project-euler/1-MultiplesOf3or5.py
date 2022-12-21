def sum(n):
	"""
	Returns the sum of all natural numbers bellow n
	"""
	return n * (n + 1) * 0.5


def multiples3or5(number):
	number -= 1

	sum3  =  3 * sum(number //  3)
	sum5  =  5 * sum(number //  5)
	sum15 = 15 * sum(number // 15)

	soma = sum3 + sum5 - sum15
	
	return soma


a = multiples3or5(1000)
print(a)
