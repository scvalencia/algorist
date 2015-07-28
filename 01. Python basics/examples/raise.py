def sqrt(n):
	if not isinstance(n, (int, float)):
		raise TypeError('n must be numeric')
	elif n < 0:
		raise ValueError('n cannot be negative')
	xn = 1
	xn1 = (xn + n/xn)/2
	while abs(xn1 - xn) > 1:
		xn = xn1
		xn1 = (xn + n/xn)/2
	while xn1*xn1 > n:
		xn1 -= 1
	if isinstance(n, int):
		return int(xn1)
	elif isinstance(n, float):
		return xn1 + 0.0