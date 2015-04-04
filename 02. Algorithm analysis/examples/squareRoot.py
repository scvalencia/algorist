def squareRootExhaustive(x, epsilon):
	step = epsilon * 2
	ans = 0.0
	while abs(ans ** 2 - x) >= epsilon and ans <= max(x, 1):
		ans += step
	return ans

def squareRootBinary(x, epsilon):
	low = 0.0
	high = max(1.0, x)
	ans = (low + high) / 2.0

	while abs(ans ** 2 - x) >= epsilon:

		if ans ** 2 < x:
			low = ans
		else:
			high = ans

		ans = (high + low) / 2.0

	return ans

print squareRootExhaustive(25, 0.0001)
print squareRootBinary(25, 0.0001)