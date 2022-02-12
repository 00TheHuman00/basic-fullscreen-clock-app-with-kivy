import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.clock import Clock


class main(BoxLayout):
    def __init__(self,**x):
        super(main,self).__init__(**x)
        Clock.schedule_interval(self.clock_,1)

    def clock_(self,event):
        zaman=datetime.datetime.now()
        self.ids.label.text = "{}:{}:{}".format(zaman.hour,zaman.minute,zaman.second)

class app(App):
    def build(self):
        Window.fullscreen = "auto"
        return main()
    

app().run()
