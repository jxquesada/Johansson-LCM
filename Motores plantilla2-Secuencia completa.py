import RPi.GPIO as GPIO #Librería para el control de los motores a pasos y el servomotor
from RpiMotorLib import RpiMotorLib #Librería para motores a pasos
from RpiMotorLib import rpiservolib #Librería para servomotor
import time
from time import sleep
import serial #Librería para configuración y adquisición de datos de dispositivos seriales

serTESA=serial.Serial('/dev/ttyUSBI', baudrate=1200, bytesize=serial.SEVENBITS,
                      parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_TWO,
                      xonxoff=True, timeout=0.2) #Configuración de puerto

listaMedicionesBloque=[] #Creación de lista para almacenar mediciones de bloques

def DatosTESA(serTESA): 
    detenerse=0 #Constante para while que captura dato
    def recv(serial): #Definición de una función para recibir datos
        while True:
            data=serial.read(30) #Lectura de 30 bytes
            if data == '':
                continue
            else:
                break
            sleep(0.02)
        return data
    while detenerse == 0:
        data=recv(serTESA) #Llamada de la función
        print(data)
        if data != b'': #Comparación de datos recibidos, vacío hasta que se de la medición
            medicion=float(data) #Pasando de string a float
            MedicionBloque=medicion #Guardando dato en lista
            detenerse = 1 #Condición para salir del while
    return MedicionBloque


def ActivaPedal(servo_pin): 

    myservotest = rpiservolib.SG90servo("servoone", 50, 2, 12) #Parámetros del servomotor

    myservotest.servo_move(servo_pin, 2.3, .5, False, .01) #Movimiento a posición 2.3
    myservotest.servo_move(servo_pin, 7.5, .5, False, .01) #Movimiento a posición 7.5
  
  
def Completa2(repeticiones):

    for i in range(repeticiones):
        
        sleep(2)

        ActivaPedal(servo_pin) #Baja paTruelpador
        sleep(tiempoEstabilizacion) #Tiempo de estabilización
        ActivaPedal(servo_pin) #Sube palpador
        #MedicionBloque=DatosTESA(serTESA) #Llama función TESA
        #print(MedicionBloque)
        #listaMediciones.append(MedicionBloque)  #Valor del patrón en posición 1 (centro)

        mymotortest1.motor_go(True, "Half", 416, .005, False, 2) #Mov de 1 a 2

        ActivaPedal(servo_pin) #Baja palpador
        sleep(tiempoEstabilizacion) #Tiempo de estabilización
        ActivaPedal(servo_pin) #Sube palpador
        #MedicionBloque=DatosTESA(serTESA) #Llama función TESA
        #print(MedicionBloque)
        #listaMediciones.append(MedicionBloque)  #Valor del calibrando en posición 2 (esquina)
        
        mymotortest1.motor_go(False, "Half", 96, .005, False, 2) #Mov1 de 2 a 3
        mymotortest2.motor_go(False, "Full", 337, .005, False, 1) #Mov2 de 2 a 3
        mymotortest1.motor_go(True, "Half", 182, .005, False, 1) #Mov3 de 2 a 3

        ActivaPedal(servo_pin) #Baja palpador
        sleep(tiempoEstabilizacion) #Tiempo de estabilización
        ActivaPedal(servo_pin) #Sube palpador
        #MedicionBloque=DatosTESA(serTESA) #Llama función TESA
        #print(MedicionBloque)
        #listaMediciones.append(MedicionBloque)  #Valor del calibrando en posición 3 (esquina)
        
        mymotortest1.motor_go(False, "Half", 183, .005, False, 2) #Mov de 3 a 4

        ActivaPedal(servo_pin) #Baja palpador
        sleep(tiempoEstabilizacion) #Tiempo de estabilización
        ActivaPedal(servo_pin) #Sube palpador
        #MedicionBloque=DatosTESA(serTESA) #Llama función TESA
        #print(MedicionBloque)
        #listaMediciones.append(MedicionBloque)  #Valor del calibrando en posición 4 (esquina)

        mymotortest2.motor_go(True, "Full", 683, .005, False, 2) #Mov de 4 a 5

        ActivaPedal(servo_pin) #Baja palpador
        sleep(tiempoEstabilizacion) #Tiempo de estabilización
        ActivaPedal(servo_pin) #Sube palpador
        #MedicionBloque=DatosTESA(serTESA) #Llama función TESA
        #print(MedicionBloque)
        #listaMediciones.append(MedicionBloque)  #Valor del calibrando en posición 5 (esquina)

        mymotortest1.motor_go(True, "Half", 178, .005, False, 2) #Mov de 5 a 6

        ActivaPedal(servo_pin) #Baja palpador
        sleep(tiempoEstabilizacion) #Tiempo de estabilización
        ActivaPedal(servo_pin) #Sube palpador
        #MedicionBloque=DatosTESA(serTESA) #Llama función TESA
        #print(MedicionBloque)
        #listaMediciones.append(MedicionBloque)  #Valor del calibrando en posición 6 (esquina)

        mymotortest1.motor_go(False, "Half", 178, .005, False, 2) #Mov de 6 a 5
        mymotortest2.motor_go(False, "Full", 342, .005, False, 1) #Mov de 5 a Esp2
        mymotortest1.motor_go(False, "Half", 332, .005, False, 1) #Mov de Esp2 a 1

        ActivaPedal(servo_pin) #Baja palpador
        sleep(tiempoEstabilizacion) #Tiempo de estabilización
        ActivaPedal(servo_pin) #Sube palpador
        #MedicionBloque=DatosTESA(serTESA) #Llama función TESA
        #print(MedicionBloque)
        #listaMediciones.append(MedicionBloque)  #Valor del patrón en posición 1 (centro)

    mymotortest1.motor_go(True, "Half", 208, .005, False, 2) #Mov de 1 a HOME
        
    ActivaPedal(servo_pin) #Baja palpador

    return listaMediciones


GPIO_pins1 = (22, 27, 17) #pines de modo para el motor1
direction1 = 9 #pin de dirección para el motor1
step1 = 11 #pin de step para el motor1

GPIO_pins2 = (5, 6, 13) #pines de modo para el motor2
direction2 = 20 #pin de dirección para el motor2
step2 = 21 #pin de step para el motor2

EN_pin = 24 #pin de enable

servo_pin = 26 #Pin que envía la señal al servomotor

mymotortest1 = RpiMotorLib.A4988Nema(direction1, step1, GPIO_pins1, "A4988") #Parámetros del motor1
mymotortest2 = RpiMotorLib.A4988Nema(direction2, step2, GPIO_pins2, "A4988") #Parámetros del motor2

GPIO.setup(EN_pin, GPIO.OUT)                                                                                                                                                
GPIO.output(EN_pin, GPIO.LOW) #Enable debe estar en LOW

repeticiones=int(input('Cantidad de repeticiones: ')) #Petición del número de repeticiones que se harán de la secuencia
tiempoEstabilizacion=int(input('Tiempo de estabilización: '))

listaMediciones=[]

listaMediciones=Completa2(repeticiones)


GPIO.cleanup()