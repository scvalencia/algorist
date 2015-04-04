'''
	Given a sequence S consisting of n numbers, we want
	to compute a sequence A such that A[j] is the average
	of S[0], S[1], ..., S[j] for j = 0, ..., n - 1

		A[j] = (sum(S, 0, j)) / j + 1

'''

# O(n ** 2)
def prefix_avg1(S):
	n = len(S)
	A = [0 for _ in range(n)]

	for j in range(n):
		total = 0
		for i in range(j + 1):
			total += S[i]
		A[j] = total / (j + 1)

	return A

'''
	T(n) = 1 + n + sum(1 + sum(1, i, j), j, n) = O(n**2)
'''

# O(n ** 2)
def prefix_avg2(S):
	n = len(S)
	A = [0 for _ in range(n)]

	for j in range(n):
		A[j] = sum(S[:j + 1]) / (j + 1)

	return A

# O(n)
def prefix_avg3(S):
	n = len(S)
	A = [0 for _ in range(n)]
	total = 0

	for j in range(n):
		total += S[j]
		A[j] = total / (j + 1)

	return A