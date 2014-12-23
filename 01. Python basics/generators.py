def factors1(n):
	for k in range(1, n + 1):
		if n % k == 0:
			yield k

def factors2(n):
	k = 1
	while k * k < n:
		if n % k == 0:
			yield k
			yield n // k
		k = k + 1

		if k * k == n:
			yield k

def fibonacci():
	a = 0
	b = 1
	while True:
		yield a
		temp = a + b
		a = b
		b = temp

def main():
	FACTORS = False

	if FACTORS:

		for factor in factors1(100):
			print factor

	else:

		for i in fibonacci():
			print i
			if i > 10000000: break		

main()