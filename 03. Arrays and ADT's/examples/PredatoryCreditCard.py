from CreditCard import CreditCard

class PredatoryCreditCard(CreditCard):
	''' An extension to CreditCard that compounds interests and fees. '''

	def __init__(self, customer, bank, acnt, limit, apr):
		''' Create a new predatory credit card instance.

		The initial balance is zero.

		customer 	the name of the customer (e.g., 'Sebastian Valencia')
		bank 		the name of the bank (e.g., 'California Savings')
		acnt 		the account identifier (e.g., '5391 0375 9387 5309')
		limit 		credit limit (measured in dollars)
		apr 		annual percentage rate (e.g., 0.0825 for 8.25 APR)
		'''

		CreditCard.__init__(self, customer, bank, acnt, limit)
		self.apr = apr

	def charge(self, price):
		''' Charge given price to the card, assuming sufficient
			credit limit.

		Return True if charge was processed
		Return False and assess $5 fee if charge is denied
		'''

		success = CreditCard.charge(self, price)
		if not success:
			self.balance += 5
		return success

	def process_month(self):
		''' Assess monthly interest on outstanding balance.'''
		if self.balance > 0:
			monthly_factor = pow(1 + self.apr, 1/12)
			self.balance *= monthly_factor