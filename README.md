# polizei-auto-projekt
Gewinner TEAM TIKT!
Alaaf!
from time import sleep
from gpiozero import LightSensor, PWMLED

# Sensor an GPIO 13, LED an GPIO 19 anschließen
sensor = LightSensor(13)
led = PWMLED(19)

# Ab welchem Wert es als "dunkel" gilt (0.0 = dunkel, 1.0 = sehr hell)
schwelle = 0.5

try:
    while True:
        # Aktuelle Helligkeit abfragen (Wert zwischen 0.0 und 1.0)
        helligkeit = sensor.value

        if helligkeit < schwelle:
            # Je dunkler es ist, desto heller leuchtet die LED
            led.value = 1 - helligkeit
            print(round(helligkeit, 2), "- dunkel")
        else:
            # Es ist hell genug, LED ausschalten
            led.off()
            print(round(helligkeit, 2), "- hell")

        sleep(0.3)

except KeyboardInterrupt:
    # Wenn du das Programm mit Strg+C beendest
    print("Programm beendet")

finally:
    # Räumt die Pins am Ende sauber auf
    sensor.close()
    led.close()
