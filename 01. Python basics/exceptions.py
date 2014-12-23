age = -1
while age <= 0:
	try:
		age = int(raw_input('Enter your age in years: '))
		if age <= 0:
			print 'Age must be positive.'
	except ValueError:
		print 'This is an invalid age specification.'
	except EOFError:
		print 'Unexpected error reading input'