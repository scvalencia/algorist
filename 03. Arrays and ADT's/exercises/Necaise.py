# Code for the exercises in Necaise's
# book on data structures and algorithms using Python

import math
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

# E-1.04

class Date03(Date02):

	def __init__(self, month = 0, day = 0, year = 0):
		if month == day == year == 0:
			date = datetime.datetime.now()

			month = date.month
			day = date.day
			year = date.year

		Date02.__init__(self, month, day, year)

# PROJECTS

# P-1.01

# P-1.02

# P-1.03

# P-1.04

# P-1.05

# P-1.06

# P-1.07

# P-1.08

# P-1.09

# P-1.10

# P-1.11

def main():
	d = Date03()
	print_calendar(d)
	

if __name__ == '__main__':
	main()