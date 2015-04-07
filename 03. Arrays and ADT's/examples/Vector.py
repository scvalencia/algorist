class Vector(object):

	def __init__(self, dim):
		self.size = dim
		self.last = 0
		self.array = [None for itm in range(dim)]	

	def push(self, item):
		self.array[self.last] = item
		self.last += 1

	def clear(self):
		dim = self.size
		self.last = 0
		self.array = [None for itm in range(dim)]

	def is_complete(self):
		nones = self.array.count(None)
		if nones != 0:
			return False
		else:
			return True

	def get_basis(self):
		if not self.is_complete():
			raise ValueError('vector must be complete')
		ans = []
		dim = self.size

		i = 0
		for j in range(dim):
			item = Vector(dim)

			k = 0
			while k != dim:
				item.push(0)
				k += 1

			item[i] = 1
			i += 1
			ans.append(item)

		return ans

	def __mul__(self, other):
		pass

	def __abs__(self):
		pass

	def __len__(self):
		return len(self.array)

	def __getitem__(self, index):
		return self.array[index]

	def __setitem__(self, j, val):
		self.array[j] = val

	def __add__(self, other):
		if len(self) != len(other):
			raise ValueError('dimensions must agree')

		result = Vector(len(self))

		for i in range(len(self)):
			item = self[i] + other[i]
			result.push(item)

		return result

	def __sub__(self, other):
		pass

	def __eq__(self, other):
		return self.array == other.array

	def __ne__(self, other):
		return self.array != other.array

	def __iadd__(self, other):
		new_vector = self + other
		return new_vector

	def __str__(self):
		ans = '<'
		for i, itm in enumerate(self.array):
			to_add = str(itm)
			if i == len(self) - 1:
				ans += to_add
			else:
				ans += to_add + ', '
		ans += '>'
		return ans

	def __repr__(self):
		return str(self)

class SequenceIterator(object):
	'''
		An iterator for any sequence supporting both __len__, and
		__getitem__
	'''

	def __init__(self, sequence):
		self.__seq = sequence
		self.__k = -1

	def __next__(self):
		self.__k += 1
		if self.__k < len(self.__seq):
			return self.__seq[self.__k]
		else:
			raise StopIteration()

	def __iter__(self):
		return self 

