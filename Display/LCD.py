import RPi.GPIO
from RPLCD.gpio import CharLCD              #externe Library -> stark vereinfachte Nutzung

lcd = CharLCD(
    pin_rs = 25,                
    pin_e = 24,
    pins_data=[23, 18, 21, 20],     #über diese GPIOs werden die Daten gesendet
    numbering_mode = RPi.GPIO.BCM,  #damit GPIO Port Nummern genutzt werden und nicht die physischen nummern
    cols = 16,                      #Anzahl zeichen pro Zeile 
    rows = 2                        #Anzahl Reihen
)

#String erstellen für die Anzeige
def createLCDText(input_upper= "KEIN INPUT", input_lower= ""):
    lcd.clear()
    new_str_upper = str(input_upper)[:16]           #klare Abgrenzung bei 16 Zeichen da sonst der 2. input verschoben wird
    new_str_lower = str(input_lower)[:16]
    
    strLCD = f"{new_str_upper}\r\n{new_str_lower}"
    lcd.home()                                      #cursor wieder ganz oben links ansonsten öfter bugs
    return lcd.write_string(strLCD)                                                                                                                                                                                        

## --------------------------------für Testzwecke ------------------------------ 
if __name__ == "__main__":
    import time
    import sys
    import os
    proj_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(proj_root)
    from Sensoren import distanzsensor
    try:
        while True:

            dist, text = distanzsensor.getMotionsensOutput()
            createLCDText(dist, text) 
            time.sleep(1)

    except KeyboardInterrupt:
        print("Programm beendet")

    finally:
        lcd.clear()
        distanzsensor.red.value=0
        distanzsensor.distsens.close()
        RPi.GPIO.cleanup