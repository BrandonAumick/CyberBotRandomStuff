from microbit import *
import radio
import music
import speech

radio.on()
radio.config(channel=3)

sleep(1000)

while True:
    
    packet = radio.receive()
    
    if packet:
        try:
            print("Receive:", packet)
            print (len(packet))
            if (len(packet)) < 6:
                music.play(packet)
            else:    
                speech.say(packet)
        except AttributeError:
            print("packet not image string")
