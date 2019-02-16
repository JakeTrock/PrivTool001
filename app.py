import io

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MainPage(GridLayout):
	def __init__(self, **kwargs):
		super(MainPage, self).__init__(**kwargs)
		self.cols = 3
		self.rows = 3
		self.add_widget(Button(text="Connect", on_press=lambda x:self.btnTest()))

	def btnTest(self):
		print('button pressed')

class TorApp(App):
	def build(self):
		return MainPage()
	
TorApp().run()
