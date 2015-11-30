import ctypes

def sample():
	ArrayType = ctypes.py_object * 5
	slots = ArrayType()
	#print slots[0] # Exception

	for i in range(5):
		slots[i] = None

	slots[0] = 69
	slots[3] = 12
	slots[4] = 43

	for i in range(5):
		print slots[i]

	slots[3] = None

	print '#' * 10

	for i in range(5):
		print slots[i]