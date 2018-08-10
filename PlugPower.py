from datetime import datetime
import pigpio

class PlugPower:
	def __init__(self, outletPin, lightPin):
		self.pi = pigpio.pi()
		self.pi.set_mode(outletPin, pigpio.OUTPUT)
		self.pi.set_mode(lightPin, pigpio.OUTPUT)

		self.state1 = 0
		self.state2 = 0
		self.state_change1 = 0
		self.state_change2 = 0
		self.date = datetime.now()



	def check(self):
		self.data = datetime.now()


	def check_hour(self):
		self.date = datetime.now()
		self.state_change1 = 0
		self.state_change2 = 0

		if (self.date.hour >= 19) or ((self.date.hour >= 12) and (self.date.weekday() == 5)): #weekday 5 = sábado
			if (self.state1 == 1):
				self.state1 = 0
				self.state_change1 = 1
		elif ((self.date.hour >= 7) or (self.date.weekday() < 5)):
			if (self.state1 == 0):
				self.state1 = 1
				self.state_change1 = 1
		if (self.date.hour >= 18):
			if(self.state2 == 0):
				self.state2 = 1
				self.state_change2 = 1
		elif (self.date.hour >= 6):
			if(self.state2 == 1):
				self.state2 = 0
				self.state_change2 = 1
