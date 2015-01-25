def fact(n):
	ans = 1
	if n < 2: 
		ans = 1
	else:
		i = 1
		while i != n + 1:
			ans = ans * i
			i += 1
	return ans

facts = [fact(i) for i in range(20)]

def solve(n):
	org = n
	summation = 0
	ans = []

	j = 0

	while n > 0:
		i = 1
		while facts[i - 1] < n: 
			i = i + 1
		ans.append(i)
		summation = summation + facts[i]
		print summation
		n = n - facts[i]
		print n

		j += 1

		if j == 10: break



	return ans

print solve(42)

