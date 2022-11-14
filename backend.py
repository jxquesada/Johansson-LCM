# import RPi.GPIO as GPIO             #Biblioteca para el control de los motores a pasos y el servomotor
# from RpiMotorLib import RpiMotorLib #Biblioteca para motores a pasos
# from RpiMotorLib import rpiservolib #Biblioteca para servomotor
# import time
# from time import sleep              #Biblioteca para sleep
# import serial                       #Biblioteca para configuración y adquisición de datos de dispositivos seriales
# import openpyxl                     #Biblioteca para hojas de datos



#####################################################
#####################################################
#####################################################
## Definicion de Constantes
# motorEnabledState = GPIO.HIGH
# motorDisabledState = GPIO.LOW
#/////////////////////////////////////////////
#////////////////////////////////////////////




#Definición de Puertos de la Raspberry pi

    #Puertos para el motor 1(Horizontal)
pin_motor1Mode = (22, 27, 17)               #pines de modo para el motor1
pin_motor1Direction = 9                     #pin de dirección para el motor1
pin_motor1Step = 11                         #pin de step para el motor1
# steperMotor1 = RpiMotorLib.A4988Nema(pin_motor1Direction,
#                                     pin_motor1Step, 
#                                     pin_motor1Mode, 
#                                     "A4988")


    #Puertos para el motor 2(Vertical)
pin_motor2Mode = (5, 6, 13)                 #pines de modo para el motor2
pin_motor2Direction = 20                    #pin de dirección para el motor2
pin_motor2Step = 21                         #pin de step para el motor2
# steperMotor2 = RpiMotorLib.A4988Nema(pin_motor2Direction, 
#                                     pin_motor2Step, 
#                                     pin_motor2Mode,
#                                     "A4988")

    #Puertos para el motor del plato giratorio
pin_motorPlateMode = (14, 15, 18)               #Pines de modo de paso
pin_motorPlateDirection = 19                    #Pin de sentido de giro
pin_motorPlateStep = 16                         #Pin de dar paso
# steperMotorPlate = RpiMotorLib.A4988Nema(pin_motorPlateDirection, 
#                                 pin_motorPlateStep, 
#                                 pin_motorPlateMode, 
#                                 "A4988")

#Seteando el pin para habilidar los motores
    #Pin para los motores de calibracion                                        
pin_enableCalibrationMotor = 24   #pin de enable

    #Pin paara el motor del plato giratorio   
pin_enablePlateMotor = 23   

    #Pin paara el sleep del motor del plato giratorio  (no muy util realmente)
sleepMot3=12                        #Pin para controlar el sleep del motor de ordenamiento
                                    #Si está en 1 está activo, en 0 está en sleep

#Seteando el pin para los sensores del plato giratorio                                 
pin_startRotationLimitSensor = 4               #Pin para el sensor infrarrojo de rotacion de angulo nicial
pin_endRotationLimitSensor = 3                 #Pin para el sensor infrarrojo de rotacion de angulo final

# pine para el servo motor
servo_pin = 26





#Puerto Serial para TESA
# serTESA=serial.Serial('/dev/ttyUSBI', baudrate=1200, bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN,
#                         stopbits=serial.STOPBITS_TWO, xonxoff=True, timeout=0.5) #Configuración de puerto
def rpiSetup():
    ######################################################################################################################################







    #Mapeado todos los puertos a la rapberry pi4
    GPIO.setup(pin_enableCalibrationMotor, GPIO.OUT)                                                                                                            
    GPIO.output(pin_enableCalibrationMotor, motorDisabledState)       #Modo seguro, motores inhabilitados

    GPIO.setup(pin_enablePlateMotor, GPIO.OUT)                                                                                                                                            
    GPIO.output(pin_enablePlateMotor, motorDisabledState)       #Modo seguro, motores de plato inhabilitados

    GPIO.setup(pin_startRotationLimitSensor, GPIO.IN)    #Se define como entrada el sensor

    GPIO.setup(sleepMot3, GPIO.OUT)                                                                                                                                                
    GPIO.output(sleepMot3, GPIO.LOW)       #Sleep debe estar en LOW para deshabilitarse

    GPIO.setmode(GPIO.BCM)              #Numeración Broadcom


    # posicionStep=0                      #Variable de posición angular del disco
    # required=0                          #Variable de pasos requeridos par llegar
    #                                     #a la posicion deseada
    # listo=0                             #Variable que determina cuando terminó


    ######################################################################################################################################################
    ######################################################################################################################################################



















