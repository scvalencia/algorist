print 'Welcome to the GPA calculator.'
print 'Please enter all your letter grades, ones per line.'
print 'Enter a blank line to designate the end.'

points = {'A+' : 4.00, 'A' : 4.00, 'A-' : 3.67, 'B+' : 3.33, 'B' : 3.00, 'B-' : 2.67,
		  'C+' : 2.33, 'C' : 2.00, 'D+' : 1.33, 'D' : 1.00, 'F' : 0.0}

num_courses = 0.0
total_points = 0
done = False

while not done:
	grade = raw_input()
	grade = grade.strip()

	if grade == '': done = True
	else:
		num_courses += 1.0
		total_points += points[grade]

if num_courses > 0:
	print 'Your GPA is {0:.3}'.format(total_points / num_courses)