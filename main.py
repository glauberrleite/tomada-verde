#!/usr/bin/env python
from PlugPower import PlugPower
import time

outletPin = 4
lightPin = 17

def check_power(pp):
	pp.check_hour()
    pi.write(pin1, pp.state1)
    pi.write(pin2, pp.state2)
    while True:
        time.sleep(300)
		pp.check_hour()
        if pp.state_change1:
			#Arrumar Aqui
            pi.write(pin1, pp.state1)
		if pp.state_change2:
			#Arrumar Aqui
			pi.write(pin2, pp.state2)

plug = PlugPower(outletPin, lightPin)

while True:
	plug.check()
