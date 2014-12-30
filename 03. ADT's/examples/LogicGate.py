class LogicGate(object):

	def __init__(self, name):

		self.label = name
		self.output = None

	def get_label(self):

		return self.label

	def get_output(self):

		self.output = self.performGateLogic()
		return self.output

class BinaryGate(LogicGate):

	def __init__(self, name):

		LogicGate.__init__(self, name)

		self.pin_a = None
		self.pin_b = None

	def get_pinA(self):

		if self.pin_a == None:
			ipt = input("Enter Pin A input for gate " + self.get_label() + " --> ")
			return int(ipt)
		else:
			return self.pin_a.getFrom().get_output()

	def get_pinB(self):

		if self.pin_b == None:
			ipt = input("Enter Pin B input for gate " + self.get_label() + " --> ")
			return int(ipt)
		else:
			return self.pin_b.getFrom().get_output()

	def set_next_pin(self, source):

		if self.pin_a == None:
			self.pin_a = source

		else:
			if self.pin_b == None:
				self.pin_b = source
			else:
				raise RuntimeError("Error: NO EMPTY PINS")

class UnaryGate(LogicGate):

	def __init__(self, name):

		LogicGate.__init__(self, name)

		self.pin = None

	def get_pin(self):

		ipt = input("Enter Pin input for gate " + self.get_label() + " --> ")
		return int(ipt)

	def set_next_pin(self, source):

		if self.pin == None:
			self.pin = source
		else:
			raise RuntimeError("Error: NO EMPTY PINS")

class AndGate(BinaryGate):

	def __init__(self, name):

		BinaryGate.__init__(self, name)

	def performGateLogic(self):

		a = self.get_pinA()
		b = self.get_pinB()

		if a == 1 and b == 1:
			return a

		else:
			return 0

class OrGate(BinaryGate):

	def __init__(self, name):

		BinaryGate.__init__(self, name)

	def performGateLogic(self):

		a = self.get_pinA()
		b = self.get_pinB()

		if a == 1 or b == 1:
			return 1

		else:
			return 0

class NotGate(UnaryGate):

	def __init__(self, name):

		UnaryGate.__init__(self, name)

	def performGateLogic(self):

		pin = self.get_pin()

		if pin == 1:
			return 0

		else:
			return 1

class Connector(object):

	def __init__(self, fgate, tgate):

		self.fromgate = fgate
		self.togate = tgate

		tgate.set_next_pin(self)