from gpiozero import PWMLED, LightSensor, Button, TonalBuzzer
from gpiozero.tones import Tone
from time import sleep
import threading
from signal import pause

#------------------------------------------------------------------------------------------------------------------------------------

gelb_links = PWMLED(24)
gelb_rechts = PWMLED(23)
modus = "A"     # A = aus

def blinker(seite):

    gelb_rechts.off()
    gelb_links.off()
    match seite.upper():
        case "L": 
            gelb_links.blink(on_time = 0.5, off_time = 0.5)
        case "R":
            gelb_rechts.blink(on_time = 0.5, off_time = 0.5)
        case "B":
            gelb_links.blink(on_time = 0.5, off_time = 0.5)
            gelb_rechts.blink(on_time = 0.5, off_time = 0.5)
        case "A":
            pass
        case _:
            return False

while True:
    modus = str(input("Modus eingeben"))
    if modus.upper() == "Q":
        break
    blinker(modus)

gelb_rechts.off()
gelb_links.off()

#------------------------------------------------------------------------------------------------------------------------------------

blaulicht_links = PWMLED(24)
blaulicht_rechts = PWMLED(23)

double_flash = [(True, 0.05), (False, 0.05), (True, 0.05), (False, 0.25)]

beenden = threading.Event()
_lock = threading.Lock()
blaulicht_thread = None

def muster():
    while not beenden.is_set():
        for an, dauer in double_flash:
            if an:
                blaulicht_links.on()
                blaulicht_rechts.on()
            else:
                blaulicht_links.off()
                blaulicht_rechts.off()
            if beenden.wait(dauer):
                break
    blaulicht_links.off()
    blaulicht_rechts.off()

def blaulicht(an):
    global blaulicht_thread
    with _lock:
        if an:
            if blaulicht_thread and blaulicht_thread.is_alive():
                return
            beenden.clear()
            blaulicht_thread = threading.Thread(target = muster, daemon = True)
            blaulicht_thread.start()
        else:
            beenden.set()
            if blaulicht_thread:
                blaulicht_thread.join()

while True:
    eingabe = input("modus: ")

    if eingabe == "1":
        blaulicht(True)
    elif eingabe == "2":
        blaulicht(False)
    elif eingabe == "Q":
        break
    else:
        print("Fehler Eingabe")
blaulicht(False)

#------------------------------------------------------------------------------------------------------------------------------------

