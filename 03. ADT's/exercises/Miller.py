class Fraction(object):

	def __init__(self, num, den):

		common = self.gcd(num, den)

		if den == 0:
			raise ValueError("Division by Zero")

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

	def __sub__(self, other):
		pass

	def __mul__(self, other):
		pass

	def __truediv__(self, other):
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

	def __repr__(self):
		return str(self)
