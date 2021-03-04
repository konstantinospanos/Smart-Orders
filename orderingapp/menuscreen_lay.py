# -*- coding: utf-8 -*-

menu_str = '''
<MenuScreen>:
    name:'menu'
    FloatLayout:
        Label:
            size_hint_x: 0.9
            pos_hint: {'x' : .05 , 'y': .78}
            size_hint_y: None
            height: self.parent.height/8
            Image:
                source: 'data/ordering_white-01.png'
                center_x: self.parent.center_x
                center_y: self.parent.center_y
        Label:
            canvas.before:
                Color:
                    rgb: 0,0,0,1
                Rectangle:
                    pos: self.pos
                    size: self.size 
            color: 1,1,1,1
            text: str(root.date)
            font_size: self.height/5
            size_hint_x: 0.9
            size_hint_y: None
            pos_hint: {'x' : .05 , 'y': .63}
            size_hint_y: None
            height: self.parent.height/6
            
        Button:
            text: "orders user"
            font_size: self.height/5
            size_hint_x: 0.9
            pos_hint: {'x' : .05 , 'y': .37}
            size_hint_y: .2
            on_press: root.manager.current ='Profil'
            on_press: root.ordersuser()
            height: self.parent.height/6 

        Label:
            text: root.user_name
            font_size: self.height/5
            size_hint_x: 0.9
            pos_hint: {'x' : .05 , 'y': .32}
            size_hint_y: .2
            height: self.parent.height/6
            
        Button:
            text: "select table"
            font_size: self.height/5
            size_hint_x: 0.9
            pos_hint: {'x' : .05 , 'y': .15}
            size_hint_y: .2
            height: self.parent.height/6
            on_press: root.manager.current ='Table';

        SqrGrayBackButton:
            text:'<'
            size_hint_x: None
            size_hint_y: None
            height: self.parent.height/13
            width: self.parent.width/9
            pos_hint: root.button_back_pos_hint
            on_press: root.manager.current = 'Login'
'''
