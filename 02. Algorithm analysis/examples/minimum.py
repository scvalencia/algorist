def min_quadratic(lst):
	n = len(lst)
	ans = lst[0]
	for i in range(n):
		for j in range(i + 1, n):
			ans = min(min(lst[i], lst[j]), ans)

	return ans

def min_linear(lst):
	ans = lst[0]
	for itm in lst:
		ans = min(ans, itm)

	return ans