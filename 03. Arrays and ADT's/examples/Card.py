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

def main():

	for suit in 'cdhs':
		for rank in range(1, 14):
			card = Card(suit, rank)
			print card

if __name__ == '__main__':
	main()





