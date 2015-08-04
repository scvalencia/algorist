from time import time
from random import random
from random import choice
import matplotlib.pyplot as plt


def linear_search(collection, target):

	for i in collection:
		if i == target:
			return i

	return -1

def binary_search(collection, target):

	low, high = 0, len(collection) - 1	

	while low <= high:
		mid = (low + high) / 2
		if collection[mid] == target:
			return mid
		elif target < collection[mid]:
			high = mid - 1
		else:
			low = mid + 1

	return -1


def main():

	sizes = [i for i in range(0, 11000, 1000)]
	lists = [sorted([int(1000 * random()) for i in xrange(size)]) for size in sizes if size != 0]
	results = {}
	
	target = 57
	for lst in lists:
		start_time = time()
		linear_search(lst, target)
		linear_time = time() - start_time
		
		start_time = time()
		binary_search(lst, target)
		binary_time = time() - start_time
	

		results[len(lst)] = (linear_time, binary_time)

	linear = {i : results[i][0] for i in results}
	binary = {i : results[i][1] for i in results}

	print 'n \t Linear Search \t Binary Search'
	print '-' * 37

	for itm in sizes[1:]:
		print "%d \t %.8f \t %.8f " % (itm, results[itm][0], results[itm][1])

	plt.bar(linear.keys(), linear.values(), 100, color='g')
	plt.bar(binary.keys(), binary.values(), 100, color='r')
	plt.show()

if __name__ == '__main__':
	main()