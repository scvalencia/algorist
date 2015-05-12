# Code for the exercises in Goodrich, Tamassia, Goldwasser's 
# book on data structures and algorithms in Python

import re
import pickle
import random
import urllib2
from xml.dom import minidom
from bs4 import BeautifulSoup

# CHAPTER 2

# PROJECTS

# P-2.33

commands = ['']

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
		''' Evaluation using the Horner rule '''
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

def parse_polynomial(polynomial, variable = 'x'):
	parse = re.compile("[+|-]").split(polynomial)
	for i, itm in enumerate(parse):
		parse[i] = itm.strip()

	polynomial = polynomial.replace(' ', '')

	signs = []
	for itm in polynomial:
		if itm in ['+', '-']:
			signs.append(itm)

	for i, itm in enumerate(parse):
		if itm == '':
			parse.pop(i)

	if len(parse) != len(signs):
		print 'Error while parsing polynomial'

	number = ''
	power = ''
	sign = ''

	dct = []

	for itm in parse:
		if variable in itm:
			index = itm.index(variable)
			number = itm[0:index]
			power = itm[index+2:]
			if power == '': power = '1'
		else:
			number = itm
			power = '0'

		dct.append((power, number))

	ans = []

	for itm in dct:
		sign = signs.pop(0)
		ans.append((itm[0], eval(sign + itm[1])))

	return ans

def tokenize_polynomial(tokens):
	degree = -1
	dct = {}
	for itm in tokens:
		deg = eval(itm[0])
		if deg > degree:
			degree = deg
		if deg in dct:
			dct[deg] = itm[1] + dct[deg]
		else:
			dct[deg] = itm[1]

	polynomial = [0 for _ in range(degree + 1)]
	
	for itm in dct:
		polynomial[itm] = dct[itm]

	return polynomial

def main():
	env = {}

	while True:
		command = raw_input('>> ')
		if '=' in command:
			parse = command.split('=')
			name = parse[0]
			tokens = parse_polynomial(parse[1])
			coefficients = tokenize_polynomial(tokens)
			polynomial = Polynomial(coefficients)
			env[name] = polynomial

		elif 'LET' in command:
			parse = command.split()
			if len(parse) != 5:
				print 'Error while parsing LET expression'
			else:
				recipent = parse[1]
				op1 = parse[2]
				sign = parse[3]
				op2 = parse[4]

				if op1 not in env:
					print 'Name ', op1, ' is not defined'
				elif op2 not in env:
					print 'Name ', op2, ' is not defined'
				else:
					op1 = env[op1]
					op2 = env[op2]

					if sign in ['+', '-', '*', '/', '|']:
						if sign == '+':
							env[recipent] = op1 + op2
						elif sign == '-':
							env[recipent] = op1 - op2
						elif sign == '*':
							env[recipent] = op1 * op2
						elif sign == '/':
							env[recipent] = op1 / op2
						elif sign == '|':
							env[recipent] = op1 % op2
					else:
						print 'Error while parsing LET expression'
						print 'Unsuported operator: ', sign


		elif 'EVAL' in command:
			parse = command.split()
			if len(parse) != 3:
				print 'Error while parsing EVAL expression'
			else:
				op1 = parse[1]
				value = parse[2]
				try:
					value = float(value)
				except Exception:
					print 'Type of ', value, ' must be numeric'

				if op1 not in env:
					print 'Name ', op1, ' is not defined'
				else:
					op1 = env[op1]
					print op1.eval(value)


		elif 'DIFF' in command:
			parse = command.split()

			if len(parse) == 2:
				op1 = parse[1]

				if op1 not in env:
					print 'Name ', op1, ' is not defined'
				else:
					op1 = env[op1]
					print op1.derivate()

			elif len(parse) == 3:
				op1 = parse[1]
				value = parse[2]
				try:
					value = float(value)
				except Exception:
					print 'Type of ', value, ' must be numeric'

				if op1 not in env:
					print 'Name ', op1, ' is not defined'
				else:
					op1 = env[op1]
					print op1.derivate(value)

			else:
				print 'Error while parsing DIFF expression'


		elif 'INT' in command:
			parse = command.split()

			if len(parse) == 2:
				op1 = parse[1]

				if op1 not in env:
					print 'Name ', op1, ' is not defined'
				else:
					op1 = env[op1]
					print op1.integrate()

			elif len(parse) == 4:
				op1 = parse[1]
				value1 = parse[2]
				value2 = parse[3]
				try:
					value1 = float(value1)
				except Exception:
					print 'Type of ', value1, ' must be numeric'

				try:
					value2 = float(value2)
				except Exception:
					print 'Type of ', value2, ' must be numeric'
				
				if op1 not in env:
					print 'Name ', op1, ' is not defined'
				else:
					op1 = env[op1]
					print op1.integrate(value1, value2)

			else:
				print 'Error while parsing INT expression'

		elif '+' in command:
			parse = command.split()
			if len(parse) != 3:
				print 'Error while parsing expression'
			else:
				op1 = parse[0]
				op2 = parse[-1]

				if op1 not in env:
					print 'Name ', op1, ' is not defined'
				elif op2 not in env:
					print 'Name ', op2, ' is not defined'
				else:
					op1 = env[op1]
					op2 = env[op2]

					print op1 + op2

		elif '-' in command:
			parse = command.split()
			if len(parse) != 3:
				print 'Error while parsing expression'
			else:
				op1 = parse[0]
				op2 = parse[-1]

				if op1 not in env:
					print 'Name ', op1, ' is not defined'
				elif op2 not in env:
					print 'Name ', op2, ' is not defined'
				else:
					op1 = env[op1]
					op2 = env[op2]

					print op1 - op2

		elif '*' in command:
			parse = command.split()
			if len(parse) != 3:
				print 'Error while parsing expression'
			else:
				op1 = parse[0]
				op2 = parse[-1]

				if op1 not in env:
					print 'Name ', op1, ' is not defined'
				elif op2 not in env:
					print 'Name ', op2, ' is not defined'
				else:
					op1 = env[op1]
					op2 = env[op2]

					print op1 * op2

		elif '/' in command:
			print 'Unsuported operator'

		elif '|' in command:
			print 'Unsuported operator'

		elif 'QUIT' in command:
			break

		else:
			if command in env:
				print env[command]
			else:
				print 'Name ', command, ' is not defined'