def loadSettings():
        Settings = {
            "DarkTheme" : True
        }
        return Settings









def setColorTheme(Settings):
    """Esta funcion toma un diccionario y que contenga el parametro DarkTheme y setea los colores segun si su valor es True o False"""
    if Settings("DarkTheme"):
        backgoundColorDarkLv1 = (0.15, 0.15, 0.15, 1)
        backgoundColorDarkLv2 = (0.125, 0.125, 0.125, 1)
        backgoundColorDarkLv3 = (0.1, 0.1, 0.1, 1)
        menuButtonColor       = (0.15, 0.15, 0.15, 1)
        menuButtonColorHighlight = (0.17, 0.17, 0.17, 1)
        textColorDark         = (1, 1, 1, 1)
        lineColorDark         = (1, 1, 1, 1)
        colorPallete = [backgoundColorDarkLv1, backgoundColorDarkLv2, backgoundColorDarkLv3, menuButtonColor, menuButtonColorHighlight, textColorDark, lineColorDark]
    else:
        backgoundColorDarkLv1 = (0.9, 1, 0.9, 1)
        backgoundColorDarkLv2 = (0.125, 0.125, 0.125, 1)
        backgoundColorDarkLv3 = (0.1, 0.1, 0.1, 1)
        menuButtonColor       = (0.15, 0.15, 0.15, 1)
        menuButtonColorHighlight = (0.17, 0.17, 0.17, 1)
        textColorDark         = (0, 0, 0, 1)
        lineColorDark         = (0, 0, 0, 1)
        colorPallete = [backgoundColorDarkLv1, backgoundColorDarkLv2, backgoundColorDarkLv3, menuButtonColor, menuButtonColorHighlight, textColorDark, lineColorDark]





def recv(serial):               #Definición de una función para recibir datos
        while True:
            
            data=serial.read(30)    #Lectura de 30 bytes
            if data == '':
                continue
            else:
                break
            sleep(0.02)
        return data





def DatosTESA():                                   
    
    detenerse=0                     #Constante para while que captura dato
    
    while detenerse == 0:
        data=recv(serTESA)          #Llamada de la función
        print(data)
        if data != b'':             #Comparación de datos recibidos, vacío hasta que se de la medición
            try:
                medicion=float(data) #Pasando de string a float
                MedicionBloque=medicion #Guardando dato en lista
            
            except:
                divisionDatos=data.split()
                print(divisionDatos)
                medicion=float(divisionDatos[1])    #Pasando de string a float #Cambio de valor a tomar por el TESA
                MedicionBloque=medicion #Guardando dato en lista
            detenerse = 1           #Condición para salir del while
    return MedicionBloque



def ActivaPedal(servo_pin): 

    myservotest = rpiservolib.SG90servo("servoone", 50, 2, 12) #Parámetros del servomotor

    myservotest.servo_move(servo_pin, 2.3, .5, False, .01)     #Movimiento a posición 2.3
    myservotest.servo_move(servo_pin, 7.5, .5, False, .01)     #Movimiento a posición 7.5





