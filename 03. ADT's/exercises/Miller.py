class Fraction(object):

	def __init__(self, num, den = 1):

		common = self.gcd(num, den)

		# Pogramming exercises 5
		if type(den) != int or type(den) != int:
			raise ValueError("Values must be integers")

		if den == 0:
			raise ValueError("Division by Zero")

		# Pogramming exercises 6
		if num < 0 or den < 0:

			# Pogramming exercises 2
			self.num = -num // common
			self.den = den // common

		else:

			# Pogramming exercises 2
			self.num = num // common
			self.den = den // common

	# Pogramming exercises 1
	def get_num(self):
		return self.num

	def get_den(self):
		return self.den

	def gcd(self, a, b):
		if b == 0: 
			return a
		else:
			return self.gcd(b, a % b)

	def __add__(self, other):
		new_num = self.num * other.den + self.den * other.num
		new_den = self.den * other.den

		return Fraction(new_num, new_den)

	# Pogramming exercises 3
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

	# Pogramming exercises 4
	def __gt__(self, other):
		pass

	def __ge__(self, other):
		pass

	def __lt__(self, other):
		pass

	def __le__(self, other):
		pass

	def __ne__(self, other):
		pass

	def __eq__(self, other):
		num_eq = self.num == other.num
		den_eq = self.den == other.den

		return num_eq and den_eq

	def __str__(self):
		if self.den == 1:
			return str(self.num)
		else:
			return str(self.num) + "/" + str(self.den)

	# Pogramming exercises 9
	def __repr__(self):
		return str(self)
