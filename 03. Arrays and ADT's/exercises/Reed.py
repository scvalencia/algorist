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

# P-2.5

# P-2.6

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

# P-2.8

# P-2.9

# P-2.10

# P-2.11

# P-2.12

def main():
	p2_4()

if __name__ == '__main__':
	main()