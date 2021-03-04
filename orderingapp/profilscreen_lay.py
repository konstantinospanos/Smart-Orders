# -*- coding: utf-8 -*-

profil_str = '''

<ProfilScreen>:
    lv_ordersuser_box:lv_ordersuser_box.__self__
    lb_total:lb_total.__self__
    
    name:'Profil'
    FloatLayout:
        canvas.before:
            Color:
                rgb: 0,0,1,1
            Rectangle:
                pos: self.pos
                size: self.size 
        color: 1,1,1,1
        Button:#button close profil screen back menu
            text:'x'
            on_press: root.manager.current = 'menu';
            height: self.parent.height/13
            width: self.parent.width/8
            pos_hint:{'x':0.86, 'y': 0.91}
            size_hint: None, None
        Label:
            size_hint_x: 0.9
            pos_hint: {'center_x' : .5 , 'y': .75}
            size_hint_y: None
            height: self.parent.height/8

            Image:
                #source: 'data/ordering_white-01.png'
                center_x: self.parent.center_x
                center_y: self.parent.center_y
        Label:
            text: root.user_name
            font_size: self.height/4
            size_hint_x: 0.9
            size_hint_y: None
            pos_hint: {'x' : .05 , 'y': .65}
            height: self.parent.height/10
        Label:
            text:str(root.date)
            font_size: self.height/4
            size_hint_x: 0.9
            size_hint_y: None
            pos_hint: {'x' : .05 , 'y': .61}
            height: self.parent.height/10
        BoxLayout:
            canvas.before:
                Color:
                    rgba: .1,.7,.2,1
                Rectangle:
                    pos: self.pos
                    size: self.size
            id:lv_ordersuser_box
            size_hint_x: 0.9
            size_hint_y: None
            height: self.parent.height/3 
            pos_hint: {'x': .05 , 'y': .25}

        Label:  #total
            color: 1,1,1,1
            text:"Total orders"
            font_size: self.height/2
            pos_hint: {'x' : .05 , 'y': .16}
            size_hint_x: 0.5
            size_hint_y: None
            height: self.parent.height/20
            text_size: self.size

        Label:
            id:lb_total
            color: 1,1,1,1
            text: str(root.total_user)
            font_size: self.height/2
            pos_hint: {'x' : .60 , 'y': .16}
            size_hint_x: 0.5
            size_hint_y: None
            height: self.parent.height/20
            text_size: self.size

        BoxLayout:
            pos_hint: {'x' : 0 , 'y': 0}
            size_hint: 1,0.1

            BoxLayout:
                orientation:'vertical'
                Button:
                    text:'LOGOUT'
                    pos_hint: {'x' : 0 , 'y': 0}
                    size_hint: 1,0.1
                    pos: self.pos
                    size: self.size
                    on_press:root.do_logout()

'''
