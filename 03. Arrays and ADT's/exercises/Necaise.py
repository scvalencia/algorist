# Code for the exercises in Necaise's
# book on data structures and algorithms using Python

import sys
import math
import time
import random
import datetime

# CHAPTER 1

# EXERCISES

# E-1.01

class Date(object):

	def __init__(self, month, day, year):
		self.day = day
		self.month = month
		self.year = year

		leap = self.is_leap()

		self.days_per_month = {1 : 31, 2 : 29 if leap else 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 
			7 : 31, 8 : 31, 9 : 30 , 10 : 31 , 11 : 30 , 12 : 21}

		assert self.valid(), "Invalid gregorian date"

		a = math.floor((14.0 - self.month) / 12.0)
		y = self.year + 4800 - a
		m = self.month + 12 * a - 3

		self.julian_day = int(self.day + math.floor((153 * m + 2) / 5.0) + (365 * y) + \
							math.floor(y / 4.0) - math.floor(y / 100.0) + \
							math.floor(y / 400.0) - 32045)

	def valid(self, month = None, day = None, year = None):
		if month == None: 
			month = self.month
		if day == None: 
			day = self.day
		if year == None: 
			year = self.year

		valid_month = month in self.days_per_month.keys()
		valid_day = valid_month and day in range(1, self.days_per_month[month] + 1)
		valid_year = valid_day and year >= 0

		return valid_year

	def month_name(self):
		months = ['', 'January', 'February', 'March', 'April', 'May', \
					'June', 'July', 'August', 'September', 'October', 'November', 'December']

		return months[self.month]

	def day_of_week(self):
		y = self.year - (14 - self.month) / 12
		x = y + y / 4 - y / 100 + y / 400
		m = self.month + 12 * ((14 - self.month) / 12) - 2
		d = (self.day + x + (31 * m) / 12) % 7

		days = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']

		return d, days[d]

	def num_days(self, other):
		return abs(other.julian_day - self.julian_day)

	def is_leap(self):
		leap = 0 if (self.year % 4 == 1) or ((self.year % 100 == 0) and
			(self.year % 400 == 1)) else 1

		return leap

	def next(self):
		if self.valid(self.month, self.day + 1, self.year):
			return Date(self.month, self.day + 1, self.year)
		elif self.valid(self.month + 1, 1, self.year):
			return Date(self.month + 1, 1, self.year)
		else:
			return Date(1, 1, self.year + 1)

	def advance(self, days):
		current = self.next()
		while self.num_days(current) != days:
			current = current.next()
		return current

	def __str__(self):
		return ('0' + str(self.day) if self.day < 10 else str(self.day)) + \
				'-' + ('0' + str(self.month) if self.month < 10 else str(self.month)) + '-' + str(self.year)

	def __eq__(self, arg_date):
		return self.julian_day == arg_date.julian_day

	def __lt__(self, arg_date):
		return self.julian_day < arg_date.julian_day

	def __le__(self, arg_date):
		return self.julian_day <= arg_date.julian_day

def date_handler():
	date1 = Date(9, 11, 2015)
	date2 = Date(9, 11, 2016)
	print date1.julian_day
	print date1.num_days(date2)
	print date1
	print date1.next()
	print date1.advance(300)

# E-1.02

class Date02(Date):

	def __init__(self, month, day, year):
		Date.__init__(self, month, day, year)

	def day_of_week_name(self):
		d, string = self.day_of_week()
		days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
		return days[d]

	def day_of_year(self):
		init = Date(1, 1, self.year)
		return init.num_days(self) + 1

	def is_weekday(self):
		d, string = self.day_of_week()
		return d in [1, 2, 3, 4, 5]

	def as_gregorian(self, divchar = '/'):
		return ('0' + str(self.day) if self.day < 10 else str(self.day)) + \
				divchar + ('0' + str(self.month) if self.month < 10 else str(self.month)) + \
				divchar + str(self.year)

def date02_handler():
	date = Date02(9, 11, 2015)
	print date.day_of_week_name()
	print date.day_of_year()
	print date.is_weekday()
	print date.as_gregorian('-') 

# E-1.03

