from plug_power import PlugPower
import time
import pigpio
#Olhar os Pinos
#Pin1 = Inversor
#Double check o plug_power pls
pin1 = 4
def check_power(pp):
    pi = pigpio.pi()
    pi.set_mode(pin1, pigpio.OUTPUT)
    pp.check_hour()
    pi.write(pin1, pp.state1)
    print("Estado inicial: " + str(pp.state1))
    while True:
        time.sleep(300)
        pp.check_hour()
        if pp.state_change1:
            print("Mudança de estado -> Estado: " + str(pp.state1))
            pi.write(pin1, pp.state1)

print("Iniciando script")
plug = PlugPower()
check_power(plug)
