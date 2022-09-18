from ast import Pass
from kivy.app import App #librería principal para GUI kivy
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.lang import Builder

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView


#Builder.load_file('Johansson.kv')



    

# class HomeWidget(BoxLayout):#BoxLayout Widget:
#     """
#     Elemento principal usado para agregar personalizar la interfaz
#     """
#     pass

class HomeBoxLayout(BoxLayout):
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




class JohanssonApp(App):
    """
    Clase principal de kivy,
    Usada para inicializar la GUI principal
    """
    def build(self):
        return HomeBoxLayout()

if __name__=='__main__':
    JohanssonApp().run()