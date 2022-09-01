import time
import RPi.GPIO as GPIO

# Pins definitions
slotted_pin = 4

# Set up pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(slotted_pin, GPIO.IN)

# If button is pushed, light up LED
try:
    while True:
        out=GPIO.input(slotted_pin)
        if out==1:
            print("Posición Home")
        else:
            print("Fuera de home")
 

# When you press ctrl+c, this will be called
finally:
    GPIO.cleanup()

#Pines en uso: 14, 15, 18, 20, 21, 22, 27, 17, 9, 11, 24, 26
#La entrada será el pin 4

    #La salida es 0 cuando no hay objeto que detectar
