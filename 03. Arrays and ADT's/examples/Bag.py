'''
ADT: Bag, 
	represents a simple container to store collection of items (duplicated allowed).
	The items, each of which is individually stored, have no particular order but they
	must be comparable

Bag():
	Creates a bag that is initialli empty

length():
	Returns the number of items stores in the bag. Accessed using len()

contains(item):
	Determines if the given target item is stored in the bag. Accessed using in

add(item):
	Adds the given item to the bag

remove(item):
	Removes and returns an occurrence of item from the bag. An exception is raised
	if the element is not in the bag

iterator():
	Creates and returns an iterator that can be used to iterate over the collection of items
'''

class Bag(object):

	def __init__(self):
		self._body = []

	def __len__(self):
		return len(self._body)

	def __contains__(self, item):
		return item in self._body

	def add(self, item):
		self._body.append(item)

	def remove(self, item):
		assert item in self._body, "The item must be in the bag."
		index = self._body.index(item)
		return self._body.pop(index)

	def __iter__(self):
		return BagIterator(self._body)

class BagIterator(object):

	def __init__(self, lst):
		self._items = lst
		self._current = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self._current < len(self._items):
			item = self._items[self._current]
			self._current += 1
			return item
		else:
			raise StopIteration("error")