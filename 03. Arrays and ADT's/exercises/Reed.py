# Code for the exercises in Reed, Zelle's
# book on data structures and algorithms in Python and C++

import random
from tabulate import tabulate

# CHAPTER 2

# PROGRAMMING EXERCISES

# P-2.1, P-2.2

'''
ADT Card:
	A simple playying card. A card is characterized by two components:
	rank: an integer value between 1 and 13, inclusive (Ace-King)
	suit: a character in 'cdhs' for clubs, diamonds, hearts and
		  spades.

Operations:

	create(rank, suit):
		Create a new card
		pre: rank in [1 - 13] /\ suit in {'c', 'd', 'h', 's'}
		post: returns a Card of the gicen rank and suit

	suit():
		Card suit
		post: returns Card's suit as a single character

	rank():
		Card rank
		post: returns Card's rank as an integer

	suitName():
		Card suit suit
		post: returns one of {'clubs', 'diamonds', 'hearts', 'spades'}
		      corresponding to Card's suit

	rankName():
		Card rank name
		post: returns one of {'ace', 'two', ..., 'king'} corresponding 
			  to Card's rank

	__str__():
		String representation od Card
		post: returns string naming of Cards, e.g. 'Ace of Spades'

'''

class Card(object):

	SUITS = 'cdhs'
	SUIT_NAMES = ['clubs', 'diamonds', 'hearts', 'spades']
	RANK = range(1, 14)
	RANK_NAMES = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 
				'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

	def __init__(self, suit, rank):
		self.rank_num = rank
		self.suit_char = suit

	def suit(self):
		return self.suit_char

	def rank(self):
		return self.rank_num

	def suit_name(self):
		index = self.SUITS.index(self.suit_char)
		return self.SUIT_NAMES[index]

	def rank_name(self):
		index = self.RANK.index(self.rank_num)
		return self.RANK_NAMES[index]

	def __str__(self):
		return self.rank_name() + ' of ' + self.suit_name()

# P-2.3

class Deck(object):

	def __init__(self):
		self.cards = []

		for suit in 'cdhs':
			for rank in range(1, 14):
				card = Card(suit, rank)
				self.cards.append(card)

	def deal(self):
		index = random.randint(0, len(self.cards))
		card = self.cards.pop(index)
		return card

	def cards_left(self):
		return len(self.cards)

def p2_3():
	deck = Deck()
	print deck.deal()

# P-2.4

class Player(object):

	def __init__(self, identifier):
		self.id = identifier
		self.hand = []
		self.points = 0
		self.bet = 1

	def get_points(self):
		ans = 0

		for card in self.hand:
			if card.rank() in range(2, 11):
				ans += card.rank()
			elif card.rank() in [11, 12, 13]:
				ans += 10
			elif card.rank() == 1:
				if ans > 10: 
					ans += 1
				else: 
					ans += 11

		self.points = ans

	def add_card(self, card):
		self.hand.append(card)

	def bet(self):
		self.bet += 1

	def clear(self):
		self.hand = []
		self.points = 0
		self.bet = 0

	def get_choice(self):
		print 'Pedir (1) o Plantar (2)'
		ans = input()
		return ans

	def report(self):
		headers = ['cards']
		table = [[str(_)] for _ in self.hand]
		print 'P' + str(self.id)	
		print tabulate(table, headers, tablefmt="fancy_grid")

	def __str__(self):
		return 'P' + str(self.id)

def blackjack():
	deck = Deck()
	n = input('Number of players: ')
	players = [Player(_ + 1) for _ in range(n)]
	crupier = Player(n + 1)

	for player in players:
		player.add_card(deck.deal())

	crupier.add_card(deck.deal())

	for player in players:
		player.add_card(deck.deal())

	for player in players:
		player.report()

	crupier.report()

	for player in players:
		print str(player) + ' Juega'
		while player.get_choice() == 1 and player.bet > 0:
			player.add_card(deck.deal())
			player.get_points()
			player.report()

			if player.points > 21:
				print str(player) + ' Pierde'
				player.bet = 0
	
	while crupier.points <= 17:		
		crupier.add_card(deck.deal())
		crupier.get_points()
		crupier.report()

	cp = crupier.points

	for player in filter(lambda x : x.bet != 0, players):
		if player.points < cp:
			player.bet = 0
		else:
			player.bet += 1

	for player in players:
		print player, player.points, player.bet

def p2_4():
	blackjack()

# P-2.5, i don't know how  to play Solitaire

# P-2.6, i don't know how  to play Solitaire

# P-2.7

