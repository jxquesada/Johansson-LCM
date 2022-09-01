import openpyxl
import time

wb = openpyxl.Workbook()
hoja = wb.active
hoja.title = "Datos de calibración"
hoja1 = wb.create_sheet("Información de servicio")

repeticiones=int(input('Repeticiones: '))

################## Creación de encabezados secuencia completa ##################

encabezado1=[] #Creación de lista vacía para guardar encabezado 1
encabezado1=['','','','','']
for i in range(repeticiones): #Se harán espacios para cada medición
    encabezado1.append('Medición #'+str(i+1))
    for j in range(6):
        encabezado1.append('')

encabezado1.append('Medición Final') 

hoja.append(encabezado1) #Crea la fila del encabezado 1 con los títulos

encabezado2=[] #Creación de lista vacía para guardar encabezado 2
encabezado2=['Número de bloque','Fecha','Hora','Identificación del bloque', 'Valor nominal del bloque (mm o pulg)']

for i in range(repeticiones): #Se harán espacios para los valores de cada medición
    encabezado2.append('Valor del Patrón en posición 1 (Centro) medición #'+str(i+1)+' (µm o µpulg)')
    encabezado2.append('Valor del Calibrando en posición 2 (Centro) medición #'+str(i+1)+' (µm o µpulg)')
    encabezado2.append('Valor del Calibrando en posición 3 (esquina) medición #'+str(i+1)+' (µm o µpulg)')
    encabezado2.append('Valor del Calibrando en posición 4 (esquina) medición #'+str(i+1)+' (µm o µpulg)')
    encabezado2.append('Valor del Calibrando en posición 5 (esquina) medición #'+str(i+1)+' (µm o µpulg)')
    encabezado2.append('Valor del Calibrando en posición 6 (esquina) medición #'+str(i+1)+' (µm o µpulg)')
    encabezado2.append('Valor del Patron en posición 1 (Centro) medición #'+str(i+1)+' (µm o µpulg')

encabezado2.append('Valor del Patrón en posición 1 (Centro) medición #'+str(repeticiones+1)+' (µm o µpulg)')

encabezado2.append('Temperatura del Patrón durante la toma del Valor del Patrón en  posición 1 (Centro) medición #1 (°C)') #Encabezado para temperaturas al inicio de la secuencia
encabezado2.append('Temperatura del Calibrando durante la toma del Valor del Patrón en posición 1 (Centro) medición #1 (°C)')
encabezado2.append('Temperatura ambiente dentro de la cámara durante la toma del Valor del Patrón en posición 1 (Centro) medición #1 (°C)')
encabezado2.append('Temperatura del Calibrador de bloques durante la toma del Valor del Patrón en posición 1 (Centro) medición #1 (°C)')

encabezado2.append('Temperatura del Patrón durante la toma del Valor del Patrón en  posición 1 (Centro) medición #'+str(repeticiones+1)+' (°C)') #Encabezado para temperaturas al final de la secuencia
encabezado2.append('Temperatura del Calibrando durante la toma del Valor del Patrón en posición 1 (Centro) medición #'+str(repeticiones+1)+' (°C)')
encabezado2.append('Temperatura ambiente dentro de la cámara durante la toma del Valor del Patrón en posición 1 (Centro) medición #'+str(repeticiones+1)+' (°C)')
encabezado2.append('Temperatura del Calibrador de bloques durante la toma del Valor del Patrón en posición 1 (Centro) medición #'+str(repeticiones+1)+' (°C)')

encabezado2.append('Humedad Relativa Promedio Vaisala (%)') #Encabezado para promedio de humedad relativa

hoja.append(encabezado2) #Crea la fila del encabezado 2 con los títulos

################## Datos de información ##################

listaDatos=[]
lista=[1,2,3,4,5]

listaDatos.append(i+1) #Número de bloque
listaDatos.append(time.strftime("%d/%m/%y")) #Fecha
listaDatos.append(time.strftime("%H:%M:%S")) #Hora
#listaDatos.append(identificacionBloques) #Identificación del bloque
#listaDatos.append(valorNominalBloques) #Valor Nominal del bloque
listaDatos.append(lista[1])

print(listaDatos)

################## Creación de encabezado secuencia centros ##################

##encabezado1=[] #Creación de lista vacía para guardar encabezado 1
##encabezado1=['','','','','']
##for j in range(repeticiones): #Se harán espacios para cada medición
##    encabezado1.append('Medición #'+str(i+1))
##    encabezado1.append('')
##
##encabezado1.append('Medición Final') 
##
##hoja.append(encabezado1) #Crea la fila del encabezado 1 con los títulos
##
##encabezado2=[] #Creación de lista vacía para guardar encabezado 2
##encabezado2=['Número de bloque','Fecha','Hora','Identificación del bloque', 'Valor nominal del bloque (mm o pulg)']
##
##for j in range(repeticiones): #Se harán espacios para los valores de cada medición
##    encabezado2.append('Valor del Patrón medición #'+str(i+1)+' (µm o µpulg)')
##    encabezado2.append('Valor del Calibrando medición #'+str(i+1)+' (µm o µpulg)')
##
##encabezado2.append('Valor del Patrón medición #'+str(repeticiones+1)+' (µm o µpulg)')
##
##encabezado2.append('Temperatura del Patrón durante la toma del Valor del Patrón en  posición 1 (Centro) medición #1 (°C)') #Encabezado para temperaturas al inicio de la secuencia
##encabezado2.append('Temperatura del Calibrando durante la toma del Valor del Patrón en posición 1 (Centro) medición #1 (°C)')
##encabezado2.append('Temperatura ambiente dentro de la cámara durante la toma del Valor del Patrón en posición 1 (Centro) medición #1 (°C)')
##encabezado2.append('Temperatura del Calibrador de bloques durante la toma del Valor del Patrón en posición 1 (Centro) medición #1 (°C)')
##
##encabezado2.append('Temperatura del Patrón durante la toma del Valor del Patrón en  posición 1 (Centro) medición #'+str(repeticiones+1)+' (°C)') #Encabezado para temperaturas al final de la secuencia
##encabezado2.append('Temperatura del Calibrando durante la toma del Valor del Patrón en posición 1 (Centro) medición #'+str(repeticiones+1)+' (°C)')
##encabezado2.append('Temperatura ambiente dentro de la cámara durante la toma del Valor del Patrón en posición 1 (Centro) medición #'+str(repeticiones+1)+' (°C)')
##encabezado2.append('Temperatura del Calibrador de bloques durante la toma del Valor del Patrón en posición 1 (Centro) medición #'+str(repeticiones+1)+' (°C)')
##
##encabezado2.append('Humedad Relativa Promedio Vaisala (%)') #Encabezado para promedio de humedad relativa
##
##hoja.append(encabezado2) #Crea la fila del encabezado 2 con los títulos


wb.save('productos.xlsx')
