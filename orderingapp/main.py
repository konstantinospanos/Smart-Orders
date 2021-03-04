# -*- coding: utf-8 -*-
from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
from kivy.properties import StringProperty
from kivy.app import App
from mainlayout import MainLayout
       
class OrderingApp(App):

    from menu_data import datamenu
    menu = datamenu
 
    def __init__(self, *args, **kwargs):
        super(OrderingApp, self).__init__(*args, **kwargs)
                
    def on_pause(self):
        return True

    def on_resume(self):
        pass
 
    def build(self):
        main = MainLayout()
        return main
 
if __name__ == '__main__':
    OrderingApp().run()
    