class Dataset(object):

	def __init__(self):
		self.data = []
		self.size = 0

	def add(self, x):
		self.data.append(x)
		self.size = self.size + 1

	def size(self):
		return self.size

	def min(self):
		i = 0
		n = self.size
		ans = self.data[i]

		while i < n:
			if self.data[i] < ans:
				ans = self.data[i]
			i = i + 1

		return ans

	def max(self):
		i = 0
		n = self.size
		ans = self.data[i]

		while i < n:
			if self.data[i] > ans:
				ans = self.data[i]
			i = i + 1

		return ans

	def average(self):		
		i = 0		
		ans = 0.0
		n = self.size

		while i < n:
			ans = ans + self.data[i]
			i = i + 1

		ans = ans / (n + 0.0)
		return ans

	def std_deviation(self):
		i = 0
		ans = 0
		n = self.size
		miu = self.average()

		while i < n:
			ans = ans + (self.data[i] - miu) ** 2
			i = i + 1

		ans = ans * (1.0 / n)
		ans = math.sqrt(ans)

		return ans

# P-2.8, TODO

# P-2.9, TODO

# P-2.10

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

# P-2.11

def find_great_smallest_unit_fraction(fraction):
	lst = [Fraction(1, i) for i in range(2, fraction.den + 1)]
	maximum = Fraction(1, fraction.den)

	for frc in lst:
		if frc < fraction and frc > maximum:
			maximum = frc

	return maximum

def egyptian_fraction():
	num = input('Numerator: ')
	den = input('Denominator: ')

	ans = []

	fraction = Fraction(num, den)
	while not fraction.is_unit():
		sub = find_great_smallest_unit_fraction(fraction)
		fraction = fraction - sub
		ans.append(sub)

	ans.append(fraction)

	print Fraction(num, den), '=', ans[0],

	for frc in ans[1:]:
		print '+', frc,

# P-2.12

class Polynomial(object):
	''' A class representing a polynomial in the form ax^n + ... + d '''

	def __init__(self, coeffs, variable = 'x'):
		self.degree = len(coeffs)
		self.coeffs = coeffs
		self.variable = variable

	def __repr__(self):

		def repr_power(variable, power):
			if power == 0:
				return ''
			elif power == 1:
				return variable
			else:
				return variable + '^' + str(power)
		
		ans = ''
		i = self.degree - 1
		for itm in reversed(self.coeffs):
			if itm != 0:
				ans += '+' if itm > 0 else ''
				ans += str(itm) + repr_power(self.variable, i)
			i -= 1

		return ans

	def __str__(self):
		return self.__repr__()

	def __add__(self, other):
		max_polynomial = other if other.degree > self.degree else self
		min_polynomial = other if other.degree < self.degree else self

		old_degree = min_polynomial.coeffs
		new_padding = min_polynomial.padding(max_polynomial.degree)

		ans = None

		ans_coeffs = []

		i = 0
		while i < max_polynomial.degree:
			a = max_polynomial.coeffs[i]
			b = new_padding[i]
			ans_coeffs.append(a + b)
			i += 1

		ans = Polynomial(ans_coeffs)
		return ans
		

	def __sub__(self, other):
		max_deg = other.degree if other.degree > self.degree else self.degree
		
		ans = None

		a_coeffs = self.padding(max_deg)
		b_coeffs = other.padding(max_deg)

		ans_coeffs = []

		i = 0
		while i < max_deg:
			a = a_coeffs[i]
			b = b_coeffs[i]
			ans_coeffs.append(a - b)
			i += 1

		ans = Polynomial(ans_coeffs)
		return ans

	def __mul__(self, other):
		
		new_deg = self.degree + other.degree
		new_coeffs = [0 for _ in range(new_deg - 1)]

		max_polynomial = other if other.degree > self.degree else self
		min_polynomial = other if other.degree < self.degree else self

		for i, itm1 in enumerate(max_polynomial.coeffs):
			for j, itm2 in enumerate(min_polynomial.coeffs):
				deg = i + j
				new_coeffs[deg] += itm1 * itm2

		ans = Polynomial(new_coeffs)
		return ans

	def __div__(self, other):
		pass

	def eval(self, point):
		i = self.degree - 1
		t1 = self.coeffs[i]

		while i > 0:
			t1 = t1 * point + self.coeffs[i - 1]
			i -= 1

		return t1

	def derivate(self, point = None):

		ans = None
		new_coeffs = [0 for _ in range(self.degree - 1)]

		i = 0
		for itm in self.coeffs[1:]:
			new_coeffs[i] = (i + 1) * itm
			i += 1

		ans = Polynomial(new_coeffs)
		
		if point:
			result = ans.eval(point)
			ans = Polynomial([result])

		return ans

	def integrate(self, lower_bound = None, upper_bound = None):
		
		ans = None
		new_coeffs = [0 for _ in range(self.degree + 1)]

		i = 0
		for itm in self.coeffs:
			new_coeffs[i + 1] = itm / (i + 1.0)
			i += 1

		ans = Polynomial(new_coeffs)
		
		if lower_bound and upper_bound:
			a = ans.eval(upper_bound)
			b = ans.eval(lower_bound)
			ans = Polynomial([a - b])

		return ans

	def padding(self, size):
		lst = [0 for _ in range(size  -self.degree)]
		return self.coeffs + lst

def main():
	egyptian_fraction()

if __name__ == '__main__':
	main()