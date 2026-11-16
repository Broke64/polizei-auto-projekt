from pirc522 import RFID
import signal
import time

ERLAUBTE_UID = '218-50-123-127-236'

offen = None
rdr = RFID(pin_irq=None)

print('RFID-Tag an RC522 halten.')

try:
    while True:
        error, tag_type = rdr.request()
        
        if not error:
            error, uid = rdr.anticoll()

            if not error:
                user = '-'.join(str(x) for x in uid)

                print('UID:', user)

                if user == ERLAUBTE_UID:
                    offen = True
                    print('Fahrzeug geöffnet.')

                else:
                    offen = False
                    print('Ungültige Karte.')

                time.sleep(1)

        time.sleep(0.1)

except KeyboardInterrupt:
    print('Programm beendet.')

finally:
    rdr.cleanup()