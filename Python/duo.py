# '''
# Develop a Python script to connect to and make video-calls 

# platform used: Duo
# '''
# #!/usr/bin/python
# # Ensure PyUserInput is installed
# # Ensure webcam is connected, Duo is running full screen and audio sources are set

# from time import sleep
# import RPi.GPIO as GPIO
# from pymouse import PyMouse
# from pykeyboard import PyKeyboard

# m = PyMouse()
# k = PyKeyboard()

# sleep(2)

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Doorbell Button
# GPIO.setup(9, GPIO.OUT) # Indicator LED

# while True:
#     if ( GPIO.input(22) == 1):
#         print ("Doorbell Pressed")
#         GPIO.output(9,True)
#         m.click(276,372) # Click in the Duo text box
#         sleep(0.5)
#         k.tap_key('Delete',n=6,interval=0.05) # Delete existing characters
#         k.type_string("Father") # Type name of Duo contact
#         sleep(0.2)
#         k.tap_key('Return') # Hit Return to select contact
#         sleep(1.5)
#         m.click(683,445) # Click on Video Call button
#         GPIO.output(9,False)
#         for count in range(0, 30):    
#             GPIO.output(9, True)
#             sleep(0.8)
#             GPIO.output(9, False)
#             sleep(0.8)
#     else:
#         sleep(0.05)

import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()

m.click(490,468)
k.tap_key('BackSpace',n=15, interval=0.05) # Delete existing characters
k.tap_key('Delete',n=15, interval=0.05) # Delete existing characters
time.sleep(1.5)
k.type_string("Maa") # Type name of Duo contact
k.tap_key('Return') # Hit Return to select contact
time.sleep(2)
m.click(778,653)

#print(m.position())