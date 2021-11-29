# -*- coding: utf-8 -*-
popups_str = '''
# setings url popup first screen 

<Confg_lay>:  
    confg_closer:confg_closer.__self__
    confg_back:confg_back.__self__
    confg_server_url:confg_server_url.__self__
    FloatLayout:
        canvas.before:
            Color:
                rgb: app.root.background 
            Rectangle:
                pos: self.pos
                size: self.size                
        Label:
            text:" Server Url"
            pos_hint: {'x' : .1 , 'y': .65}
            size_hint_x: 0.85
            size_hint_y: None
            font_size: self.height/3
            height: self.parent.height/6
            width: self.parent.width/6
            text_size: self.size
            halign: 'left'
            valign: 'middle'
        TextInput:
            id: confg_server_url
            font_size: self.height/3
            pos_hint: {'x' : .1 , 'y': .5}
            size_hint_x: 0.85
            size_hint_y: None
            height: self.parent.height/6
            width: self.parent.width/6
        YelDelButton:
            id: confg_back
            text: "<"
            pos_hint: {'x' : .04 , 'y': .82}
        YelDelButton:
            id: confg_closer
            text: "ΟΚ"
            pos_hint: {'x' : .82 , 'y': .06}
            on_press: root.change_confg_txt()

<EditProducts>: # Popup open choice product 
    closer: closer.__self__
    choices_oprop:choices_oprop.__self__ #id add widget listview
    comment:comment.__self__

    orientation:'vertical'
    spacing: 50
    canvas.before:
        Color:
            rgb: 1,1,1,1
        Rectangle:
            pos: self.pos
            size: self.size

    Label:#product name header
        text:app.root.order_scr.product_name
        color: [0,0,0, 0.95]
        pos_hint: {'x' : .1 , 'y': .5}
        font_size: self.height/3
        size_hint_x: 0.8
        size_hint_y: None
        height: self.parent.height/14 
        
    BoxLayout:#the listview ####choices list menu_data.py import
    
        orientation:'vertical'
        id:choices_oprop
        size_hint_x: 0.9
        size_hint_y: 0.8
        pos_hint:{'x':.04,'y':.20}
    
    TextInput:
        id:comment
        text:'ΓΡΑΨΤΕ ΣΧΟΛΙΟ ΕΔΩ'
        size_hint_x: 0.9
        size_hint_y: 0.4
        pos_hint: {'x' : .04 , 'y': .30}
        never_selected: False
        on_focus: if self.never_selected == False: self.text = ''; self.never_selected = True

    Button:
        id:closer
        text:"ok"
        on_press:root.close_pop(*args)
        size_hint_x: None
        size_hint_y: None
        pos_hint: {'x': .76, 'y': .38}
        height: self.parent.height/10
        width: self.parent.width/8
'''
