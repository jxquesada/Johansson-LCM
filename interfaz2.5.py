from tkinter import *
from tkinter import ttk
#from matplotlib import pyplot as plt
#from scipy.spatial import distance
#from PIL import Image
#from PIL import ImageTk
from tkinter import filedialog
#import cv2
import numpy as np
import math
#import PIL

#################### CREACIÓN VENTNA PRINCIPAL ####################
window=Tk()
window.title("Sistema de medición para válvulas")#Nombre de la ventana
window.resizable(0,0)#No permite cambiar dimensiones de la venta
window.geometry("800x600") #Tamaño de la ventana
#window.config(bg="white")#Color de la ventana

#Boton de salida pantalla general
ttk.Button(window, text='Salir', command=quit).pack(side=BOTTOM) #Boton de salir
##################################################################

#Variables
Medi= IntVar()
Lote = StringVar()
panelA = None


#!!!!!!!BORRAR VERSION FINAL!!!!!abrir imagen
def openfilename(): 
    filename = filedialog.askopenfilename(title ='Buscador') #Busca la imagen en carpeta
    return filename



#Funciones
#################### MEDICIÓN DIÁMETRO ####################
def MedicionDiametro (image):
    imagedia=image
    gray = cv2.cvtColor(imagedia, cv2.COLOR_BGR2GRAY)#Conversion a grises
    ret, binary = cv2.threshold(gray,100,255,cv2.THRESH_OTSU) #Umbralización
    imgray=cv2.Canny(gray,100,150)#Contornos Canny
    valve_circle = cv2.HoughCircles(imgray,cv2.HOUGH_GRADIENT,2,200,param1=20,param2=90,minRadius=550,maxRadius=600)#Hough
    circles = valve_circle.reshape(-1, 3)
    circles = np.uint16(np.around(circles))
    for i in circles:
        cv2.circle(imagedia, (i[0], i[1]), i[2], (0, 0, 255), 5)
        radio=i[2]
    return radio,imagedia
###########################################################

#################### MEDICIÓN LONGITUD ####################
def longitud(ima):
    gray = cv2.cvtColor(ima, cv2.COLOR_BGR2GRAY)#Tonos de grises
    image = gray[650:1400, 150:950]#Recorta imagen grises
    imagecolor = ima[650:1400, 150:950]#Recorta imagen color
    ret, binary = cv2.threshold(image,155,255,cv2.THRESH_BINARY_INV)#Umbralización
    binary = ~binary#Inversion de tonos
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)#Contornos findcontours
    for pic, contour in enumerate(contours): #Recorre los contronos
        area = cv2.contourArea(contour)                #Se obtiene el área del contornos
        if(area<2000): #Encuentra las coordenadas de contornos pequeños   
            xrn,yrn,wrn,hrn = cv2.boundingRect(contour)     #Coordenadas de rectangulos que contiene los contornos
            cv2.rectangle(binary, (xrn,yrn), (xrn+wrn,yrn+hrn), 255, -1) #Dibujo los rectangulos blancos sobre contornos
        continue
    imgray=cv2.Canny(binary,20,40)#Contornos Canny
    lines = cv2.HoughLinesP(imgray,1,np.pi/180,100,minLineLength=0,maxLineGap=100)#Hough
    i=0
    for line in lines: #Recorre lineas encontradas
        x1,y1,x2,y2 = line[0] #Obtiene coordenadas de líneas encontradas
        cv2.line(imagecolor,(x1,y1),(x2,y2),(0,255,0),1) #Dibuja linea encontrada
    Lon=distance.euclidean((x1,y1), (x2,y2))#Calcula longitud de distancia encontrada
    return Lon,imagecolor
##############################################################

