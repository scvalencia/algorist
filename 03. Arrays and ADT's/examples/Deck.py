class Deck(object):

	def __init__(self):
		'''Creates a new Deck object
		post: create a 52-card deck in standard order
		'''

	def shuffle(self):
		'''Shuffle the deck of cards
		post: randomizes the order of the cards in the deck
		'''

	def size(self):
		'''Crads left
		post: returns the number of cards in self
		'''

	def deal(self):
		'''Deal a single card
		pre: self <> NULL self.size() > 0
		post: returns the next card in the deck, and removes it from the deck
		'''