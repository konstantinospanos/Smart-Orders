# -*- coding: utf-8 -*-
table_str = '''

<TableScreen>:
    addtable_obj: addtable_obj.__self__
    id:selectable
    name:'Table'

    BoxLayout:
        canvas.before:
            Color:
                rgb: 1,1,1,1
            Rectangle:
                pos: self.pos
                size: self.size
        orientation:'vertical'    

        GridLayout:
            id:addtable_obj    
            cols:2
            spacing: 10
            padding: [10]
        
        FloatLayout:
            size_hint_x: 1
            size_hint_y: None
            pos_hint: {'x' : 0,'y':0}
            canvas.before:
                Color:
                    rgb: 1,1,1,1
                Rectangle:
                    pos: self.pos
                    size: self.size

            SqrGrayBackButton:
                text:'<'
                pos_hint: {'x': .05, 'y': .38} 
                on_press: root.manager.current ='menu';
'''
