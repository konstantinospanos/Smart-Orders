# -*- coding: utf-8 -*-
mainlayout_str = '''

<MainLayout>:
    sm:sm.__self__
    settings_btn:settings_btn.__self__
    popup_confg: popup_confg.__self__
    ScreenManager:  
        id:sm
        Screen:#first screen
            canvas.before:
                Color:
                    rgba: root.background
                Rectangle:
                    pos: self.pos
                    size: self.size
            name: 'Connect'
            id:mnlayout
            Popup:                #popup button setting url
                id: popup_confg
                size_hint: 0.8, 0.4
                on_parent: if self.parent == mnlayout: mnlayout.remove_widget(self)
            
            FloatLayout:
                Button:#button setting
                    id: settings_btn
                    text: 'settings'
                    bold: '1'
                    size_hint_x: 0.18
                    size_hint_y: None
                    height: self.parent.height/16
                    width: self.parent.height/12
                    pos_hint:{'x':0.8, 'y': 0.9}
                    background_color: 0.105, .458, .733, 1
                    background_normal: ''
                    on_release: root.popup_confg.open(); root.confg_pop();       #mainlayout open pop up
                    
                Button:
                    text: "Ordering App"
                    font_size: self.height/9
                    size_hint_x: 0.8
                    pos_hint: {'x' : .08 , 'y': .6}
                    size_hint_y: None
                    height: self.parent.height/6
                    on_press: sm.current ='Login';
                    background_color: root.background
'''
