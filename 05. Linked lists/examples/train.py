class Node(object):

	def __init__(self, item):
		self.item = item
		self.next = None

	def set_next(self, item):
		self.next = Node(item)

class LinkedList(object):

	def __init__(self):

		self.head = None

	def append(self, item):
		if not self.head:
			self.head = Node(item)
		else:
			current = self.head
			while current.next:
				current = current.next
			current.set_next(item)

	def length(self):
		if not self.head:
			return 0
		else:
			ans = 1
			current = self.head
			while current.next:
				current = current.next
				ans += 1
			return ans

	def reverse(self):
		current = self.head
		while(current.next):
			t = self.head
			self.head = current.next
			current.next = current.next.next
			self.head.next = t


	def __str__(self):
		current = self.head
		ans = str(current.item)
		while current.next:
			current = current.next
			ans += '-> ' + str(current.item)
			
		return ans


l = LinkedList()
for itm in range(8):
	l.append(itm)

print l

l.reverse()

print l