# polizei-auto-projekt
Gewinner TEAM TIKT!
Alaaf!


def pdc(dist):

    if dist <=50 and dist >10:
        sounds.play(Tone(frequency = 440))
        sleep(dist/10)
        sounds.stop()
        
    elif dist <=10:
        sounds.play(Tone(frequency = 440))
        sleep(0.05)
        sounds.stop()
    else:
        sounds.stop()


        

