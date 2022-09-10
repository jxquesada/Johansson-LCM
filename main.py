from ast import Pass
from kivy.app import App #librería principal para GUI kivy
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty




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
    def configurationButton_click(self):
        self.temperatureText = "Configuracion Selecionado"
    def usersButton_click(self):
        self.temperatureText = "Usuarios Selecionado"
    def blocksCalibrationButton_click(self):
        self.temperatureText = "Calibración de Bloques Selecionado"
    def resultsButton_click(self):
        self.temperatureText = "Resultados Selecionado"
    def patternsButton_click(self):
        self.temperatureText = "Patrones Selecionado"

JohanssonApp().run()