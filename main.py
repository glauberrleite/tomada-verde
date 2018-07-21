import plug_power
import time
import pigpio
import sys

'Pinos seguindo BCM'
invRelayPin = 27
coolerRelayPin = 22

pi = pigpio.pi()

pi.set_mode(invRelayPin, pigpio.OUTPUT)
pi.set_mode(coolerRelayPin, pigpio.OUTPUT)

if len(sys.argv) > 1:
	'testing routine'
    
	if int(sys.argv[1]):
		pi.write(invRelayPin, 1)
		pi.write(coolerRelayPi, 1)
	else:
		pi.write(invRelayPin, 0)
		pi.write(coolerRelayPi, 0)
	
    quit()

def check_power(pp):
    pp.check_hour()
    pi.write(invRelayPin, pp.state)
	pi.write(coolerRelayPin, pp.state)
    while True:
        time.sleep(300)
        if pp.check_hour():
			pi.write(invRelayPin, not pi.read(invRelayPin))
			pi.write(coolerRelayPi, not pi.read(coolerRelayPin))


plug = plug_power.plug_power()
check_power(plug)