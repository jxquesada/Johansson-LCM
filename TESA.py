import serial #Librería para configuración y adquisición de datos de dispositivos seriales
from time import sleep #Librería de tiempo

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
        if data != b'': #Comparación de datos recibidos, vacío hasta que se de la medición
            medicion=float(data) #Pasando de string a float
            MedicionBloque=medicion #Guardando dato en lista
            detenerse = 1 #Condición para salir del while
    return MedicionBloque

MedicionBloque=DatosTESA(serTESA)
listaMedicionesBloque.append(MedicionBloque)

MedicionBloque=DatosTESA(serTESA)
listaMedicionesBloque.append(MedicionBloque)

print(listaMedicionesBloque)

    

