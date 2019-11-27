

from time import time
from kivy.app import App
from os.path import dirname, join
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty, BooleanProperty,\
    ListProperty
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Rectangle,Color
from time import gmtime, strftime
import time
			
class Time(Label):
	def updateTime(self,*args):
		self.text = time.strftime("%H:%M")
	def Aviso(self,*args):
		self.text = time.strftime("%H:%M")
		print(self.text)

class Gerenciador(ScreenManager):
	pass
class Atividades(Screen):
	def __init__(self,Atividades=[],**kwargs):
		super().__init__(**kwargs)
		for Atividade in Atividades:
			self.ids.box.add_widget(Atividade(text=Atividade))
	def AddWidget(self):
		texto = self.ids.text_Atividade.text
		Hora = self.ids.Hora_Atividade.text
		self.ids.box.add_widget(Atividade(text=texto+'-'+Hora))
		self.ids.text_Atividade.text = ''
		self.ids.Hora_Atividade.text = ''		
		

			
class Atividade(BoxLayout):
	def __init__(self,text='',**kwargs):
		super().__init__(**kwargs)
		self.ids.label.text = text
class Jogar(Screen):
	pass
class Menu(Screen):
	pass
class Comunicar(Screen):
	pass
class Comer(Screen):
    pass
class Beber(Screen):
    pass

class Dancar(Screen):
    pass

class Fumar_um(Screen):
    pass

class Brincar(Screen):
    pass

class Dormir(Screen):
    pass			
class SigninWindow(Screen):
    def __init__(self,**kwargs):
    	super().__init__(**kwargs)

    def validate_user(self):
    		user = self.ids.username_field	
    		pwd = self.ids.pwd_field
    		info = self.ids.info
    		button = self.ids.btn
    		uname = user.text
    		passw = pwd.text	

    		if uname == '' or passw == '':
    			info.text = '[color=#FF0000]username and/or password required'
    		else:
    			if uname == "Marcos" and passw == 'Marcos':
    				info.text = '[color=#00FF00]Logged in Successfully'
    				
    			else:
    				info.text = '[color=#FF0000]Invalid Username and/or password'
    				 	


class SigninApp(App):

    def build(self):
    	t = Time()
    	Clock.schedule_interval(t.updateTime,60)
    	Clock.schedule_interval(t.Aviso,1)
    	return Gerenciador()
        
            
SigninApp().run()