# P-2.34

def frequencies(text):
	dct = {}

	for ch in text:
		if ch in dct:
			dct[ch] += 1
		else:
			dct[ch] = 1

	for itm in dct:
		print itm, ' : ', '*' * dct[itm]

# P-2.35

class Person(object):

	def __init__(self, name):
		self.name = name
		self.packets = []

	def send_packet(self, who, packet):
		who.add_packet(packet)

	def add_packet(self, packet):
		self.packets.append(packet)

	def read_packet(self):
		if len(self.packets) != 0:
			print self.packets.pop(-1)

class Process(object):

	def __init__(self):
		self.queue = []

	def add_packet(self, packet):
		self.queue.append(packet)


def simulate():
	alice = Person('Alice')
	bob = Person('Bob')

	p = Process()

	i = 0
	while i < 5:
		packets = ['Hi', 'Bob']
		for itm in packets:
			p.add_packet(itm)
			bob.add_packet(itm)
			bob.read_packet()
		i += 1

# P-2.36

def simulation1(size):

	class Bear(object):

		def __init__(self):
			self.type = 'Bear'

		def __repr__(self):
			return 'Bear'

	class Fish(object):

		def __init__(self):
			self.type = 'Fish'

		def __repr__(self):
			return 'Fish'

	river = [None for _ in range(size)]

	def populate():
		i = 0
		while i < size:
			rndm = random.randint(1, 3)
			if rndm == 1:
				river[i] = Bear()
			elif rndm == 2:
				river[i] = Fish()
			else:
				river[i] = None
			i += 1

	def run():
		i = 1
		while i < size - 1:
			rndm = random.choice(['L', 'R'])
			next = i - 1 if rndm == 'L' else i + 1

			if river[i] != None and river[next] != None:
				if river[i].type == river[next].type:
					new = Fish() if river[i].type == 'Fish' else Bear()
					nones = map(lambda x : x == None, river)
					flag = False; j = 0
					while not flag:
						j = random.choice([_ for _ in range(len(nones))])
						if j == True: flag = True
						river[j] = new

				else:
					if river[i].type == 'Fish':
						river[i] = None
					else: 
						river[next] = None 

			i += 1

	populate()
	run()
	print river


# P-2.37

def simulation2(size):

	class Bear(object):

		def __init__(self, gender, strength):
			self.type = 'Bear'
			self.gender = gender
			self.strength = strength

		def __repr__(self):
			return 'Bear'

	class Fish(object):

		def __init__(self, gender, strength):
			self.type = 'Bear'
			self.gender = gender
			self.strength = strength

		def __repr__(self):
			return 'Fish'

	river = [None for _ in range(size)]

	def populate():
		i = 0
		while i < size:
			rndm = random.randint(1, 3)
			gender = random.choice([True, False])
			strength = random.choice([_ for _ in range(90)])
			if rndm == 1:
				river[i] = Bear(gender, strength)
			elif rndm == 2:
				river[i] = Fish(gender, strength)
			else:
				river[i] = None
			i += 1

	def run():
		i = 1
		while i < size - 1:
			rndm = random.choice(['L', 'R'])
			next = i - 1 if rndm == 'L' else i + 1

			if river[i] != None and river[next] != None:
				if river[i].type == river[next].type:
					if river[i].gender != river[next].gender:
						gender = random.choice([True, False])
						strength = random.choice([_ for _ in range(90)])
						new = Fish(gender, strength) if river[i].type == 'Fish' else Bear(gender, strength)
						nones = map(lambda x : x == None, river)
						flag = False; j = 0
						while not flag:
							j = random.choice([_ for _ in range(len(nones))])
							if j == True: flag = True
							river[j] = new
					else:
						if river[i].strength < river[next].strength:
							river[i] = None
						else: 
							river[next] = None 


				else:
					if river[i].type == 'Fish':
						river[i] = None
					else: 
						river[next] = None 

			i += 1

	populate()
	run()
	print river

