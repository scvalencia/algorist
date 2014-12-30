class LogicGate(object):

	def __init__(self, name):

		self.label = name
		self.output = None

	def get_label(self):

		return self.label

	def get_output(self):
		
		self.output = self.performGateLogic()
		return self.output