class LogicGate(object):

	def __init__(self, name):

		self.label = name
		self.image = ''
		self.output = None

	def get_label(self):

		return self.label

	def get_output(self):

		self.output = self.perform_logic()
		return self.output

class BinaryGate(LogicGate):

	def __init__(self, name):

		LogicGate.__init__(self, name)

		self.pin1 = None
		self.pin2 = None

	def set_pin1(self, value):

		if value not in [0, 1]:
			raise ValueError("Pin value must be 0, or 1")

		else:
			self.pin1 = value

	def get_pin1(self):

		return self.pin1

	def set_pin2(self, value):

		if value not in [0, 1]:
			raise ValueError("Pin value must be 0, or 1")

		else:
			self.pin2 = value

	def get_pin2(self):

		return self.pin2

	def set_pin(self, value):

		if value not in [0, 1]:
			raise ValueError("Pin value must be 0, or 1")

		else:
			if self.pin1 == None:
				self.set_pin1(value)

			else:
				if self.pin2 == None:
					self.set_pin2(value)
				else:
					raise RuntimeError("No empty pins in the gate " + self.label)

class UnaryGate(LogicGate):

	def __init__(self, name):

		LogicGate.__init__(self, name)

		self.pin = None

	def set_pin(self, value):

		if value not in [0, 1]:
			raise ValueError("Pin value must be 0, or 1")

		else:
			if self.pin == None:
				self.pin = value
			else:
				raise RuntimeError("No empty pins in the gate " + self.label)

	def get_pin(self):

		return self.pin

class Connector(object):

	def __init__(self, fgate, tgate):

		self.fromgate = fgate
		self.togate = tgate

		self.fromgate.perform_logic()

		out = self.fromgate.output

		tgate.set_pin(out)

class AndGate(BinaryGate):

	def __init__(self, name):

		BinaryGate.__init__(self, name)

	def perform_logic(self):

		if self.pin1 == self.pin2 == 1:
			self.output = 1

		else: 
			self.output = 0

class OrGate(BinaryGate):

	def __init__(self, name):

		BinaryGate.__init__(self, name)

	def perform_logic(self):

		if self.pin1 == 1 or self.pin2 == 1:
			self.output = 1

		else: 
			self.output = 0

class NandGate(BinaryGate):

	def __init__(self, name):

		BinaryGate.__init__(self, name)

	def perform_logic(self):

		if self.pin1 == 1 and self.pin2 == 1:
			self.output = 0

		else: 
			self.output = 1

class NorGate(BinaryGate):

	def __init__(self, name):

		BinaryGate.__init__(self, name)

	def perform_logic(self):

		if self.pin1 == 0 and self.pin2 == 0:
			self.output = 1

		else: 
			self.output = 0

class XorGate(BinaryGate):

	def __init__(self, name):

		BinaryGate.__init__(self, name)

	def perform_logic(self):

		if self.pin1 == self.pin2:
			self.output = 0

		else: 
			self.output = 1

class XnorGate(BinaryGate):

	def __init__(self, name):

		BinaryGate.__init__(self, name)

	def perform_logic(self):

		if self.pin1 == self.pin2:
			self.output = 1

		else: 
			self.output = 0

class NotGate(UnaryGate):

	def __init__(self, name):

		UnaryGate.__init__(self, name)

	def perform_logic(self):

		if self.pin == 1:
			self.output = 0

		else:
			self.output = 1

def basic_circuit1():

	g1 = AndGate("g1")
	g2 = OrGate("g2")
	g3 = NotGate("g3")

	g1.set_pin(1)
	g1.set_pin(0)

	c1 = Connector(g1, g2)

	g2.set_pin(1)

	c2 = Connector(g2, g3)
	g3.perform_logic()

	print g3.output

def basic_circuit2(a, b, c, d):

	g1 = NotGate("G1")
	g2 = NotGate("G2")
	g3 = OrGate("G3")

	g1.set_pin(a)
	g2.set_pin(a)

	g3.set_pin(c)
	g3.set_pin(c)

	g4 = AndGate("G4")
	g5 = AndGate("G5")

	Connector(g2, g4)
	Connector(g3, g4)
	Connector(g1, g5)
	Connector(g4, g5)

	g5.perform_logic()
	return g5.output

def get_binary_string(number, length):

	representation = "{0:b}".format(number)
	new_len = length - len(representation)
	return ("0" * new_len) + representation


def simulation():
	bits = 15
	length = len("{0:b}".format(15))

	i = 0
	while i <= bits:
		rep = get_binary_string(i, length)
		a, b, c, d = int(rep[0]), int(rep[1]), int(rep[2]), int(rep[3])
		basic_circuit2(a, b, c, d)
		i += 1

