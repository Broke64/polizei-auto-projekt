from gpiozero import DistanceSensor, PWMLED

red = PWMLED(16)                                                                                                                                 
distsens = DistanceSensor(echo = 26, trigger = 12)

def getMotionsensOutput():                                                      
                                                                                
    distance = distsens.distance*100                                                                                                                           
                                                                                
    if distance == 100:                                                         
        red.value = 0                                                           
        text = "Kein Hindernis"                                                 
    elif distance >= 50 and distance < 100:                                     
        red.value = 0                                                           
        text = "Objekt erkannt"                                                 
    elif distance < 50 and distance > 10:                                       
        red.blink(off_time=distance/200, on_time=distance/200)                  
        text = "Vorsicht!"                                                      
    elif distance < 10:                                                         
        text = "!!!STOP!!!"                                                     
        red.value = 1                                                           
                                                                                                                                                               
    dist = f"PDC: {distance:.2f}cm"                                                                                                                            
                                                                                
    return dist, text   #distanz als str (z.B. 100.00cm) und text -> status     