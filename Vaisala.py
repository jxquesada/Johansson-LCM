import serial
from time import sleep
serVaisala=serial.Serial('/dev/ttyUSB0', baudrate=4800, bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout= 0.5)
#serVaisala=serial.Serial('/dev/ttyAMA0', baudrate=4800, bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout= 0.5)
#serVaisala=serial.Serial('/dev/ttyUSB0', baudrate=19200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout= 0.5)

listaDatosPresVaisala=[]
listaDatosTempVaisala=[]
listaDatosHumeVaisala=[]

#serVaisala.write(b'RUN\r\n')
#serVaisala.write(b'R\r/\n')
#serVaisala.write(b'form "P=" 4.2 P " " U6 \t "T=" t " " U3 \t "RH=" 4.2 rh " " U5 \r\n')
#serVaisala.write(b'form 4.2 P " " \t 4.2 t " " \t 4.2 rh " " \r\n')

def DatosVaisala(serVaisala):
    serVaisala.write(b'SEND\r\n')
    
    detenerse=0
    
    DatoPresVaisala=0
    DatoTempVaisala=0
    DatoHumeVaisala=0
    
    def recv(serial):
        while True:
            data=serial.read(30)
            print(data)
            if data == '':
                continue
            else:
                break
            sleep(0.02)
        return data
    while detenerse == 0:
        data=recv(serVaisala)
        if data != b'': #Comparación de datos recibidos, vacío hasta que se de la medición
            todos=data.split()#Separar los 4 datos en una lista
            DatoPresVaisala=float(todos[1]) #Guardando presión atmosférica en lista
            DatoTempVaisala=float(todos[2]) #Guardando temperatura en lista
            DatoHumeVaisala=float(todos[3]) #Guardando humedad relativa 3 en lista
            detenerse = 1
    return DatoPresVaisala, DatoTempVaisala, DatoHumeVaisala


DatoPresVaisala, DatoTempVaisala, DatoHumeVaisala=DatosVaisala(serVaisala)

listaDatosPresVaisala.append(DatoPresVaisala)
listaDatosTempVaisala.append(DatoTempVaisala)
listaDatosHumeVaisala.append(DatoHumeVaisala)

DatoPresVaisala, DatoTempVaisala, DatoHumeVaisala=DatosVaisala(serVaisala)

listaDatosPresVaisala.append(DatoPresVaisala)
listaDatosTempVaisala.append(DatoTempVaisala)
listaDatosHumeVaisala.append(DatoHumeVaisala)

print(listaDatosPresVaisala)
print(listaDatosTempVaisala)
print(listaDatosHumeVaisala)



    
