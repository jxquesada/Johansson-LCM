import RPi.GPIO as GPIO #Librería para el control de los motores a pasos y el servomotor
from RpiMotorLib import rpiservolib
from time import sleep

servo_pin = 26

def ActivaPedal(servo_pin):

    myservotest = rpiservolib.SG90servo("servoone", 50, 2, 12)

    myservotest.servo_move(servo_pin, 2.3, .5, False, .01)
    myservotest.servo_move(servo_pin, 7.5, .5, False, .01)
    #myservotest.servo_move(servo_pin, 12.3, .5, False, .01)
    
ActivaPedal(servo_pin)

sleep (30)

ActivaPedal(servo_pin)

GPIO.cleanup()


