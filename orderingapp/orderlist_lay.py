# -*- coding: utf-8 -*-
orderlist_str = '''

<OrderScreen>:
    level1tv_oprop:level1tv_oprop.__self__ #treeview
    level2lv_oprop:level2lv_oprop.__self__ #listview level2
    level3lv_oprop:level3lv_oprop.__self__ #listview level3 create order
    changeorder_oprop:changeorder_oprop.__self__ #btn reference id 'Ξ Ξ‘Ξ΅Ξ‘Ξ“Ξ“Ξ•Ξ›Ξ™Ξ‘Ξ£','Ξ•Ξ�Ξ—Ξ�Ξ•Ξ΅Ξ©Ξ£Ξ•Ξ™'
    thesi_lbl: thesi_lbl.__self__
    edit_pop:my_popup.__self__

    name:'Order'
    BoxLayout:
        orientation:'vertical'
        BoxLayout:#Treview
            canvas.before:
                Color:
                    rgb: 1,1,1,1
                Rectangle:
                    pos: self.pos
                    size: self.size
            pos_hint: {'x': .0, 'y': .48}
            orientation:'horizontal'                
            id:level1tv_oprop     
            
            BoxLayout:#level.2
                id:level2lv_oprop
                canvas.before:
                    Color:
                        rgb: 1,1,1,1
                    Rectangle:
                        pos: self.pos
                        size: self.size
        FloatLayout:
            canvas.before:
                Color:
                    rgb: 0,0,0,1
                Rectangle:
                    pos: self.pos
                    size: self.size

            Label:  #total
                canvas.before:
                    Color:
                        rgb: 0,0,0,1
                    Rectangle:
                        pos: self.pos
                        size: self.size
                color: 1,1,1,1
                text:"Total"
                font_size: self.height/1
                pos_hint: {'x' : .1 , 'y': .94}
                size_hint_x: 0.5
                size_hint_y: None
                height: self.parent.height/20
                text_size: self.size

            Label:
                canvas.before:
                    Color:
                        rgb: 0,0,0,1
                    Rectangle:
                        pos: self.pos
                        size: self.size
                #id: thesi_lbl
                color: 1,1,1,1
                text: str(root.totalorder_nprop)
                font_size: self.height/1
                pos_hint: {'x' : .3 , 'y': .94}
                size_hint_x: 0.5
                size_hint_y: None
                height: self.parent.height/20
                text_size: self.size

            Label: #trapezi
                canvas.before:
                    Color:
                        rgb: 0,0,0,1
                    Rectangle:
                        pos: self.pos
                        size: self.size
                id: thesi_lbl
                color: 1,1,1,1
                font_size: self.height/1
                pos_hint: {'x' : .7 , 'y': .94}
                size_hint_x: 0.5
                size_hint_y: None
                height: self.parent.height/20
                text_size: self.size

            BoxLayout:    #order list 
                orientation:'vertical'
                id:level3lv_oprop
                size_hint_x: 0.94
                size_hint_y: 0.80
                pos_hint: {'x' : .03,'y':.13}
                
            BoxLayout:
                orientation:'horizontal'
                spacing: 10
                padding: [15,90,20,6]
                OrdGrayBackButton:
                    text:'<'
                    on_press: root.btn_back_managementorders(*args)
                BoxLayout:
                    spacing: 15
                    orientation:'horizontal'
                    pos_hint: {'x' : .1,'y':.03}
                    
                    OrdGreendelButton: #button delete
                        text:'DELETE'
                        on_press:root.delete_order(*args)
                        on_release: app.root.sm.current ='managementorders'
                    
                    OrdGreenbtnorderButton: # button change order update or new
                        id:changeorder_oprop
                        on_press:root.order_btn_press(*args)
                        on_release: app.root.sm.current = 'managementorders';

    #create popup EditProducts
    BoxLayout:
        id: boxlayout
        Popup:
            id: my_popup 
            size_hint: 0.9, 0.9
            on_parent: if self.parent == boxlayout: boxlayout.remove_widget(self)

'''
