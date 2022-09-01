import serial
from time import sleep

serFluke=serial.Serial('/dev/ttyUSB2', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                       stopbits=serial.STOPBITS_ONE, xonxoff=True, timeout=0.5) #Configuración de puerto

listaMedicionesTemp1=[] #Creación de lista para almacenar mediciones de temperatura en bloque patrón
listaMedicionesTemp2=[] #Creación de lista para almacenar mediciones de temperatura en bloque calibrando
listaMedicionesTemp3=[] #Creación de lista para almacenar mediciones de temperatura en ambiente del calibrador de bloques
listaMedicionesTemp4=[] #Creación de lista para almacenar mediciones de temperatura en calibrador de bloques

def DatosFluke(serFluke):
    serFluke.write(b'READ?1\r\n') #Envío de instrucción para capturar dato de temperatura 1
    serFluke.write(b'READ?2\r\n') #Envío de instrucción para capturar dato de temperatura 2
    serFluke.write(b'READ?3\r\n') #Envío de instrucción para capturar dato de temperatura 3
    serFluke.write(b'READ?4\r\n') #Envío de instrucción para capturar dato de temperatura 4

    detenerse=0 #Constante para while que captura dato
    
    MedicionTemp1=0 #Creación de variable para almacenar mediciones de temperatura en bloque patrón
    MedicionTemp2=0 #Creación de variable para almacenar mediciones de temperatura en bloque calibrando
    MedicionTemp3=0 #Creación de variable para almacenar mediciones de temperatura en ambiente del calibrador de bloques
    MedicionTemp4=0 #Creación de variable para almacenar mediciones de temperatura en calibrador de bloques


    def recv(serial): #Definición de una función para recibir datos
        while True:
            data=serial.read(32) #revisar cantidad de bits 30 o 100
            print(data)
            if data == '':
                continue
            else:
                break
            sleep(0.02)
        return data
    while detenerse == 0:
        data=recv(serFluke) #Llamada de la función   
        if data != b'': #Comparación de datos recibidos, vacío hasta que se de la medición
            todas=data.split()#Separar los 4 datos en una lista
            MedicionTemp1=float(todas[0]) #Guardando temperatura 1 en lista
            MedicionTemp2=float(todas[1]) #Guardando temperatura 2 en lista
            MedicionTemp3=float(todas[2]) #Guardando temperatura 3 en lista
            MedicionTemp4=float(todas[3]) #Guardando temperatura 4 en lista
            detenerse = 1  #Condición para salir del while
    return MedicionTemp1, MedicionTemp2, MedicionTemp3, MedicionTemp4

MedicionTemp1, MedicionTemp2, MedicionTemp3, MedicionTemp4=DatosFluke(serFluke)


listaMedicionesTemp1.append(MedicionTemp1)
listaMedicionesTemp2.append(MedicionTemp2)
listaMedicionesTemp3.append(MedicionTemp3)
listaMedicionesTemp4.append(MedicionTemp4)

MedicionTemp1, MedicionTemp2, MedicionTemp3, MedicionTemp4=DatosFluke(serFluke)

listaMedicionesTemp1.append(MedicionTemp1)
listaMedicionesTemp2.append(MedicionTemp2)
listaMedicionesTemp3.append(MedicionTemp3)
listaMedicionesTemp4.append(MedicionTemp4)


print(listaMedicionesTemp1, listaMedicionesTemp2, listaMedicionesTemp3, listaMedicionesTemp4)