#################### MEDICIÓN PROFUNDIDAD ####################
def calculodispro (X,Y,imagray,imacolor): #Función para calcular la distancia
    cv2.circle(imacolor, (X, Y), 5, (0,0,255), -1)#Dibuja circulo superior
    rows,cols = imagray.shape #Obtiene cantidad de filas y columnas
    Yfi=0
    i=1
    for i in range(rows):#Recorre las filas en un Y definido
        k = imagray[i-1,X]
        k2 = imagray[i,X]
        if k!=k2: #Detecta cambio de color
            Yfi=i
    cv2.circle(imacolor, (X, Yfi), 5, (0,0,255), -1)#Dibuja circulo inferior
    dist=distance.euclidean((X, Y), (X, Yfi))#Calcula distancia derecha
    print("DD:",dist)
    return dist

def profundidad (ima):
    gray = cv2.cvtColor(ima, cv2.COLOR_BGR2GRAY)#Escala de grises
    imagris = gray[68:262, 170:1046] #Recorte imagen tono grises
    imagcolor = ima[68:262, 170:1046] #Recorte imagen color
    ret, binary = cv2.threshold(imagris,87,255,cv2.THRESH_BINARY) #Umbralización
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #Contorno FindContour
    for pic, contour in enumerate(contours):#Recorre contornos encontrados
        area = cv2.contourArea(contour)             #Se obtiene el área del contornos
        if(18000>area>12000):                       #Para contornos con area mayor a 12000 
            xr,yr,wr,hr = cv2.boundingRect(contour)     #Coordenadas de los contornos
        if(area<5000): #Encuentra las coordenadas de contornos pequeños   
            xrn,yrn,wrn,hrn = cv2.boundingRect(contour)     #Coordenadas de rectangulos que contiene los contornos
            cv2.rectangle(binary, (xrn,yrn), (xrn+wrn,yrn+hrn), 255, -1) #Dibujo los rectangulos blancos sobre contornos
        continue
    XIz=int(xr+wr/20)#Posición X izquierda
    XCe=int(xr+wr/2)#Posición X centro
    XDe=int(xr+19*wr/20) #Posición X derecha
    distIZ=calculodispro (XIz,int(yr),binary,imagcolor)#Obtiene distancia de punto izquierdo
    distCent=calculodispro (XCe,int(yr),binary,imagcolor)#Obtiene distancia de punto centro
    distDer=calculodispro (XDe,int(yr),binary,imagcolor)#Obtiene distancia de punto derecho
    distfin=(distIZ+distCent+distDer)/3#Calcula distancia final
    return distfin, imagcolor
###############################################################

#################### CARGAR IMAGEN ####################
def openfiledia():
    global panelA
    filename = filedialog.askopenfilename(title ='Buscador') #Busca la imagen en carpeta
    image = cv2.imread(filename)#Lectura de imagen
    Radi,ImaMediDia=MedicionDiametro(image)#Llama función de diametro
    image = cv2.resize(ImaMediDia, (300,350), interpolation = cv2.INTER_AREA)#Ajusta el tamaño de la imagen a la pantalla
    image = Image.fromarray(image)#Convierte imagen en formato PIL 
    image = ImageTk.PhotoImage(image)#Convierte imagen en formato ImageTk
    if panelA is None:
        panelA = Label(image=image)
        panelA.image = image
        panelA.pack(side="left", padx=10, pady=10)
    else:
        panelA.pack()
        panelA.configure(image=image)
        panelA.image = image

def openfilelon():
    global panelA
    filename = filedialog.askopenfilename(title ='Buscador') #Busca la imagen en carpeta
    image = cv2.imread(filename)#Lectura de imagen
    longi, image=longitud(image)#Llama función de longitud
    image = cv2.resize(image, (300,350), interpolation = cv2.INTER_AREA)#Ajusta el tamaño de la imagen a la pantalla
    image = Image.fromarray(image)#Convierte imagen en formato PIL 
    image = ImageTk.PhotoImage(image)#Convierte imagen en formato ImageTk
    if panelA is None:
        panelA = Label(image=image)
        panelA.image = image
        panelA.pack(side="left", padx=10, pady=10)
    else:
        panelA.pack()
        panelA.configure(image=image)
        panelA.image = image

