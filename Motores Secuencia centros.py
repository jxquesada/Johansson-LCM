import RPi.GPIO as GPIO #Librería para el control de los motores a pasos y el servomotor
from RpiMotorLib import RpiMotorLib #Librería para motores a pasos
from RpiMotorLib import rpiservolib #Librería para servomotor
import time
from time import sleep
import serial #Librería para configuración y adquisición de datos de dispositivos seriales

serTESA=serial.Serial('/dev/ttyUSBI', baudrate=1200, bytesize=serial.SEVENBITS,
                      parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_TWO,
                      xonxoff=True, timeout=0.5) #Configuración de puerto

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
            try:
                medicion=float(data) #Pasando de string a float
                MedicionBloque=medicion #Guardando dato en lista
            
            except:
                divisionDatos=data.split
                medicion=float(divisionDatos[2])    #Pasando de string a float
                MedicionBloque=medicion #Guardando dato en lista
            detenerse = 1 #Condición para salir del while
    return MedicionBloque


def ActivaPedal(servo_pin): 

    myservotest = rpiservolib.SG90servo("servoone", 50, 2, 12) #Parámetros del servomotor

    myservotest.servo_move(servo_pin, 2.3, .5, False, .01) #Movimiento a posición 2.3
    myservotest.servo_move(servo_pin, 7.5, .5, False, .01) #Movimiento a posición 7.5



def Centros(repeticiones):

    listaMediciones=[]

    for i in range(repeticiones):
        
        #Se inicia en 1 y con palpador arriba

        ActivaPedal(servo_pin) #Baja palpador
        sleep(tiempoEstabilizacion) #Tiempo de estabilización
        ActivaPedal(servo_pin) #Sube palpador
        MedicionBloque=DatosTESA(serTESA) #Llama función TESA
        print(MedicionBloque)
        listaMediciones.append(MedicionBloque)  #Valor del patrón en posición 1 (centro)
     
        mymotortest1.motor_go(True, "Half", 406, .005, False, 2) #Movimiento de punto1 a punto2
        
        ActivaPedal(servo_pin) #Baja palpador
        sleep(tiempoEstabilizacion) #Tiempo de estabilización
        ActivaPedal(servo_pin) #Sube palpador
        MedicionBloque=DatosTESA(serTESA) #Llama función TESA
        print(MedicionBloque)
        listaMediciones.append(MedicionBloque)  #Valor del calibrando en posición 2 (esquina)

        mymotortest1.motor_go(False, "Half", 406, .005, False, 2) #Movimiento de punto2 a punto1
    
    
    ActivaPedal(servo_pin) #Baja palpador
    sleep(tiempoEstabilizacion) #Tiempo de estabilización
    ActivaPedal(servo_pin) #Sube palpador
    MedicionBloque=DatosTESA(serTESA) #Llama función TESA
    print(MedicionBloque)
    listaMediciones.append(MedicionBloque)  #Valor del calibrando en posición 2 (esquina)

    mymotortest1.motor_go(True, "Half", 203, .005, False, 2) #Movimiento de punto1 a HOME

    ActivaPedal(servo_pin) #Baja palpador

    return listaMediciones

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

repeticiones=int(input('Cantidad de repeticiones: ')) #Petición del número de repeticiones que se harán de la secuencia
tiempoEstabilizacion=int(input('Tiempo de estabilización: '))

servo_pin = 26 #Pin que envía la señal al servomotor

listaMediciones=Centros(repeticiones)

print(listaMediciones)

GPIO.cleanup()

