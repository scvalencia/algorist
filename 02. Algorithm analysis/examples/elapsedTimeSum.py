def linear_sum(n):
	ans = 0
	i = 1

	while i <= n:
		ans += i
		i += 1

	return ans

def constant_sum(n):
	return n * (n + 1) / 2