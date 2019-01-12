'''
Eventstyrd pushbutton
En Pushbutton kopplad via 1 kOhm från GPIO 23 till jord
En lysdiod kopplad till GPIO 18

'''
#!/usr/bin/env python

# För att kunna köra från terminal
# coding=utf-8
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # Väljer numrering enl. GPIO
GPIO.setwarnings(False)
LED=18
SIGIN=23
GPIO.setup(LED, GPIO.OUT)

GPIO.setup(SIGIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Set pin SIGIN to be an input pin and set initial value to be pulled low (off)

def button_callback(channel):
    print("Button was pushed!")
    if GPIO.input(SIGIN) == GPIO.LOW:
         GPIO.output(LED, True)
         #print("Button was pushed!")
    else:
         GPIO.output(LED, False)
# Kör först en blinksession för att se att led fungerar
for i in range(0,3):
     GPIO.output(LED, True)
     sleep(1)
     GPIO.output(LED, False)
     sleep(1)

ok=True

GPIO.add_event_detect(SIGIN,GPIO.RISING,callback=button_callback) # Setup event on pin SIGIN rising edge


while ok: # Run forever
     pass
          
print("ok:",ok)

GPIO.cleanup() # Rensar GPIO:s