def print_calendar(date):
	month = date.month_name()
	year = date.year

	init = Date(date.month, 1, year)
	day = init.day_of_week()[0]

	print (month + ' ' + str(year)).center(20)
	print 'Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'

	pos = [i for i in range(1, 7 - day + 1)]
	pre = [' ' for i in range(7 - len(pos))]

	tpl = pre + pos
	row = tuple([i * 2 if i == ' ' else i for i in tpl])


	print "%2s %2s %2s %2s %2s %2s %2s" % row

	last = tpl[-1]
	stop = date.days_per_month[date.month]

	while last < stop:
		row = ()
		tpl = [i for i in range(last + 1, last + 1 + 7)]
		if stop in tpl:
			row = tuple(map(lambda x : x if x <= stop else ' ', tpl))
		else:
			row = tuple([i * 2 if i == ' ' else i for i in tpl])

		print "%2s %2s %2s %2s %2s %2s %2s" % row

		last += 7

def print_calendar_handler():
	date = Date(9, 11, 2015)
	print_calendar(date)

# E-1.04

class Date03(Date02):

	def __init__(self, month = 0, day = 0, year = 0):
		if month == day == year == 0:
			date = datetime.datetime.now()

			month = date.month
			day = date.day
			year = date.year

		Date02.__init__(self, month, day, year)

def date03_handler():
	date = Date03()
	print date

# PROJECTS

# P-1.01

'''
ClickCounter ADT

A model of a small hand-held device that contains a push button and a count display.
To increment the counter, the button is pushed and thw new count shows in the display

	ClickCounter() : Creates a new ClickCounter display instance

	push() : Increment the count and display it

	display() : Shows the current count

	reset() : Sets the counter to zero

'''

class ClickCounter(object):

	def __init__(self):
		self.click = 0
		self.display()

	def push(self):
		self.click += 1
		self.display()

	def display(self):
		print self.click

	def reset(self):
		self.click = 0
		self.display()

def click_counter_handler():
	cc = ClickCounter()
	time.sleep(2)
	cc.push()
	time.sleep(2)
	cc.push()
	time.sleep(2)
	cc.reset()

# P-1.02

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

	def next(self):
		if self._current < len(self._items):
			item = self._items[self._current]
			self._current += 1
			return item
		else:
			raise StopIteration("error")

class GrabBag(Bag):

	def __init__(self):
		Bag.__init__(self)

	def grab_item(self):
		index = random.randint(0, len(self) - 1)
		return self._body.pop(index)

def grab_bag_handler():
	gb = GrabBag()
	gb.add(1)
	gb.add(8)
	gb.add(9)

	for itm in gb:
		print itm,

	print
	print gb.grab_item()

	for itm in gb:
		print itm,

# P-1.03

class CountingBag(Bag):

	def __init__(self):
		Bag.__init__(self)

	def num_of(self, item):
		occurrences = 0

		for itm in self:
			if itm == item:
				occurrences += 1

		return occurrences

def counting_bag_handler():
	cb = CountingBag()
	cb.add(1)
	cb.add(8)
	cb.add(9)
	cb.add(1)

	print cb.num_of(1)

# P-1.04

class StudentRecord(object):

	def __init__(self, student_id, first_name, last_name, year, gpa):
		self._year_dct = {1 : 'Freshman', 2 : 'Sophomore', 3 : 'Junior', 4 : 'Senior'}
		self.id = student_id
		self.first_name = first_name
		self.last_name = last_name
		self.year = self._year_dct[year]
		self.gpa = gpa

class StudentFileReader(object):

	def __init__(self, file_name):
		self._file_name = file_name
		self._file_object = None

	def open(self):
		self._file_object = open(self._file_name, 'r')

	def close(self):
		self._file_object.close()
		self._file_object = None

	def _fetch_one(self):
		line = self._file_object.readline()
		if line == "":
			return None

		student_id, first_name, last_name, year, gpa = tuple(map(lambda x : x.replace(' ', ''), line.split(',')))
		student_id = int(student_id)
		year = int(year)
		gpa = float(gpa)

		student = StudentRecord(student_id, first_name, last_name, year, gpa)
		return student

	def fetch_all(self):
		records = []

		student = self._fetch_one()

		while student != None:
			records.append(student)
			student = self._fetch_one()

		return records

def students_record_handler():

	sfr = StudentFileReader('students.txt')
	sfr.open()
	students = sfr.fetch_all()
	sfr.close()

	students.sort(key = lambda s : s.id)

	print 'LIST OF STUDENTS'.center(50)
	print 
	print "%-5s %-25s %-10s %-4s" % ('ID', 'NAME', 'CLASS', 'GPA')
	print "%5s %25s %10s %4s" % ('-' * 5, '-' * 25, '-' * 10, '-' * 4)

	for student in students:
		print '%5d %-25s %-10s %4.2f' % (student.id, student.last_name + ', ' + student.first_name,
			student.year, student.gpa)

	print '-' * 47
	print 'Number of students: ', len(students)

