def gcd(m, n):

	while m % n != 0:
		oldm = m
		oldn = n

		m = oldn
		n = oldm % oldn

	return n

class Fraction(object):	

	def __init__(self, top, bottom):

		self.num = top
		self.den = bottom

	def __add__(self, other):

		new_num = self.num * other.den + self.den * other.num
		new_den = self.den * other.den
		common = gcd(new_num, new_den)

		return Fraction(new_num // common, new_den // common)

	def __eq__(self, other):

		firstnum = self.num * other.den
		secondnum = other.num * self.den

		return firstnum == secondnum

	def __str__(self):
		return str(self.num) + "/" + str(self.den)

	def __repr__(self):
		return str(self)