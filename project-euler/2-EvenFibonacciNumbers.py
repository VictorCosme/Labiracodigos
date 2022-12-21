a = 0
b = 2

soma = 2
while 4*b + a <= 4000000:
	c = 4*b + a
	a, b = b, c

	soma += c

print(soma)
