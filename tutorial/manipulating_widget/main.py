import kivy

from kivymd.app import MDApp
from kivy.uix.label import Label

from kivy.lang import Builder


class TestApp(MDApp):
    def build(self):
        return Builder.load_file('test.kv')

    def clear_widget(self):
        self.root.ids.box_container.clear_widgets()
    
    def add_widget(self):
        self.root.ids.box_container.add_widget(Label(text='This is a new label'))


if __name__ == '__main__':
    TestApp().run()


