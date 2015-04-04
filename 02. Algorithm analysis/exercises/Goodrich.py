# Code for the exercises in Goodrich, Tamassia, Goldwasser's 
# book on data structures and algorithms in Python

import math

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

