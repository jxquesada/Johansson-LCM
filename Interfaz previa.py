from tkinter import *
from tkinter import ttk

window=Tk()
window.title("Calibración de bloques")#Nombre de la ventana
window.resizable(0,0)#No permite cambiar dimensiones de la venta
window.geometry("1000x800") #Tamaño de la ventana

secEscogida= IntVar()
planEscogida= IntVar()
escogerFolio= IntVar()

def irCalibra():
    FrameInfo.pack_forget()
    FrameCalibra.pack(side="top", fill="both", expand=True)

def obtenerSecuencia():
    Secuencia=secEscogida.get()
    Plantilla=planEscogida.get()
    return Secuencia,Plantilla
   
def selectorSecuencia():
    Secuencia,Plantilla=obtenerSecuencia()
    if Secuencia==1 and Plantilla==1: #Entra a venta de medición de diametro
        print('Secuencia completa plantilla 1')
    if Secuencia==1 and Plantilla==2: #Entra a venta de medición de longitud
        print('Secuencia completa plantilla 2')
    if Secuencia==2: #Entra a venta de medición de longitud
        print('Secuencia centros')

def obtenerFolio():
    if escogerFolio.get()==1: #Folio1
        folioUsado='LRR-DI-01-FOLIOS'
    if escogerFolio.get()==2: #Folio2
        folioUsado='ORA-DI-01-FOLIOS'
    if escogerFolio.get()==3: #Folio3
        folioUsado='ILH-DI-03-FOLIOS'
    if escogerFolio.get()==4: #Otro
        folioUsado='ILH-DI-03-FOLIOS'
    

FrameInfo=Frame(window) #Crea el frame donde estará la información de servicio
FrameCalibra=Frame(window) #Crea el frame donde se realizará el proceso de calibración

################## Frame Información de servicio ##################

FrameInfo.pack(side="top", fill="both", expand=True) #Empieza el frame de información

Label(FrameInfo, text="Información servicio",font=(100)).place(x=10, y=10)

Label(FrameInfo, text="Información general",font=(100)).place(x=10, y=70)

Label(FrameInfo, text="Número de certificado: ").place(x=10, y=100)
numeroCertificado=Entry(FrameInfo).place(x=200, y=100)

Label(FrameInfo, text="Solicitante: ").place(x=10, y=130)
solicitante=Entry(FrameInfo).place(x=200, y=130)

Label(FrameInfo, text="Número de solicitud: ").place(x=10, y=160)
numeroSolicitud=Entry(FrameInfo).place(x=200, y=160)

Label(FrameInfo, text="Dirección del solicitante: ").place(x=10, y=190)
direccionSolicitante=Entry(FrameInfo).place(x=200, y=190)

Label(FrameInfo, text="Información del calibrando",font=(100)).place(x=10, y=250)

Label(FrameInfo, text="Cantidad de bloques: ").place(x=10, y=280)
cantidadBloques=Entry(FrameInfo).place(x=200, y=280)

Label(FrameInfo, text="Marca: ").place(x=10, y=310)
marca=Entry(FrameInfo).place(x=200, y=310)

Label(FrameInfo, text="Folios de bitacora utilizados: de ").place(x=10, y=340)
folio1=Entry(FrameInfo, width=5).place(x=225, y=340)
Label(FrameInfo, text="a ").place(x=282, y=340)
folio2=Entry(FrameInfo, width=5).place(x=302, y=340)

Label(FrameInfo, text="Referencia de datos: ").place(x=10, y=370)
Radiobutton(FrameInfo, text="LRR-DI-01-FOLIOS", variable=escogerFolio,value=1, command=obtenerFolio).place(x=10, y=400)
Radiobutton(FrameInfo, text="ORA-DI-01-FOLIOS", variable=escogerFolio,value=2, command=obtenerFolio).place(x=10, y=430)
Radiobutton(FrameInfo, text="ILH-DI-03-FOLIOS", variable=escogerFolio,value=3, command=obtenerFolio).place(x=10, y=460)
Radiobutton(FrameInfo, text="Otro: ", variable=escogerFolio,value=4, command=obtenerFolio).place(x=10, y=490)
nuevoFolio=Entry(FrameInfo).place(x=200, y=490)

ttk.Button(FrameInfo, text='Siguiente', command=irCalibra).place(x=855, y=740) #Boton para ir a frame de calibración

################## Frame Calibración ##################

Label(FrameCalibra, text="Secuencia: ").place(x=10, y=10)
Radiobutton(FrameCalibra, text="Completa", variable=secEscogida,value=1, command=obtenerSecuencia).place(x=10, y=40)
Radiobutton(FrameCalibra, text="Centros", variable=secEscogida,value=2, command=obtenerSecuencia).place(x=10, y=70)

Label(FrameCalibra, text="Plantilla: ").place(x=10, y=130)
Radiobutton(FrameCalibra, text="1", variable=planEscogida,value=1, command=obtenerSecuencia).place(x=10, y=160)
Radiobutton(FrameCalibra, text="2", variable=planEscogida,value=2, command=obtenerSecuencia).place(x=10, y=190)

Label(FrameCalibra, text="Tiempo de estabilización: ").place(x=10, y=250)
tiempoEstabilizacion=Entry(FrameCalibra).place(x=200, y=250)

Label(FrameCalibra, text="Repeticiones: ").place(x=10, y=280)
repeticiones=Entry(FrameCalibra).place(x=200, y=280)

boton2=ttk.Button(FrameCalibra, text='Iniciar calibración', command=selectorSecuencia).place(x=10, y=500) #Boton para ir a frame de calibración

boton3=ttk.Button(FrameCalibra, text='Pausar calibración', command=selectorSecuencia).place(x=445, y=500) #Boton para parar secuen

boton4=ttk.Button(FrameCalibra, text='Reanudar calibración', command=selectorSecuencia).place(x=840, y=500) #Boton para parar secuen

ttk.Button(window, text='Salir', command=quit).pack(side=BOTTOM) #Boton de salir

window.mainloop()

window.mainloop() 


