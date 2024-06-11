from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class TestWindow(BoxLayout):
    pass

class TestApp(App):
    
    def build(self):
        return Button(text= 'hello world')

if __name__ == "__main__":
    x = TestApp()
    x.run()
