from ast import Pass
from kivy.app import App #librería principal para GUI kivy
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import ColorProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
import backend as bef



#Builder.load_file('Johansson.kv')
Builder.load_file('ConfigurationPage.kv')
Builder.load_file('UsersPage.kv')
Builder.load_file('CalibrationPage.kv')
Builder.load_file('ResultsPage.kv')
Builder.load_file('PatternsPage.kv')


print(round(0.12315,2))                                                                                                                                                         

# class HomeWidget(BoxLayout):#BoxLayout Widget:
#     """
#     Elemento principal usado para agregar personalizar la interfaz
#     """
#     pass
class HomeMenuPageManager(ScreenManager):
    pass

class HomeBoxLayout(BoxLayout):
    temperatureText = StringProperty("Temperatura")
    selectedButtonName = StringProperty("Home")
    # ConfigurationPageOpacity = NumericProperty(0)
    # UsersPageOpacity = NumericProperty(0)
    



    def configurationButton_click(self, ScreenManager):
        self.temperatureText = "Configuracion Selecionado"
        self.selectedButtonName = "Configuracion"
        ScreenManager.current = "ConfigurationPage"


    def usersButton_click(self, ScreenManager):
        self.temperatureText = "Usuarios Selecionado"
        self.selectedButtonName = "Usuarios"
        ScreenManager.current = "UsersPage"


    def blocksCalibrationButton_click(self, ScreenManager):
        self.temperatureText = "Calibración de Bloques Selecionado"
        self.selectedButtonName = "Calibración de Bloques"
        ScreenManager.current = "CalibrationPage"

    def resultsButton_click(self, ScreenManager):
        self.temperatureText = "Resultados Selecionado"
        self.selectedButtonName = "Resultados"
        ScreenManager.current = "ResultsPage"
        
    def patternsButton_click(self, ScreenManager):
        self.temperatureText = "Patrones Selecionado"
        self.selectedButtonName = "Patrones"
        ScreenManager.current = "PatternsPage"
    
    def createUser(self, new_user_fullname, new_user_email, new_user_phone_number):
        print("New User created with the following data:\n"+new_user_fullname+"\n"+new_user_email+"\n"+new_user_phone_number)
    
    # def changePageOpacity(self, targetPage):
    #     """Pone la opacidad de la ventana actual en cero
    #     y la objetivo la sube al maximo
    #     opciones de target:
    #         Users,
    #         Configuration
    #     """
    #     self.turnOffAllPages()
    #     match targetPage:
    #         case "Users":
    #             self.UsersPageOpacity=1
    #         case "Configuration":
    #             self.ConfigurationPageOpacity=1

    
    # def turnOffAllPages(self):
    #     """Desactiva la opacidad de todas las ventanas del menú"""
    #     self.ConfigurationPageOpacity=0
    #     self.UsersPageOpacity=0

    
    
# class UsersStackLayout(StackLayout):
#     newButtonID = 0

#     def addButton(self):
#         newButton = Button(text=str(self.newButtonID),size_hint=(1,None),height="50dp")
#         self.add_widget(newButton,index=self.newButtonID)
#         self.newButtonID +=1
# #########################
#Funciones del Back-End

#########


class JohanssonApp(App):
    """
    Clase principal de kivy,
    Usada para inicializar la GUI principal y contine 
    los parametros y funciones globales de la app
    """
    Settings = bef.loadSettings()                                   #Light                  or      Dark
    backgoundColorDarkLv10 = ColorProperty((1, 1, 1, 1))            # 1, 1, 1, 1            or      0.2, 0.2, 0.2, 1
    backgoundColorDarkLv20 = ColorProperty((0, 0, 0, 0.1))          #
    backgoundColorDarkLv30 = ColorProperty((0, 0, 0, 0.05))
    menuButtonColor        = ColorProperty((0.95, 0.95, 0.95, 1))      # 0.95, 0.95, 0.95, 1      or      0.15, 0.15, 0.15, 1
    generalButtonColor     = ColorProperty((0.1, 0.7, 0.9, 1))      # 0.1, 0.7, 0.9, 1      or      0.3, 0.3, 0.3, 1
    textboxColor           = ColorProperty((0, 0, 0, 0.05))
    textColor              = ColorProperty((0, 0, 0, 1))            # 0, 0, 0, 1            or      1, 1, 1, 1
    
    def changeTheme(self, darkThemeSwitchState):
        """"Esta funcion se encarga de realizar el cambio de Tema de color de la interfaz
            cuando se interacciona con el Switch de encendido y apagado de tema oscuro
            ubicado en configuraciones
            On(True): Tema oscuro
            Off(False): Tema claro
        """
        if darkThemeSwitchState:
            print("darktheme\n")
            self.Settings["DarkTheme"] = darkThemeSwitchState
        else:
            print("lighttheme\n")
            self.Settings["DarkTheme"] = darkThemeSwitchState
        pass
    
    def setColorTheme(self):
        bef.setColorTheme(self.Settings)


    def build(self):
        return HomeBoxLayout()

if __name__=='__main__':
    JohanssonApp().run()