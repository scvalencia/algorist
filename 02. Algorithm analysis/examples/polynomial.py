import math

# O(n^2)
def compute1(p, x):
	ans = 0.0

	for i, itm in enumerate(p):
		
		accum = 1.0
		for j in range(i):
			accum *= x

		ans += itm * accum

	return ans

# O(log(n))
def power(x, n):
	if n == 0: 
		return 1
	if n % 2 == 0:
		m = power(x, n / 2)
		return m * m
	else:
		return x * power(x, n - 1)

# O(n * log(n))
def compute2(p, x):

	ans = 0.0

	for i, itm in enumerate(p):
		ans += itm * power(x, i)

	return ans

# O(n)
def horner(p, x):
	'''
		Given p(x) = a + bx + c^2 + dx^3
		p(x) = a + x(b + x(c + dx))

		t1 = d
		t1 = t1 * x
		t1 = t1 + c
		t1 = t1 * x
		t1 = t1 + b
		t1 = t1 * x
		t1 = t1 + a

		t1 = p(x)
	'''
	
	i = len(p) - 1
	t1 = p[i]

	while i > 0:
		t1 = t1 * x + p[i - 1]
		i -= 1

	return t1

p1 = [-1, 2, -6, 2]
p2 = [9, 7, 5, 3, 1]

print compute1(p1, 3)
print compute2(p1, 3)
print horner(p1, 3)

print compute1(p2, 3)
print compute2(p2, 3)
print horner(p2, 3)