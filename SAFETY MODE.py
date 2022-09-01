from tkinter import *
from tkinter import ttk
import xlrd
from tkinter import filedialog
import time
from datetime import date
import RPi.GPIO as GPIO             #Biblioteca para el control de los motores a pasos y el servomotor
from RpiMotorLib import RpiMotorLib #Biblioteca para motores a pasos
from RpiMotorLib import rpiservolib #Biblioteca para servomotor
from time import sleep              #Biblioteca para sleep
import serial                       #Biblioteca para configuración y adquisición de datos de dispositivos seriales
import openpyxl                     #Biblioteca para hojas de datos
from openpyxl import load_workbook  #Biblioteca para cargar excel ya existente
import smtplib, ssl

GPIO_pins1 = (22, 27, 17)           #pines de modo para el motor1
direction1 = 9                      #pin de dirección para el motor1
step1 = 11                          #pin de step para el motor1

GPIO_pins2 = (5, 6, 13)             #pines de modo para el motor2
direction2 = 20                     #pin de dirección para el motor2
step2 = 21                          #pin de step para el motor2

EN_pin = 24                         #pin de enable

GPIO_pins3 = (14, 15, 18)           #Pines de modo de paso
direction3 = 19                     #Pin de sentido de giro
step3 = 16                          #Pin de dar paso
sleepMot3=12                        #Pin para controlar el sleep del motor de ordenamiento
                                    #Si está en 1 está activo, en 0 está en sleep

motor3 = RpiMotorLib.A4988Nema(direction3, step3, GPIO_pins3, "A4988") #Parámetros del motor

mymotortest1 = RpiMotorLib.A4988Nema(direction1, step1, GPIO_pins1, "A4988") #Parámetros del motor1
mymotortest2 = RpiMotorLib.A4988Nema(direction2, step2, GPIO_pins2, "A4988") #Parámetros del motor2

GPIO.setup(EN_pin, GPIO.OUT)                                                                                                                                                
GPIO.output(EN_pin, GPIO.HIGH)       #Modo seguro, motores inhabilitados

GPIO.setup(sleepMot3, GPIO.OUT)                                                                                                                                                
GPIO.output(sleepMot3, GPIO.LOW)       #Sleep debe estar en LOW para deshabilitarse

slotted_pin = 4                     #Pin para el sensor infrarrojo
GPIO.setmode(GPIO.BCM)              #Numeración Broadcom
GPIO.setup(slotted_pin, GPIO.IN)    #Se define como entrada el sensor

posicionStep=0                      #Variable de posición angular del disco
required=0                          #Variable de pasos requeridos par llegar
                                    #a la posicion deseada
listo=0                             #Variable que determina cuando terminó
