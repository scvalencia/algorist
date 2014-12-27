class Vector(object):

	def __init__(self, size):
		self.size = size
		self.last = 0
		self.array = [None for itm in range(size)]

	

	def add(self, item):
		self.array[self.last] = item
		self.last += 1

	def __getitem__(self, index):
		return self.array[index]

	def __add__(self, other):
		new_size = self.size + other.size
		new_vector = Vector(new_size)

		i = 0
		for itm in self.array:
			new_vector.array[i] = itm
			i += 1

		for itm in other.array:
			new_vector.array[i] = itm
			i += 1

		return new_vector

	def __iadd__(self, other):
		new_vector = self.add(other)
		self = new_vector

	def __len__(self):
		return len(self.array)

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