def openfilepro():
    global panelA
    filename = filedialog.askopenfilename(title ='Buscador') #Busca la imagen en carpeta
    image = cv2.imread(filename)#Lectura de imagen
    distafinal, imagen=profundidad(image)#Llama función de profundidad
    image = cv2.resize(image, (300,350), interpolation = cv2.INTER_AREA)#Ajusta el tamaño de la imagen a la pantalla
    image = Image.fromarray(image)#Convierte imagen en formato PIL 
    image = ImageTk.PhotoImage(image)#Convierte imagen en formato ImageTk
    if panelA is None:
        panelA = Label(image=image)
        panelA.image = image
        panelA.pack(side="left", padx=10, pady=10)
    else:
        panelA.pack()
        panelA.configure(image=image)
        panelA.image = image  


#################### SELECCIÓN DE MEDICIÓN ####################
def Mostrar():
    if Medi.get()==1: #Entra a venta de medición de diametro
        miFrame.pack_forget() #Cierra ventana principal
        FrameDia.pack(side="top", fill="both", expand=True)
        e3=Label(FrameDia,text="Medición de diametro").grid(row=0, column=1, padx=10, pady=10)
        boton2=ttk.Button(FrameDia,text='Volver',command=volverprincipal).grid(row=0, column=0)
        btncar = Button(FrameDia, text="Tomar medición", command=openfiledia).grid(row=2, column=0)  #####!!!!!!CAMBIAR!!!!      
    if Medi.get()==2: #Entra a venta de medición de longitud
        miFrame.pack_forget() #Cierra ventana principal
        FrameLon.pack(side="top", fill="both", expand=True)
        e3=Label(FrameLon,text="Medición de longitud").grid(row=0, column=1, padx=10, pady=10)
        boton2=ttk.Button(FrameLon,text='Volver',command=volverprincipal).grid(row=0, column=0)
        btncar = Button(FrameLon, text="Tomar medición", command=openfilelon).grid(row=2, column=0)  #####!!!!!!CAMBIAR!!!!   
    if Medi.get()==3:
        miFrame.pack_forget() #Cierra ventana principal
        FramePro.pack(side="top", fill="both", expand=True)
        Label(FramePro,text="Medición de Profundidad").grid(row=0, column=1, padx=10, pady=10)
        ttk.Button(FramePro,text='Volver',command=volverprincipal).grid(row=0, column=0)
        btncar = Button(FramePro, text="Tomar medición", command=openfilepro).grid(row=2, column=0)  #####!!!!!!CAMBIAR!!!!   
###############################################################

def volverprincipal():
    global panelA
    FrameDia.pack_forget()
    FrameLon.pack_forget()
    FramePro.pack_forget()
    panelA.pack_forget()
    miFrame.pack(side="top", fill="both", expand=True)


#################### CREACIÓN DE FRAMES ####################
FrameDia=Frame(window)
FrameLon=Frame(window)
FramePro=Frame(window)
miFrame=Frame(window) 
miFrame.pack(side="top", fill="both", expand=True)
############################################################


#################### FRAME PRINCIPAL ####################
Label(miFrame, text="Número de lote: ",font=(18)).grid(row=0, column=0, padx=10, pady=10) #Texto lote
Lote=Entry(miFrame) #Crea cuadro texto lote
Lote.grid(row=0, column=1) #Posición cuadro de texto
Label(miFrame, text="Seleccione la característica que desea medir",font=(18)).grid(row=1, column=0) #Texto
Dia=Radiobutton(miFrame, text="Diámetro", variable=Medi,value=1, command=Mostrar).grid(row=2, column=0) #Crea la seleccion (Diámetro)
Lon=Radiobutton(miFrame, text="Longitud", variable=Medi,value=2, command=Mostrar).grid(row=3, column=0)#Crea la seleccion (Longitud)
Pro=Radiobutton(miFrame, text="Profundidad", variable=Medi,value=3, command=Mostrar).grid(row=4, column=0)#Crea la seleccion (Profundidad)
############################################################

window.mainloop()
