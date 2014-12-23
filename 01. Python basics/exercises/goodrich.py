# Code for the exercises in Goodrich, Tamassia, Goldwasser's 
# book on data structures and algorithms in Python


# REINFORCEMENT

# R-1.1
def is_multiple(n, m):
	return n % m == 0

# R-1.2
def even(k):
	return is_multiple(k, 2)

# R-1.3
def minmax(data):
	ans_min, ans_max = data[0], data[0]
	for itm in data:
		if itm > ans_max:
			ans_max = iym
		if itm < ans_min:
			ans_min = itm
	return ans_min, ans_max

# R-1.4
def funny_sum(n):
	ans = 0
	i = 0
	while i < n:
		ans += i * i
		i += 1
	return ans

# R-1.5
def short_funny_sum(n):
	return sum([i * i for i in xrange(n)])

# R-1.6
def sum_odds(n):
	ans = 0
	i = 0
	while i < n:
		if i % 2 == 1:
			ans += i * i
		i += 1
	return ans

# R-1.7
def short_sum_odds(n):
	return sum([i * i for i in xrange(n) if i % 2 == 1])

# R-1.8
def negative_index():
	data = list(xrange(100))
	for i in xrange(1, 100):
		assert data[100 - i], data[-i]

# R-1.9
def sequence_1():
	print range(50, 90, 10)

# R-1.10
def sequence_2():
	print range(8, -9, -2)

# R-1.11
def sequence_3():
	print [2 ** i for i in range(9)]

# R-1.12
def choice(data):
	from random import randrange
	return data[randrange(0, len(data))]

# CREATIVITY

# C-1.13
def reverse(data):
	length = len(data)
	ans = [None for _ in xrange(length)]
	for i in range(length):
		ans[i] = data[(length - 1) - i]
	return ans

# C-1.14
def odd_product(data):
	ans = False
	for i in xrange(len(data)):
		for j in xrange(len(data)):
			if i != j and data[i] != data[j]:
				if data[i] * data[j] % 2 == 1: 
					ans = True
					break
	return ans

# C-1.15
def distinct1(data):
	return len(data) == len(set(data))

def distinct2(data):
	ans = True
	for i in xrange(len(data)):
		for j in xrange(len(data)):
			if i != j:
				if data[i] == data[j]:
					ans = False
					break
	return ans

# C-1.16, numeric values are immutable, but not the variables refering to them

# C-1.17, val is a result from an iteration, not an actual reference to the val in list

# C-1.18
def increasing():
	return [i * (i + 1) for i in xrabge(0, 10)]

# C-1.19
def alphabeth():
	return [chr(i) for i in range(97, 123)]

# C-1.20
def shuffle(data):
	import random
	ans = []
	while data:
		index = random.randint(0, len(data) - 1)
		ans.append(data[index])
		data.pop(index)
	return ans

# C-1.21
def reverse_lines(data):
	ans = []
	try:
		while True:
			ans.append(raw_input())
	except:
		ans.reverse()
		for itm in ans:
			print itm

# C-1.22
def dot_product(a, b):
	n = len(a)
	return [a[i] * b[i] for i in range(n)]

# C-1.23
def buffer_overflow():
	lst = [2, 3, 5, 6, 8, 2, 0]
	try:
		lst[100] = 1
	except IndexError:
		print 'Don\'t try buffer overflow attacks in Python!'

# C-1.24
def num_vowels(param):
	vowels = ['a', 'e', 'i', 'o', 'u']
	vowels += map(lambda y : y.upper, vowels)
	return len(filter(lambda x : x in vowels, param))

# C-1.25
def remove_punctuation(sentence):
	from string import punctuation
	ans = ''
	for itm in sentence:
		if itm not in punctuation:
			ans += itm
	return ans

# C-1.26 Boring stuff

# C-1.27
def factors(n):
	buff = []
	k = 1
	while k * k < n:
		if n % k == 0:
			yield k
			buff.append(n // k)
		k = k + 1

		if k * k == n:
			yield k

	while buff:
		yield buff.pop()

# C-1.28
def norm(v, p = 2):
	ans = 0.0
	return reduce(lambda a, b : a + b, map(lambda i : i ** p, v)) ** (1 / (p + 0.0))

# PROJECTS

# P-1.29

# P-1.30

# P-1.31

# P-1.32

# P-1.33

# P-1.34

# P-1.35

# P-1.36