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

		ipt = input("Enter Pin A input for gate " + self.get_label() + " --> ")
		self.pin_a = int(ipt)
		return self.pin_a

	def get_pinB(self):
		
		ipt = input("Enter Pin B input for gate " + self.get_label() + " --> ")
		self.pin_b = int(ipt)
		return self.pin_b

class UnaryGate(LogicGate):

	def __init__(self, name):

		LogicGate.__init__(self, name)

		self.pin = None

	def get_pin(self):

		ipt = input("Enter Pin input for gate " + self.get_label() + " --> ")
		self.pin = int(ipt)
		return self.pin

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