def Completa1(valorNominalBloque, tiempoinicial, tiempoestabilizacion, Repeticiones):
    GPIO.output(pin_enableCalibrationMotor, motorEnabledState)       #habilita los motores
    
    
    global dato
    
    #obtenerAnguloBloque(valorNominalBloque[dato])          #Moverse a la siguiente pareja de bloques
    global t1
    t1=time.time()                                   #finaliza el conteo de espera de bloques
    tic=time.perf_counter()                                 #Toma el tiempo inicial
    
    listaMediciones=[]
    
    sleep(int(tiempoinicial)*60)
    
    for i in range(int(Repeticiones)):

        ActivaPedal(servo_pin)                          #Baja palpador
        sleep(int(tiempoestabilizacion))                #Tiempo de estabilización
        ActivaPedal(servo_pin)                          #Sube palpador
        MedicionBloque=DatosTESA()                      #Llama función TESA
        listaMediciones.append(MedicionBloque)          #Valor del patrón en posición 1 (centro)
        print(MedicionBloque)

        steperMotor1.motor_go(True, "Half", 417, .005, False, 2) #Mov de 1 a 2

        ActivaPedal(servo_pin) #Baja palpador
        sleep(int(tiempoestabilizacion)) #Tiempo de estabilización
        ActivaPedal(servo_pin) #Sube palpador
        MedicionBloque=DatosTESA() #Llama función TESA
        listaMediciones.append(MedicionBloque)  #Valor del calibrando en posición 2 (esquina)
        print(MedicionBloque)

        steperMotor1.motor_go(False, "Half", 96, .005, False, 2) #Mov1 de 2 a 3
        steperMotor2.motor_go(False, "Full", 398, .005, False, 1) #Mov2 de 2 a 3
        steperMotor1.motor_go(True, "Half", 178, .005, False, 1) #Mov3 de 2 a 3

        ActivaPedal(servo_pin) #Baja palpador
        sleep(int(tiempoestabilizacion)) #Tiempo de estabilización
        ActivaPedal(servo_pin) #Sube palpador
        MedicionBloque=DatosTESA() #Llama función TESA
        listaMediciones.append(MedicionBloque) #Valor del calibrando en posición 3 (esquina)
        print(MedicionBloque)
            
        steperMotor1.motor_go(False, "Half", 178, .005, False, 2) #Mov de 3 a 4

        ActivaPedal(servo_pin) #Baja palpador
        sleep(int(tiempoestabilizacion)) #Tiempo de estabilización
        ActivaPedal(servo_pin) #Sube palpador
        MedicionBloque=DatosTESA() #Llama función TESA
        listaMediciones.append(MedicionBloque)  #Valor del calibrando en posición 4 (esquina)
        print(MedicionBloque)

        steperMotor2.motor_go(True, "Full", 796, .005, False, 2) #Mov de 4 a 5

        ActivaPedal(servo_pin) #Baja palpador
        sleep(int(tiempoestabilizacion)) #Tiempo de estabilización
        ActivaPedal(servo_pin) #Sube palpador
        MedicionBloque=DatosTESA() #Llama función TESA
        listaMediciones.append(MedicionBloque)  #Valor del calibrando en posición 5 (esquina)
        print(MedicionBloque)

        steperMotor1.motor_go(True, "Half", 174, .005, False, 2) #Mov de 5 a 6

        ActivaPedal(servo_pin) #Baja palpador
        sleep(int(tiempoestabilizacion)) #Tiempo de estabilización
        ActivaPedal(servo_pin) #Sube palpador
        MedicionBloque=DatosTESA() #Llama función TESA
        listaMediciones.append(MedicionBloque)  #Valor del calibrando en posición 6 (esquina)
        print(MedicionBloque)

        steperMotor1.motor_go(False, "Half", 174, .005, False, 2) #Mov de 6 a 5
        steperMotor2.motor_go(False, "Full", 398, .005, False, 1) #Mov de 5 a Esp2
        steperMotor1.motor_go(False, "Half", 330, .005, False, 1) #Mov de Esp2 a 1

        ActivaPedal(servo_pin) #Baja palpador
        sleep(int(tiempoestabilizacion)) #Tiempo de estabilización
        ActivaPedal(servo_pin) #Sube palpador
        MedicionBloque=DatosTESA() #Llama función TESA
        listaMediciones.append(MedicionBloque)  #Valor del patrón en posición 1 (centro)
        print(MedicionBloque)

    steperMotor1.motor_go(True, "Half", 208, .005, False, 2) #Mov de 1 a HOME

    ActivaPedal(servo_pin) #Baja palpador
    
    listaMediciones.append(MedicionBloque)
    #obtenerAnguloBloque(valorNominalBloques[dato])          #Moverse a la siguiente pareja de bloques
    toc=time.perf_counter()                                 #Toma el tiempo final
    global tiempoCorrida
    tiempoCorrida=toc-tic                            #retorna el tiempo de corrida en segundos
    global t0
    t0=time.time()                                   #inicia el conteo de espera de bloques
    GPIO.output(pin_enableCalibrationMotor, motorDisabledState)       #Inhabilita los motores
    return listaMediciones, tiempoCorrida, t0
    