# P-1.05

class StudentFileWriter(object):

	def __init__(self, records):
		self.records = records

	def sort_records(self, key, descending = False):
		if key == 'sid':
			self.records.sort(key = lambda student : student.id)
		elif key == 'fname':
			self.records.sort(key = lambda student : student.first_name)
		elif key == 'lname':
			self.records.sort(key = lambda student : student.last_name)
		elif key == 'year':
			self.records.sort(key = lambda student : student.year)
		elif key == 'gpa':
			self.records.sort(key = lambda student : student.gpa)

		if descending:
			self.records.reverse()

	def write_to_file(self, file_name):
		file_object = open(file_name, 'w')

		file_object.write('LIST OF STUDENTS\n'.center(50))
		file_object.write('\n')
		file_object.write("%-5s %-25s %-10s %-4s\n" % ('ID', 'NAME', 'CLASS', 'GPA'))
		file_object.write("%5s %25s %10s %4s\n" % ('-' * 5, '-' * 25, '-' * 10, '-' * 4))

		for student in self.records:
			file_object.write('%5d %-25s %-10s %4.2f\n' % (student.id, student.last_name + ', ' + student.first_name,
				student.year, student.gpa))

		file_object.write('-' * 47 + '\n') 
		file_object.write('Number of students: ' +  str(len(self.records)) + '\n')

		file_object.close()


	def print_to_terminal(self):
		print 'LIST OF STUDENTS'.center(50)
		print 
		print "%-5s %-25s %-10s %-4s" % ('ID', 'NAME', 'CLASS', 'GPA')
		print "%5s %25s %10s %4s" % ('-' * 5, '-' * 25, '-' * 10, '-' * 4)

		for student in self.records:
			print '%5d %-25s %-10s %4.2f' % (student.id, student.last_name + ', ' + student.first_name,
				student.year, student.gpa)

		print '-' * 47
		print 'Number of students: ', len(self.records)

def student_file_writer_handler():
	sfr = StudentFileReader('students.txt')
	sfr.open()
	students = sfr.fetch_all()
	sfr.close()

	print '=' * 70
	print 'Welcome to the SUR system, a system for generating reports on'
	print 'Smalltown University students.'
	print

	print 
	key = raw_input('Enter the sorting key: sid, fname, lname, year, gpa: ')
	key = key.strip()
	assert key in ['sid', 'fname', 'lname', 'year', 'gpa']
	print

	asc = input('Write (1) if you want the report in descending order, (2) otherwise: ')

	print 
	output_file = input('Enter the output file: (1) file, (2) terminal: ')
	assert output_file in [1, 2], "Invalid option"

	sfw = StudentFileWriter(students)
	sfw.sort_records(key, True if asc == 1 else False)

	file_name = ''
	if output_file == 1:
		print 
		file_name = raw_input('Enter the file name: ')
		sfw.write_to_file(file_name)

	else:
		sfw.print_to_terminal()

	print '=' * 70

# P-1.06

'''
Time ADT

A simple ADT to represent the time of the day, for any 24-hour period,
as the number of seconds that have elapsed since midnight

	Time(hour, minutes, seconds): Creates a new Time instance and initializes 
	it with the given time.

	hour(): Returns the hour part of the time.

	minutes(): Returns the minutes part of the time.

	seconds(): Returns the seconds part of the time.

	numSeconds(otherTime): Returns the number of seconds as a positive 
	integer between this time and the otherTime.

	isAM(): Determines if this time is ante meridiem or before midday 
	(at or before 12 o'clock noon).

	isPM(): Determines if this time is post meridiem or after midday (after
	12 o'clock noon).

	comparable(otherTime): Compares this time to the otherTime to determine their 
	logical ordering. This comparison can be done using any of the Python logical operators.

	toString(): Returns a string representing the time in the 12-hour format hh:mm:ss. 
	Invoked by calling Python's str() constructor.

'''

# P-1.07 Boring

# P-1.08

