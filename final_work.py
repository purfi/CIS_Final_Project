from gpiozero import DistanceSensor, LED, Button
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

sensor = DistanceSensor(echo=23, trigger=24)
red = LED(4)
button = Button(17)
    
def up():
    global result
    result = False
    
def lighton():
    red.on()
    
def lightoff():
    red.off()
    
t = True

button.wait_for_press()
while t == True:
    print('Distance to nearest object is', sensor.distance * 100, 'm')
    sleep(1)
    red.off()
    if sensor.distance * 100 < 10.00:
        lighton()
        finald = sensor.distance
        t = False
        print('Intrusion detected at', finald *100, 'm')
        sleep(10)
red.off()


        
        

    

        
    
