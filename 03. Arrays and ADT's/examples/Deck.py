import random

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

	def __eq__(self, other):
		return (self.suit_char == other.suit_char and
			self.rank_num == other.rank_num)

	def __lt__(self, other):
		if self.suit_char == other.suit_char:
			return self.rank_num < other.rank_num
		else:
			return self.suit_char < other.suit_char

	def __ne__(self, other):
		return not(self == other)

	def __le__(self, other):
		return self < other or self == other

class Deck(object):

	def __init__(self):
		'''Creates a new Deck object
		post: create a 52-card deck in standard order
		'''
		cards = []

		for suit in Card.SUITS:
			for rank in Card.RANK:
				card = Card(suit, rank)
				cards.append(card)

		self.cards = cards

	def shuffle(self):
		'''Shuffle the deck of cards
		post: randomizes the order of the cards in the deck
		'''
		current_deck = self.cards
		cards = []

		while current_deck != []:
			position = random.randint(0, self.size() - 1)
			card = current_deck.pop(position)

			cards.append(card)

		self.cards = cards

	def size(self):
		'''Crads left
		post: returns the number of cards in self
		'''
		return len(self.cards)

	def deal(self):
		'''Deal a single card
		pre: self <> NULL self.size() > 0
		post: returns the next card in the deck, and removes it from the deck
		'''
		return self.cards.pop()

class Hand(object):

	'''A labeled collection of cards that can be sorted'''

	def __init__(self, label=""):
		'''Creates an empty collection with the given label'''
		self.label = label
		self.cards = []

	def add(self, card):
		'''Add a card to the hand
		ctx: s <- |cards|
		pre: s <- |cards| /\ !(card in cards)
		post: |cards| = s + 1 /\ card min cards
		'''
		self.cards.append(card)

	def sort(self):
		'''Arranges the cards in descending bridge order
		ctx: s <- |cards|
		post: forall i in [0, s - 1] ==> cards[i] <_{bridge} cards[i + 1]
		'''
		self.cards.sort()
		self.cards.reverse()

	def dump(self):
		'''Print the content of the hand'''
		print self.label + "'s Cards:"
		for card in self.cards:
			print "  ", card
