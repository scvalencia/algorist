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
			if self.pin1 != None:
				self.set_pin1(value)

			else:
				if self.pin2 != None:
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
			if self.pin != None:
				self.pin = value
			else:
				raise RuntimeError("No empty pins in the gate " + self.label)

	def get_pin(self):

		return self.pin