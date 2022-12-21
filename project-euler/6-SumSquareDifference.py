def sum(n):
	return n * (n + 1) * 0.5


def weird_sum(n):
	a = 0
	b = 1

	sum = 0 
	while a <= n:
		sum += a**2 + b**2
		a += 1
		b += 1

	return sum

def square_of_the_sum(n):
	return sum(n) ** 2


def sum_of_the_squares(n):
	return ((n**2) * (n-2) - 2*n) * 0.5 + weird_sum(n/2) 


res = sum_of_the_squares(10)
#res = weird_sum(
print(res)
