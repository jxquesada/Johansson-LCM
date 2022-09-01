import RPi.GPIO as GPIO #Librería para el control de los motores a pasos y el servomotor
from RpiMotorLib import RpiMotorLib #Librería para motores a pasos
from RpiMotorLib import rpiservolib #Librería para servomotor
import time
from time import sleep

GPIO_pins1 = (22, 27, 17) #pines de modo para el motor1
direction1 = 9 #pin de dirección para el motor1
step1 = 11 #pin de step para el motor1

GPIO_pins2 = (5, 6, 13) #pines de modo para el motor2
direction2 = 20 #pin de dirección para el motor2
step2 = 21 #pin de step para el motor2

EN_pin = 24 #pin de enable

mymotortest1 = RpiMotorLib.A4988Nema(direction1, step1, GPIO_pins1, "A4988") #Parámetros del motor1
mymotortest2 = RpiMotorLib.A4988Nema(direction2, step2, GPIO_pins2, "A4988") #Parámetros del motor2

GPIO.setup(EN_pin, GPIO.OUT)                                                                                                                                                
GPIO.output(EN_pin, GPIO.LOW) #Enable debe estar en LOW

mymotortest1.motor_go(True, "Half", 400, .005, False, 2) #Mov de 1 a 2

# inicio=time.time()
# 
# mymotortest1.motor_go(False34e, "Half", 406, .005, False, 2) #Movimiento de punto1 a punto2
# 
# tiempo=time.time()-inicio
# 
# print(tiempo)

#mymotortest2.motor_go(True, "Full", 683, .005, False, 2) #Mov de 4 a 5

#mymotortest2.motor_go(False, "Full", 683, .005, False, 2) #Mov de 5 a 4

#mymotortest1.motor_go(False, "Half", 406, .005, False, 2) #Movimiento de punto2 a punto1