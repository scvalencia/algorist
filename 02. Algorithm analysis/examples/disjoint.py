def binary_search(collection, target):

	low, high = 0, len(collection) - 1

	while low <= high:
		mid = (low + high) // 2
		if collection[mid] == target:
			return mid
		elif target < collection[mid]:
			high = mid - 1
		else:
			low = mid + 1

	return -1

# O(|A|log(|A|) + ... + |A| * (log(|B||C|))
def disjoint3(A, B, C):

	A.sort()
	B.sort()
	C.sort()

	for a in A:
		searchB = binary_search(B, a)
		searchC = binary_search(C, a)

		if searchB != -1 and searchC != -1:
			return False			

	return True


a = [1, 2, 3, 4]
b = [5, 7]
c = [9, 6, 8]

#print set(a).intersection(b).intersection(c)

print disjoint3(a, b, c)

a = [2, 3, 4, 1, 7, 8]
b = [5, 1, 7]
c = [9, 6, 1, 8, 7]

#print set(a).intersection(b).intersection(c)

print disjoint3(a, b, c)