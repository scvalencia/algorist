# Code for the exercises in Goodrich, Tamassia, Goldwasser's 
# book on data structures and algorithms in Python

# CHAPTER 3


# CREATIVITY

# C-3.35
def merge_sort(alist):
	# Adapted form: http://interactivepython.org/
    if len(alist) > 1:
        mid = len(alist) // 2

        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i, j, k = 0, 0, 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k]=righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

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

def disjoint3(A, B, C):
	'''
		Assumming: len(A) == len(B) == len(C) = n
		T(n) = 3nlog(n) + n(2log(n)) ~ 5nlog(n) ~ O(nlog(n))
	'''

	merge_sort(A)
	merge_sort(B)
	merge_sort(C)

	for a in A:
		searchB = binary_search(B, a)
		searchC = binary_search(C, a)

		if searchB != -1 and searchC != -1:
			return False			

	return True

# C-3.36