# P-2.38

class Book(object):

	def __init__(self, title, author, link, price, book_id):
		self.id = book_id
		self.title = title
		self.author = author
		self.link = link
		self.price = price
		self.text = None

	def get(self):
		response = urllib2.urlopen(self.link)
		text = response.read()
		self.text = text.split('\n')

	def display(self):
		response = urllib2.urlopen(self.link)
		text = response.read()
		text = text.split('\n')
		return text

	def flush(self):
		self.text = None

	def __repr__(self):
		ans = ''
		ans += 'AUTHOR: ' + self.author + '\n'
		ans += 'TITLE: ' + self.link + '\n'
		return ans

	def __str__(self):
		ans = ''
		ans += 'ID: ' + str(self.id) + '\n'
		ans += 'AUTHOR: ' + self.author + '\n'
		ans += 'TITLE: ' + self.title + '\n'
		return ans

class EbookReader(object):
	''' Basic ebook reader '''

	def __init__(self):
		self.books = []
		self.money = 0.0

	def add_money(self, amount):
		self.money += amount

	def search_books(self):

		book_author = ''
		book_title = ''
		book_link = ''
		book_price = random.randint(0, 25)

		def get_url(url):
			response = urllib2.urlopen(url)
			text = response.read()
			text = text.split('\n')
			return text

		def fetch_authors():
			url = 'http://www.textfiles.com/etext/AUTHORS/'

			authors = {}

			for itm in get_url('http://www.textfiles.com/etext/AUTHORS/'):
				if 'HREF' in itm:
					y = BeautifulSoup(itm)
					authors[str(y.tr.td.tab.b.text)] = str(y.tr.td.b.a.text)

			dct = {}
			i = 1
			for itm in authors:
				print "{:0>2d}".format(i),
				print itm

				dct[i] = itm

				i += 1

			author = raw_input('Select the number of the author: ')
			author = int(author)

			book_author = dct[author]

			return authors[book_author], book_author


		def fetch_books_per_author(author):
			url = 'http://www.textfiles.com/etext/AUTHORS/' + author + '/'

			books = {}

			for itm in get_url(url):
				if 'HREF' in itm:
					y = BeautifulSoup(itm)
					books[str(y.tr.td.tab.td.br.td.text).strip()] = str(y.tr.td.a.text)

			dct = {}
			i = 1
			for itm in books:
				print "{:0>2d}".format(i),
				print itm

				dct[i] = itm

				i += 1

			book = raw_input('Select the number of the book: ')
			book = int(book)

			book_title = dct[book]
			book_link = url + books[book_title]

			return book_title, book_link
					

		author, book_author = fetch_authors()
		book_title, book_link = fetch_books_per_author(author)

		print 'Want to buy ', book_title, ' by ', book_author, '?'
		print 'Your money: ', self.money
		print 'Price: ', book_price

		ans = raw_input('Y/N? ')

		if ans.upper() == 'Y':
			book_object = Book(book_title, book_author, book_link, book_price, len(self.books))
			self.buy_book(book_object)

	def buy_book(self, book):
		if self.money >= book.price:
			self.money -= book.price
			self.books.append(book)

	def read_book(self, book_id):
		lst = self.books[book_id].display()
		for itm in lst:
			print itm

	def list_books(self):
		for itm in self.books:
			print itm

	def add_money(self, ammount):
		self.money += ammount

def handler():
	pkl_file = open('data.pkl', 'rb')
	e = pickle.load(pkl_file)
	output = open('data.pkl', 'wb')
	e.add_money(800)

	# A Menu for the e-book
	while True:

		print '= ' * 30
		print '01. List books.'
		print '02. Buy book.'
		print '03. Read book.'
		print '04. View money.'
		print '05. Add money.'
		print '06. Quit.'

		option = raw_input('>> ')
		option = int(option)

		print '= ' * 30 

		if option == 1:
			e.list_books()

		elif option == 2:
			e.search_books()

		elif option == 3:
			e.list_books()

			option = input('Which book to read: ')

			e.read_book(option)

		elif option == 4:
			print e.money

		elif option == 5:
			money = input('Money: ')
			e.add_money(money)

		else:
			break


	pickle.dump(e, output)
	output.close()

def P2_30():
	handler()


# P-2.39

class Polygon(object):
	pass

def main():
	P2_30()

if __name__ == '__main__':
	main()