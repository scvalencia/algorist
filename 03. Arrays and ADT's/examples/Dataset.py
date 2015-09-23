import math

class Dataset(object):

	def __init__(self):
		self.data = []
		self.size = 0

	def add(self, x):
		self.data.append(x)
		self.size = self.size + 1

	def size(self):
		return self.size

	def min(self):
		i = 0
		n = self.size
		ans = self.data[i]

		while i < n:
			if self.data[i] < ans:
				ans = self.data[i]
			i = i + 1

		return ans

	def max(self):
		i = 0
		n = self.size
		ans = self.data[i]

		while i < n:
			if self.data[i] > ans:
				ans = self.data[i]
			i = i + 1

		return ans

	def average(self):		
		i = 0		
		ans = 0.0
		n = self.size

		while i < n:
			ans = ans + self.data[i]
			i = i + 1

		ans = ans / (n + 0.0)
		return ans

	def std_deviation(self):
		i = 0
		ans = 0
		n = self.size
		miu = self.average()

		while i < n:
			ans = ans + (self.data[i] - miu) ** 2
			i = i + 1

		ans = ans * (1.0 / n)
		ans = math.sqrt(ans)

		return ans