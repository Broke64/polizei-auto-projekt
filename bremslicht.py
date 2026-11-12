from gpiozero import DistanceSensor, PWMLED
from time import sleep
bremslicht = PWMLED(19)  

def bremse(bremsen):
    
    if bremsen == True:
        bremslicht.value = 1
        print("Es wird gebremst!")
    else:
        bremslicht.value = 0
        print("Es wird nicht gebremst.")

