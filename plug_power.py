from datetime import datetime
class plug_power:
	def __init__(self):
		self.state = 0 #0 = off; 1 = on
		self.date = datetime.now()

	def check_hour(self):
		self.date = datetime.now()
		self.state_change = 0
		
		if (self.date.hour >= 19) | ((self.date.hour >= 12) & (self.date.weekday() == 5)):
			if (self.state == 1):
				self.state = 0
				self.state_change = 1
		elif (((self.date.hour >= 7) & (self.date.minute >= 30)) | (self.date.hour >= 8)) & (self.date.weekday() <= 5):
			if (self.state == 0): 
				self.state = 1
				self.state_change = 1

		return self.state_change
