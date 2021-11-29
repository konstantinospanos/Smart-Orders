# -*- coding: utf-8 -*-
loginscreen_str = '''

<LoginScreen>:
    name: 'Login'
    FloatLayout:
        canvas.before:
            Color:
                rgb: 1,1,1,1 
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text:'CONNECTION'
            pos_hint: {'x' : .1 , 'y': .75}
            font_size: self.height/3
            size_hint_x: 0.7
            size_hint_y: None
            height: self.parent.height/10 
            color:0,0,0,1

        TextInput:
            text:"username"
            id: us
            pos_hint: {'x' : .1 , 'y': .55}
            size_hint_x: 0.75
            size_hint_y: None
            height: self.parent.height/12
            never_selected: False
            on_focus: if self.never_selected == False: self.text = ''; self.never_selected = True                 
            
        TextInput:
            text:"password"
            id: pa
            pos_hint: {'x' : .1 , 'y': .45}
            size_hint_x: 0.75
            size_hint_y: None
            height: self.parent.height/12
            never_selected: False
            on_focus: if self.never_selected == False: self.text = ''; self.never_selected = True

        SqrGrayBackButton:# button  back first Screen
            text:'<'
            size_hint_x: None
            size_hint_y: None
            height: self.parent.height/13
            width: self.parent.width/9
            pos_hint: root.button_back_pos_hint
            on_press: root.manager.current = 'Connect'

        SqrGrayFrontButton:#check login username and password
            text:'>'
            size_hint_x: None
            size_hint_y: None
            height: self.parent.height/13
            width: self.parent.width/9
            pos_hint:root.button_front_pos_hint
            on_press: app.root.do_login(us.text, pa.text);
'''