'''
Line ADT

An ADT to represent a line segment in \mathbb{R}^2

	LineSegment(ptA, ptB): Creates a new Line Segment instance defined by the two Point objects.

	endPointA(): Returns the first endpoint of the line.

	endPointB(): Returns the second endpoint of the line.

	length(): Returns the length of the line segment given as the Euclidean distance 
	between the two endpoints.

	toString(): Returns a string representation of the line segment in the format (Ax, Ay)#(Bx, By).

	isVertical(): Is the line segment parallel to the y-axis?

	isHorizontal(): Is the line segment parallel to the x-axis?

	isParallel(otherLine): Is this line segment parallel to the otherLine?

	isPerpendicular(otherLine): Is this line segment perpendicular to the otherLine?

	intersects(otherLine): Does this line segment intersect the otherLine?

	bisects(otherLine): Does this line segment bisect the otherLine?

	slope(): Returns the slope of the line segment given as the rise over the run. If the line 
	segment is vertical, None is returned.

	shift(xInc, yInc): Shifts the line segment by xInc amount along the x-axis and yInc amount 
	along the y-axis.

	midpoint(): Returns the midpoint of the line segment as a Point object.

'''

class Point(object):

	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)
 
def orientation(p0, p1, p2):
 	x1 = p1.x - p0.x
 	y1 = p1.y - p0.y
 	x2 = p2.x - p0.x
 	y2 = p2.y - p0.y

 	det = x1 * y2 - x2 * y1

 	return (0 if det == 0 else (1 if det > 0 else 2))

def onsegment(p0, p1, p2):
	if p2.x >= min(p0.x, p1.x) and p2.x <= max(p0.x, p1.x):
		return 1
	return 0

class LineSegment(object):

	EPSILON = 0.00003

	def __init__(self, point_a, point_b):
		self.point_a = point_a
		self.point_b = point_b

	def end_pointa(self):
		return self.point_a

	def end_pointb(self):
		return self.point_b

	def length(self):
		length = math.sqrt((self.point_a.x - self.point_b.x) ** 2 + \
			(self.point_a.y - self.point_b.y) ** 2)

		return length

	def slope(self):
		return (self.point_b.y - self.point_a.y) / (self.point_b.x - self.point_a.x)

	def is_parallel(self, other):
		return self.slope() == other.slope()

	def is_perpendicular(self, other):
		return self.slope() * other.slope() in [-1 - self.EPSILON, -1 + self.EPSILON]

	def is_vertical(self, other):
		return self.slope == 0.0

	def is_horizontal(self, other):
		return self.is_parallel(LineSegment(Point(1, 1), Point(-1, 1)))

	def intersects(self, other):

		p1, q1 = self.point_a, self.point_b
		p2, q2 = self.point_b, self.point_b

		o1 = orientation(p1, q1, q2)
		o2 = orientation(p1, q1, p2)
		o3 = orientation(p2, q2, p1)
		o4 = orientation(p2, q2, q1)

		if o1 != o2 and o3 != o4:
			return True

		if(o1 == o2 == o3 == o4 == 0):
			if(onsegment(p1, q1, p2) or onsegment(p1, q1, q2)):
				return True

		return False

	def __str__(self):
		return "(%.2f, %.2f)#(%.2f, %.2f)" % \
			(self.point_a.x, self.point_a.y, self.point_b.x, self.point_b.y)


def linesegment_handler():
	p1 = Point(-1, 4)
	p2 = Point(2, -2)

	l = LineSegment(p1, p2)
	print l.length()
	print l.slope()
	print l.is_vertical(l)

	p1 = Point(1, 1)
	q1 = Point(10, 1)
	p2 = Point(1, 3)
	q2 = Point(10, 2)

	l1 = LineSegment(p1, q1)
	l2 = LineSegment(p2, q2)

	print l1.intersects(l2)

# P-1.09

'''
Polygon ADT

An ADT to represent a polygon in \mathbb{R}^2. A polygon is a plane figure that is bounded 
by a finite chain of straight line segments closing in a loop to form a closed chain or 
circuit. These segments are called its edges or sides, and the points where two edges meet 
are the polygon's vertices (singular: vertex) or corners. The interior of the polygon is 
sometimes called its body. An n-gon is a polygon with n sides. A polygon is a 2-dimensional 
example of the more general polytope in any number of dimensions.

	Polygon(points): creates a polygon given a set of points

	sides(): returns the number of sides of the polygon

	area(): returns the area of the polygon

	perimeter(): returns the perimeter of the polygon

	triangulation(): returns the minimum cost polygon triangulation

		A triangulation of a convex polygon is formed by drawing diagonals between non-adjacent 
		vertices (corners) such that the diagonals never intersect. The problem is to find the 
		cost of triangulation with the minimum cost. The cost of a triangulation is sum of the 
		weights of its component triangles. Weight of each triangle is its perimeter 
		(sum of lengths of all sides)

	inside(point): return True if the point lies inside the polygon

	bounds(): returns a rectangular bound for the perimeter

	string(): returns a string representation of a polygon

	save(filename): saves the polygon to a file

	scale(pxx): returns a scaled version of the polygon

	draw: returns HTML code with thw draw of the polygon 

'''

