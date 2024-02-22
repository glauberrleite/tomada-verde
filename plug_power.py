from datetime import datetime

class PlugPower:
	def __init__(self):
		self.state1 = 0 #0 = off; 1 = on
		self.state_change1 = 0
		self.date = datetime.now()

	def check_hour(self):
		self.date = datetime.now()
		self.state_change1 = 0
		self.state_change2 = 0
		if (self.date.hour >= 18) or ((self.date.hour >= 12) and (self.date.weekday() == 5)):
			if (self.state1 == 1):
				self.state1 = 0
				self.state_change1 = 1
		elif ((self.date.hour >= 8) and (self.date.weekday() <= 5)):
			if (self.state1 == 0):
				self.state1 = 1
				self.state_change1 = 1

