from tkinter import *
from tkinter import ttk

window=Tk()
window.title("Sistema de medición para válvulas")#Nombre de la ventana
window.resizable(0,0)#No permite cambiar dimensiones de la venta
window.geometry("500x300") #Tamaño de la ventana
#window.config(bg="white")#Color de la ventana

#Variables
Medi= IntVar()

#Funcion

def Mostrar():
    if Medi.get()==1: #Entra a venta de medición de diametro
        miFrame.pack_forget() #Cierra ventana principal!!!!!!!
        FrameDia.pack(side="top", fill="both", expand=True)##Llama ventana deseadad
        e3=Label(FrameDia,text="Medición de diametro").grid(row=0, column=1, padx=10, pady=10)
        boton2=ttk.Button(FrameDia,text='Volver',command=volverprincipal).grid(row=0, column=0)
    if Medi.get()==2: #Entra a venta de medición de longitud
        miFrame.pack_forget() #Cierra ventana principal
        FrameLon.pack(side="top", fill="both", expand=True)
        e3=Label(FrameLon,text="Medición de longitud").grid(row=0, column=1, padx=10, pady=10)
        boton2=ttk.Button(FrameLon,text='Volver',command=volverprincipal).grid(row=0, column=0)
    if Medi.get()==3:
        miFrame.pack_forget() #Cierra ventana principal
        FramePro.pack(side="top", fill="both", expand=True)
        Label(FramePro,text="Medición de Profundidad").grid(row=0, column=1, padx=10, pady=10)
        ttk.Button(FramePro,text='Volver',command=volverprincipal).grid(row=0, column=0)

def volverprincipal():
    FrameDia.pack_forget()
    FrameLon.pack_forget()
    FramePro.pack_forget()
    miFrame.pack(side="top", fill="both", expand=True)

def saludo(X, Y):
    x+y
    print("hola")

#Boton en pantalla general
ttk.Button(window, text='Salir', command=quit).pack(side=BOTTOM) #Boton de salir

#Se define los Frame
FrameDia=Frame(window)
FrameLon=Frame(window)
FramePro=Frame(window)
miFrame=Frame(window) #Crea el frame
miFrame.pack(side="top", fill="both", expand=True)####EMPIEZA EL FRAME!!!!!

#Indica el lote
Label(miFrame, text="Lote: ",font=(18)).grid(row=0, column=0, padx=10, pady=10)#muestra mensaje
####OTRA OPCION###
#.place(X=, Y=)
lote=Entry(miFrame) #Crea cuadro texto
lote.grid(row=0, column=1)

#Indica medida
Label(miFrame, text="Seleccione la característica que desea medir",font=(18)).grid(row=1, column=0) #Ubicacion del texto
#Boton en pantalla general
ttk.Button(miFrame, text='Saludo', command=saludo).grid(row=4, column=4, padx=10, pady=10) #Boton de salir


#Crea la seleccion (RadioButton)
Dia=Radiobutton(miFrame, text="Diámetro", variable=Medi,value=1, command=Mostrar).grid(row=2, column=0)
Lon=Radiobutton(miFrame, text="Longitud", variable=Medi,value=2, command=Mostrar).grid(row=3, column=0)
Pro=Radiobutton(miFrame, text="Profundidad", variable=Medi,value=3, command=Mostrar).grid(row=4, column=0)


window.mainloop()
