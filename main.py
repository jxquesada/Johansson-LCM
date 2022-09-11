from ast import Pass
from kivy.app import App #librería principal para GUI kivy
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.properties import NumericProperty




class JohanssonApp(App):
    """
    Clase principal de kivy,
    Usada para inicializar la GUI principal
    """
    pass

class MainWidget(Widget):
    """
    Elemento principal usado para agregar personalizar la interfaz
    """
    pass

class MainInfoBoxLayout(BoxLayout):
    temperatureText = StringProperty("Temperatura")
    selectedButtonName = StringProperty("Home")

    def configurationButton_click(self):
        self.temperatureText = "Configuracion Selecionado"
        self.selectedButtonName = "Configuracion"

    def usersButton_click(self):
        self.temperatureText = "Usuarios Selecionado"
        self.selectedButtonName = "Usuarios"

    def blocksCalibrationButton_click(self):
        self.temperatureText = "Calibración de Bloques Selecionado"
        self.selectedButtonName = "Calibración de Bloques"

    def resultsButton_click(self):
        self.temperatureText = "Resultados Selecionado"
        self.selectedButtonName = "Resultados"
        
    def patternsButton_click(self):
        self.temperatureText = "Patrones Selecionado"
        self.selectedButtonName = "Patrones"


class UsersStackLayout(StackLayout):
    newButtonID = 0

    def addButton(self):
        newButton = Button(text=str(self.newButtonID),size_hint=(1,None),height="50dp")
        self.add_widget(newButton,index=self.newButtonID)
        self.newButtonID +=1

JohanssonApp().run()