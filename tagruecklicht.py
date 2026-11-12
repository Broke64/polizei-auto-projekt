from gpiozero import PWMLED, Device
from time import sleep, perf_counter
from gpiozero import LightSensor
from signal import pause

#Perf Counter misst die zeit zwischen den beiden befehlen, perf counter am anfang und dann wenn du fertig gezälz haben willst
#Der Raspberry pi kann keine helligkeit direkt lesen, er erkennt nur spannung 

schwelle_ms = 30 # länger als 30 ms = dunkel

Device.ensure_pin_factory() #Pin-Fabrik wie ein dolmetscher, ensure pin factory ist dafür da damit wir abfragen bevor wir die LED aufrufen 


pin = Device.pin_factory.pin(13) #sensor an GPIO13
led = PWMLED(19)                # LED an GPIO19

#
def messen():
    pin.function = 'output'
    pin.state = False           #Kondensator entladen
    sleep(0.1)              
    pin.function = 'input'         #jetzt lädt er sich über lichtsensr auf
    start = perf_counter()             # ab jetzt schreib die zeit auf und merke sie dir
    while perf_counter() - start < 2:   #
        if pin.state:               #pin ist hoch = kondensator voll
            return (perf_counter() - start) * 1000  # Umwandlung in millisekunden
    return 2000                     #nie hoch = sehr dunkel, es wird nur ausgelöst wenn return perf counter nie ausgeführt wird


try:
    while True:
        ms = messen()               # misst die ladezeit
        if ms > schwelle_ms:        # wenns mehr als 30 dann dunkel also led an 
            if ms >= 100:
                led.value = 1
            else:
                led.value = ms / 100
            print(round(ms, 1), "ms - dunkel") # die round 1 steht für die erste nachkomma stelle, round rundet die zahl ab
        else:
            led.off()
            print(round(ms, 1), "ms - hell")
        sleep(0.3)
finally:                             # egal wie da programm endet führe da aus und schließe beide variablen
    pin.close()
    led.close()