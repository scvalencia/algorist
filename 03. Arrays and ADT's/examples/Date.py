'''
ADT: Date, represents a Date in the gregorian calendar

Date(month, day, year): 
	Creates a new Date instance initialized to the given Gregorian date which must be valid. 
	Year 1 BC and earlier are indicated by negative year components.

day(): 
	Returns the Gregorian day number of this date.

month(): 
	Returns the Gregorian month number of this date.

year(): 
	Returns the Gregorian year of this date.

monthName(): 
	Returns the Gregorian month name of this date.

dayOfWeek(): 
	Returns the day of the week as a number between 0 and 6 with 0 representing Monday 
	and 6 representing Sunday.

numDays(otherDate): 
	Returns the number of days as a positive integer be- tween this date and the otherDate.

isLeapYear(): 
	Determines if this date falls in a leap year and returns the appropriate boolean value.􏰂
􏰂
advanceBy(days): 
	Advances the date by the given number of days. The date is incremented if days is positive 
	and decremented if days is negative. The date is capped to November 24, 4714 BC, if necessary.

comparable(otherDate): 
	Compares this date to the otherDate to deter- mine their logical ordering. 
	This comparison can be done using any of the logical operators <, <=, >, >=, ==, !=.

toString (): 
	Returns a string representing the Gregorian date in the format mm/dd/yyyy. 
	Implemented as the Python operator that is automatically called via the str() constructor.

'''

class Date(object):

	def __init__(self, month, day, year):
		self.day = day
		self.month = month
		self.year = year

		print day, month, year

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