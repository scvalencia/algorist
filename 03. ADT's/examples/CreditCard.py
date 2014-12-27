class CreditCard(object):

	def __init__(self, customer, bank, acnt, limit):
		''' Creates a new credit card instance.

		The initial balance is zero
		args:
			customer (string): name of the customer (e.g. 'John Lynch')
			bank (string)    : name of thr bank (e.g 'Bank of San Serriffe')
			acnt (strign)    : account identifier (e.g '12321 343534 454545 43434')
			limit (float)    : credit limit measured in dollars
		'''

		self.customer = customer
		self.bank = bank
		self.acnt = acnt
		self.limit = limit
		self.balance = 0

	def charge(self, price):
		''' Charge given price to the card, assumming sufficient credit limit

		args:
			price (float) : price to be charged

		returns:
			boolean : a flag indicating if the charge was processed
		'''

		new_balance = price + self.balance

		if new_balance > self.limit:
			return False
		else:
			self.balance = new_balance
			return True

	def make_payment(self, amount):
		''' Processes customer payment that reduces balance 

		args:
			amount (float) : the amount of dollars to be removed from
						     the balance

		returns:
			boolean : a flag showing if the transaction was successful
		'''

		new_balance = self.balance - amount

		if new_balance < 0:
			return False
		else:
			self.balance = new_balance
			return True
		