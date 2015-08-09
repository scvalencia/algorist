# Code for the exercises in Goodrich, Tamassia, Goldwasser's 
# book on data structures and algorithms in Python

import math
import itertools
import collections

# CHAPTER 3


# CREATIVITY

# C-3.35
def merge_sort(alist):
	# Adapted form: http://interactivepython.org/
	'''
		T(n) ~ 2T(n/2) + n ~ O(nlog(n))
	'''
	if len(alist) > 1:
		mid = len(alist) // 2

       	lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i, j, k = 0, 0, 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k]=righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

def binary_search(collection, target):
	'''
		T(n) ~ T(n/2) + 1 ~ O(log(n))
	'''
	low, high = 0, len(collection) - 1

	while low <= high:
		mid = (low + high) // 2
		if collection[mid] == target:
			return mid
		elif target < collection[mid]:
			high = mid - 1
		else:
			low = mid + 1

	return -1

def disjoint3(A, B, C):
	'''
		Assumming: len(A) == len(B) == len(C) = n
		T(n) = 3nlog(n) + n(2log(n)) ~ 5nlog(n) ~ O(nlog(n))
	'''

	merge_sort(A)
	merge_sort(B)
	merge_sort(C)

	for a in A:
		searchB = binary_search(B, a)
		searchC = binary_search(C, a)

		if searchB != -1 and searchC != -1:
			return False			

	return True

# C-3.36
def kmax_element(A, k = 10):
	'''
		T(n) ~ nlog(n) + 1 ~ nlog(n)
	''' 
	if len(A) < 10:
		return
	else:
		merge_sort(A)
		print A
		i = len(A)
		return A[i - 10]

# C-3.38
'''
	sum(1, n, i^2) = n(n + 1)(n + 2) / 6 ~ O(n^3)
'''

# C-3.41
def min_max(A, low, high):
	'''
		Using Divide, conquer and combine
		Call it as (A, 0, len(A) - 1):
		T(n) ~ n = 2 ? 3 : 2T(n/2) + 2 

		T(n) = 2T(n/2) + 2
			 = 2(2T(n/2^2) + 2) + 2
			 = 2(2(2T(n/2^3) + 2) + 2) + 2
			 = 2(2^2T(n/2^3) + 2^2 + 2) + 2
			 = 2^3T(n/2^3) + 2^3 + 2^2 + 2
			 .
			 .
			 .
			?= 2^(k - 1)T(n/2^(k - 1)) + sum(i = 1, k - 1, 2^i)
			Should be tested using PMI
			Let n = 2^k => k = log2(n) = log(n)

		T(n) = 2^(log(n) - 1)T(2) + 2^(log(n)) - 2 By geometric series
		     = (2^(logn) / 2) + n - 2 
		     = (n / 2) + n - 2
		     = 3n/2 - 2

		     < 3n/2

		Q.E.D

	'''

	if high - low == 1:
		return (min(A[low], A[high]), max(A[low], A[high]))

	mid = int(math.floor((low + high) / 2))
	x1, y1 = min_max(A, low, mid)
	x2, y2 = min_max(A, mid + 1, high)

	minimum, maximum = min(x1, x2), max(y1, y2)

	return (minimum, maximum)

# C-3.42
def count_total_visits(n):
	ans = 0
	for i in range(n + 1):
		ans += i * (i + 1) / 2

	return ans + 1

# C-3.45
def lacking_number(lst, n):
	summation = n * (n - 1) / 2
	accum = 0

	for itm in lst:
		accum += itm

	return summation - accum

# C-3.50
def naive_computation(p, x):
	ans = 0.0

	for i, itm in enumerate(p):
		
		accum = 1.0
		for j in range(i):
			accum *= x

		ans += itm * accum

	return ans

def power(x, n):
	if n == 0: 
		return 1
	if n % 2 == 0:
		m = power(x, n / 2)
		return m * m
	else:
		return x * power(x, n - 1)

def optimized_computation(p, x):

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

# C-3.53
'''
	One should devise an assignation heuristic to ensure
	that all testers share a bottle, there's one bottle 
	that is not tested, and ensure combinations as follows:

	Suppose n = 8.

	Testers = [A, B, C]

	A: 2 5 6 7
	B: 3 5 6 8
	C: 4 6 7 8

	1 : [] 			-> nCr(4, 0)
	2 : [A] 		-> nCr(4, 1)
	3 : [B]
	4 : [C]
	5 : [A, B] 		-> nCr(4, 2)
	6 : [A, C]
	7 : [B, C]
	8 : [A, B, C] 	-> nCr(4, 3)

	If no tester dies, the poisoned bottle was 1.
	If just A dies, 2 was poisoned, if just B dies,
	3 was poisoned, if just C dies, then 4 was poisoned.
	If just A and B dies, 5 was poisoned.
	If just A and C dies, 6 was poisoned.
	If just B and C dies, 7 was poisoned.

	If all of them died, 8 was the poisoned bottle.

	The strategy is to generate the testing table,
	that is assign to each tester some bottles, and
	follow the heuristic.

	If there are 8 bottles, we need 3 tester, log2(8) = 3


'''

def generate_sentence(bottle, testers):
	ans = 'If ' + ', '.join(map(str, testers))
	ans += ' is ' if len(testers) == 1 else ' are '
	ans += 'dead, bottle #' + str(bottle) + ' was poisoned'
	return ans


# http://stackoverflow.com/questions/17434070/generating-all-combinations-of-a-list-in-python
# https://docs.python.org/2/library/itertools.html
# http://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
def wine_testing(n):
	table = {i: [] for i in range(1, n + 1)}
	testers_size = int(math.log(n, 2))
	testers = [i for i in range(1, testers_size + 1)]

	permutations = []

	for i in xrange(testers_size + 1):
		for j in list(itertools.combinations(testers, i)):
			permutations.append(list(j))

	i = 0
	while i < n:
		table[i + 1] = permutations[i]
		i += 1

	print

	for i in range(1, n + 1):
		print i, ' : ', table[i]


# wine_testing(16)