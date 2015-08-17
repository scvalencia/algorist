class Range(object):

	def __init__(self, start, stop = None, step = 1):

		if step == 0:
			raise ValueError('step cannot be zero')

		if stop is None:
			start, stop = 0, start

		self.__length = max(0, (stop − start + step − 1) // step)

		self.__start = start
		self.__step = step

	def __len__(self):
		return self.__length

	def __getitem__(self, k):
		if k < 0:
			k += len(self)

		if not 0 <= k < self.__length:
			raise IndexError('index out of range')

		return self.__start + k * self.__step