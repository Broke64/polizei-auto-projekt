from gpiozero import Button, TonalBuzzer
from gpiozero.tones import Tone
from time import sleep
import threading
from signal import pause



sensor = Button(17, bounce_time = 0.05)
sounds = TonalBuzzer(22, octaves = 2)

def alarmanlage():
    try:
        while True:
            while sensor.is_pressed == False:
                for sound in range(600, 1200, 20):
                    sounds.play(Tone(frequency=sound))
                    sleep(0.01)
                for sound in range(1200, 600, -20):
                    sounds.play(Tone(frequency=sound))
            else:
                sounds.stop()
            sleep(0.2)
    except KeyboardInterrupt:
        sounds.stop()

def sirene():
    while True:
        sounds.play(Tone(frequency = 480))
        sleep(0.8)
        sounds.play(Tone(frequency = 360))
        sleep(0.8)

def hupe():
    while True:
        eingabe = int(input("1 für hupen"))
        if eingabe == 1:
            sounds.play(Tone(frequency = 420))
            sleep(0.5)
            sounds.stop()