import plug_power
import time
import pigpio
#Olhar os Pinos
#Pin1 = Inversor
#Pin2 = Lampada
#Double check o plug_power pls
pin1 = 4
pin2 = 17
def check_power(pp):
	pi = pigpio.pi()
	pi.set_mode(pin1, pigpio.OUTPUT)
	pi.set_mode(pin2, pigpio.OUTPUT)
	pp.check_hour()
	pi.write(pin1, pp.state1)
	pi.write(pin2, pp.state2)
	while True:
        	time.sleep(300)
		pp.check_hour()
        	if pp.state_change1:
            		pi.write(pin1, pp.state1)
		if pp.state_change2:
			pi.write(pin2, pp.state2)

plug = plug_power.plug_power()
check_power(plug)
