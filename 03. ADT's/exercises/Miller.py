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
			self.num = (num // -common)
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

	def get_common_denominator(self, other):
		new_self = (self.num * other.den, self.den * other.den)
		new_other = (other.num * self.den, other.den * self.den)

		return (new_self, new_other)

	def mod(self):
		return self.num % self.den

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

	# Pogramming exercises 7
	def __radd__(self, other):
		return self + other

	# Pogramming exercises 8
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

	# Pogramming exercises 9
	def __repr__(self):
		return str(self)
