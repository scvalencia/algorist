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
	''' Iterator producing a geometric progression. '''

	def __init__(self, base = 2, start = 1):
		''' Create a new geometric progression.

			base 	the fixed constant each term is multiplied by.
			start 	the first term of the progression.

		'''

		Progression.__init__(self, start)
		self.base = base

	def advance(self):
		''' Updates current value by multiplying if by the base value.'''
		self.current *= self.base

class FibonacciProgression(Progression):

	def __init__(self, first = 0, second = 1):



