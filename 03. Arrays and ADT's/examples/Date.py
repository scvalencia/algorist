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
		self._julian_date = 0
		assert self._is_valid(), "Invalid Gregorian Date"

		tmp = -1 if month < 3 else 0

		self.julian_day =  day - 32075 + (1461 * (year + 4800 + tmp) // 4) + \
			(367 * (month - 2 - tmp * 12) // 12) - \
			(3 * ((year + 4900 + tmp) // 100) // 4)

	def _is_valid(self):
		return True

	def _to_gregorian(self):
		A = self.julian_day + 68569
		B = 4 * A // 146097
		A -= (146097 * B + 3) // 4
		year = 4000 * (A + 1) // 1461001
		A -= (1461 * year // 4) + 31
		month = 80 * A // 2447
		day = A - (2447 * month / 80)
		A = month // 11
		month += 2 - (12 * A)
		year = 100 * (B - 49) + year + A
		return month, day, year

	def __str__(self):
		return ''