def selectorSecuencia(self, nominalBlockValue, ):
    global BloqueActual
    global dato
    global identificacionBloque
    global valorNominalBloque
    global wb
    global wb2
    
    listaMediciones=[]
    numerocertificado=numeroCertificado.get()
    cantidadbloques=cantidadBloques.get()
    tiempoinicial=tiempoInicial.get()
    tiempoestabilizacion=tiempoEstabilizacion.get()
    Repeticiones=repeticiones.get()
    
    wb = load_workbook(filename =numerocertificado+'.xlsx')
    hoja = wb.active
    
    Secuencia,Plantilla=obtenerSecuencia()
    
    DatoHumeVaisala=DatosVaisala() #Llama función Vaisala
    MedicionTemp1, MedicionTemp2, MedicionTemp3, MedicionTemp4=DatosFluke()
    
    if Secuencia==1 and Plantilla==1: #Realiza secuencia completa1
        listaMediciones, tiempoCorrida, t0=Completa1(tiempoinicial, tiempoestabilizacion, Repeticiones)
    if Secuencia==1 and Plantilla==2: #Realiza secuencia completa2
        listaMediciones, tiempoCorrida, t0=Completa2(tiempoinicial, tiempoestabilizacion, Repeticiones)
    if Secuencia==2: #Realiza secuencia centros
        listaMediciones, tiempoCorrida, t0=Centros(tiempoinicial, tiempoestabilizacion, Repeticiones)
        
#    enviarAlarma()
    
    MedicionTemp5, MedicionTemp6, MedicionTemp7, MedicionTemp8=DatosFluke()
    DatoHumeVaisala1=DatosVaisala() #Llama función Vaisala
    PromedioHumedad=(DatoHumeVaisala+DatoHumeVaisala1)/2

    listaDatos=[]

    listaDatos.append(BloqueActual) #Número de bloque
    listaDatos.append(time.strftime("%d/%m/%y")) #Fecha
    listaDatos.append(time.strftime("%H:%M:%S")) #Hora
    listaDatos.append(identificacionBloque[dato]) #Identificación del bloque
    listaDatos.append(valorNominalBloque[dato]) #Valor Nominal del bloque
    
    listaDatos.extend(listaMediciones)

    listaDatos.append(MedicionTemp1)
    listaDatos.append(MedicionTemp2)
    listaDatos.append(MedicionTemp3)
    listaDatos.append(MedicionTemp4)
    listaDatos.append(MedicionTemp5)
    listaDatos.append(MedicionTemp6)
    listaDatos.append(MedicionTemp7)
    listaDatos.append(MedicionTemp8)

    listaDatos.append(PromedioHumedad)

    if BloqueActual==1:
        crearHoja(Repeticiones)
        hoja.append(listaDatos)
        wb.save(numerocertificado+'.xlsx')
    elif BloqueActual==int(cantidadbloques):
        hoja.append(listaDatos)
        hoja1 = wb.active
        sheet_ranges = wb['Información de servicio']
        primerafecha=sheet_ranges['B2'].value
        primerafecha=primerafecha.split('/')
        dia1=primerafecha[0]
        mes1=primerafecha[1]    
        ultimafecha=time.strftime("%d/%m/%y")
        ultimafecha=ultimafecha.split('/')
        dia2=ultimafecha[0]
        mes2=ultimafecha[1]
        meses=int(mes2)-int(mes1)
        dias=int(dia2)-int(dia1)+30*meses
        #wb = load_workbook(filename =numerocertificado+'.xlsx')
        hoja1= wb['Información de servicio']
        hoja1["B4"]=dias+1
        wb.save(numerocertificado+'.xlsx')
    elif BloqueActual!=1 and BloqueActual!=int(cantidadbloques):
        hoja.append(listaDatos)
        wb.save(numerocertificado+'.xlsx')

    BloqueActual=BloqueActual+1
    dato=dato+1