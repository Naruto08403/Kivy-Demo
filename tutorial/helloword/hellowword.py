import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='Hello world')

    def on_start(self):
        pass 

    def on_pasue(self):
        pass 

    def on_resume(self):
        pass 

    def on_stop(self):
        pass 


if __name__ == '__main__':
    MyApp().run()

