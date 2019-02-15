import io

from kivy.app import App
from kivy.uix.widget import Widget

class TorApp(App):
	def build(self):
		return MainPage()

class MainPage(Widget):
	pass

TorApp().run()