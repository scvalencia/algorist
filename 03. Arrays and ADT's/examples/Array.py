'''
Array ADT

A one-dimensional array is a collection of contiguous elements in 
which individual elements are identified by a unique integer subscript 
starting with zero. Once an array is created, its size cannot be changed.

	Array(size) : Creates a one-dimensional array consisting of size elements with each element 
				  initially set to None. size must be greater than zero.

	length() : Returns the length or number of elements in the array.

	get(index) : Returns the value stored in the array at element position index. 
	                 The index argument must be within the valid range. Accessed using 
	                 the subscript operator.

	set(index, value) : Modifies the contents of the array element at po-sition index 
							 to contain value. The index must be within the valid range. 
							 Accessed using the subscript operator.

	clear(value) : Clears the array by setting every element to value.
'''

import ctypes

class Array(object):

	def __init__(self, size):
		assert size > 0, "Array size must be > 0"
		self.size = size
		array_type = ctypes.py_object * self.size
		self.slots = array_type()

		self.clear(None)

	def __len__(self):
		return self.size

	def __getitem__(self, index):
		assert index >= 0 and index < len(self), "Array subscript out of range"
		return self.slots[index]

	def __setitem__(self, index, value):
		assert index >= 0 and index < len(self), "Array subscript out of range"
		self.slots[index] = value

	def clear(self, value):
		i = 0
		while i < self.size:
			self.slots[i] = value
			i += 1

	def __iter__( self ):
		return ArrayIterator(self.slots)

class ArrayIterator(object):

	def __init__(self, slots): 
		self.array_reference = slots 
		self.current = 0

	def __iter__( self ):
		return self

	def __next__( self ):
		if self.current < len(self.array_reference) :
			entry = self.array_reference[self.currentº] 
			self.current += 1
			return entry
		else :
			raise StopIteration