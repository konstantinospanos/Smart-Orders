# -*- coding: utf-8 -*-
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty,StringProperty

class LoginScreen(Screen):

    button_front_pos_hint = ObjectProperty({'x': .84, 'y': .05}) 
    button_back_pos_hint = ObjectProperty({'x': .05, 'y': .05})

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
