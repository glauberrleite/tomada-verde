from datetime import datetime
class plug_power:
	def __init__(self):
		self.state1 = 0 #0 = off; 1 = on
		self.state2 = 0
		self.state_change1 = 0
		self.state_change2 = 0
		self.date = datetime.now()

	def check_hour(self):
		self.date = datetime.now()
		self.state_change1 = 0
		self.state_change2 = 0
		if (self.date.hour >= 19) or ((self.date.hour >= 12) and (self.date.weekday() == 5)):
			if (self.state1 == 1):
				self.state1 = 0
				self.state_change1 = 1
		elif ((self.date.hour >= 7) and (self.date.weekday() <= 5)):
			if (self.state1 == 0):
				self.state1 = 1
				self.state_change1 = 1
		if (self.date.hour >= 18) and (self.data.hour < 23):
			if(self.state2 == 0):
				self.state2 = 1
				self.state_change2 = 1
		elif (self.date.hour >= 23) or (self.date.hour < 18):
			if(self.state2 == 1):
				self.state2 = 0
				self.state_change2 = 1

