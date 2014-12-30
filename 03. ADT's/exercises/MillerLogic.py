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