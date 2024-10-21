from kivymd.app import MDApp 
from kivy.lang import Builder 


class SimpleApp(MDApp):
    def build(self):
        return Builder.load_file('design.kv')


if __name__ == '__main__':
    SimpleApp().run()