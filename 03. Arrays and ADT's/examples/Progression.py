class Progression(object):
	''' Iterator introducing a generic Progression

	Default iterator produces the sequence 0, 1, 2, 3, ...
	'''

	def __init__(self, start =  0):
		''' Initialize current to the first term of the progression'''
		self.current = start

	def advance(self):
		''' Update self.current to a new value.

		This should be oerwritten by a subclass to customize progression.

		By convention, if current is set to None, this designates the end
		of a finite progression.
		'''

		self.current += 1

	def __next__(self):
		''' Returns the next element, or else raise StopIteration error'''
		if self.current is None:
			raise StopIteration()
		else:
			answer = self.current
			self.advance()
			return answer

	def __iter__(self):
		''' An iterator must return itself as an iterator.'''
		return self

	def print_progression(self, n):
		''' Print the next n values in the progression. '''
		print ' '.join(str(self.__next__()) for j in range(n))

class ArithmeticProgression(Progression):
	''' Iterator producing an arithmetic progression.'''

	def __init__(self, step = 1, start = 0):
		''' Create a new arithmetic progression.

		step 	the fixed constant to add to each term
		start   the first term of the progression
		'''

		Progression.__init__(self, start)
		self.step = step

	def advance(self):
		''' Update current calue by adding the fixed step. '''
		self.current += self.step

class GeometricProgression(Progression):
	''' Iterator producing a geometric progression.'''

	def __init__(self, base = 2, start = 1):
		''' Create a new geometric progression.

			base 	the fixed constant each term is multiplied by.
			start 	the first term of the progression.

		'''

		Progression.__init__(self, start)
		self.base = base

	def advance(self):
		''' Update current value by multiplying if by the base value.'''
		self.current *= self.base

class FibonacciProgression(Progression):
	''' Iterator producing a generalized Fibonacci progression.'''

	def __init__(self, first = 0, second = 1):
		''' Create a new fibonacci progression.

		first 	the first term of the progression
		second  the  second term of the progression
		'''

		Progression.__init__(self, first)
		self.prev = second - first

	def advance(self):
		''' Update current value by taking the sum of the previous two.'''
		self.prev, self.current = self.current, self.prev + self.current

class TriangularProgression(Progression):
	''' Iterator producing the Triangular Number sequence. '''

	def __init__(self):

		Progression.__init__(self, 0)
		self.term = 1

	def advance(self):
		self.current = self.current + self.term
		self.term += 1

class SquareProgression(Progression):
	''' Iterator producing the Triangular Number sequence. '''

	def __init__(self):

		Progression.__init__(self, 0)
		self.term = 1

	def advance(self):
		''' Update current value by taking the square of the current term. '''
		self.current = self.term * self.term
		self.term += 1
	

class PrimeProgression(Progression):
	''' Iterator producing a sequence of prime numbers. '''

	def __init__(self):

		Progression.__init__(self, 2)

	def is_prime(self, n):
		if n <= 1: return False
		elif n <= 3: return True
		elif n % 2 == 0 or n % 3 == 0:
			return False

		i =  5
		while i * i <= n:
			if n % i == 0 or n % (i + 2) == 0:
				return False
			i = i + 6

		return True

	def next_prime(self, n):
		i = n + 1
		while not self.is_prime(i):
			i += 1

		return i

	def advance(self):
		self.current = self.next_prime(self.current)

class AbundantProgression(Progression):
	''' Iterator producing a sequence of abundant numbers. '''

	def __init__(self):

		Progression.__init__(self, 12)

	def divisors_sum(self, number):
		i, ans = 1, 0
		while i < number:
			if number % i == 0:
				ans += i
			i += 1

		return ans

	def next_number(self, n):
		i = n + 1
		while i >= self.divisors_sum(i):
			i += 1

		return i

	def advance(self):
		self.current = self.next_number(self.current)