# P-1.10

# P-1.11

class Fraction(object):

	def __init__(self, num, den = 1):

		common = self.gcd(num, den)

		if type(den) != int or type(den) != int:
			raise ValueError("Values must be integers")

		if den == 0:
			raise ValueError("Division by Zero")

		if num < 0 or den < 0:
			self.num = (num // -common)
			self.den = den // common

		else:
			self.num = num // common
			self.den = den // common

	def get_num(self):
		return self.num

	def get_den(self):
		return self.den

	def gcd(self, a, b):
		if b == 0: 
			return a
		else:
			return self.gcd(b, a % b)

	def get_common_denominator(self, other):
		new_self = (self.num * other.den, self.den * other.den)
		new_other = (other.num * self.den, other.den * self.den)

		return (new_self, new_other)

	def mod(self):
		return self.num % self.den

	def is_unit(self):
		return self.num == 1

	def __add__(self, other):
		new_num = self.num * other.den + self.den * other.num
		new_den = self.den * other.den

		return Fraction(new_num, new_den)

	def __sub__(self, other):
		new_num = self.num * other.den - self.den * other.num
		new_den = self.den * other.den

		return Fraction(new_num, new_den)

	def __mul__(self, other):
		new_num = self.num * other.num
		new_den = self.den * other.den

		return Fraction(new_num, new_den)

	def __div__(self, other):
		new_num = self.num * other.den
		new_den = self.den * other.num

		return Fraction(new_num, new_den)

	def __gt__(self, other):
		self_tuple, other_tuple = self.get_common_denominator(other)
		return self_tuple[0] > other_tuple[0]

	def __ge__(self, other):
		self_tuple, other_tuple = self.get_common_denominator(other)
		return self_tuple[0] >= other_tuple[0]

	def __lt__(self, other):
		self_tuple, other_tuple = self.get_common_denominator(other)
		return self_tuple[0] < other_tuple[0]

	def __le__(self, other):
		self_tuple, other_tuple = self.get_common_denominator(other)
		return self_tuple[0] <= other_tuple[0]

	def __radd__(self, other):
		return self + other

	def __iadd__(self, other):
		new_fraction = self + other
		self = new_fraction

		return self

	def __isub__(self, other):
		new_fraction = self - other
		self = new_fraction

		return self

	def __imul__(self, other):
		new_fraction = self * other
		self = new_fraction

		return self

	def __idiv__(self, other):
		new_fraction = self / other
		self = new_fraction

		return self

	def __ne__(self, other):
		num_eq = self.num != other.num
		den_eq = self.den != other.den

		return num_eq and den_eq		

	def __eq__(self, other):
		num_eq = self.num == other.num
		den_eq = self.den == other.den

		return num_eq and den_eq

	def __abs__(self):
		new_num = abs(self.num)
		new_den = abs(self.den)

		return Fraction(new_num, new_den)

	def __str__(self):
		if self.den == 1:
			return str(self.num)
		else:
			return str(self.num) + "/" + str(self.den)

	def __repr__(self):
		return str(self)

	def __float__(self):
		number = (self.num + 0.0) / (self.den)
		return float(number)

	def __int__(self):
		number = (self.num + 0.0) / (self.den)
		return int(number)

def fraction_handler():
	pass

######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################

def main():
	menu = {'e-01-01' : date_handler, 'e-01-02' : date02_handler, 'e-01-03' : print_calendar_handler, \
		'e-01-04' : date03_handler, 'p-01-01' : click_counter_handler, 'p-01-02' : grab_bag_handler, \
		'p-01-03' : counting_bag_handler, 'p-01-04' : students_record_handler, \
		'p-01-05' : student_file_writer_handler, 'p-01-08' : linesegment_handler}
	
	if sys.argv[1] in menu:
		foo = menu[sys.argv[1]]
		foo()

	else:
		print 'Wrong exercise'

######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################	

if __name__ == '__main__':
	main()