# -*- coding: utf-8 -*-
Ordermanagement_str = '''

<Ordermanagement>:
    items_acc:items_acc.__self__
    name:'managementorders'
    canvas.before:
        Color:
            rgba: .1,.7,.2,1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:# listview 
        orientation: 'vertical'
        size_hint_x: 0.9
        size_hint_y: None
        height: self.parent.height/1.3
        pos_hint: {'x': .05 , 'y': .2}
        id:items_acc
    BoxLayout:
        spacing: 10
        size_hint_x: 0.9
        size_hint_y: None
        pos_hint: {'x' : .05,'y':.1}
        height: self.parent.height/15
        Label:  #total
            color: 1,1,1,1
            text:"Total"
        Label:
            color: 1,1,1,1
            text: str(root.total_orders)

        SqrYelButton:
            size_hint_x: 0.9
            #pos_hint: {'x' : 1,'y':25}
            text:'pay_all'
            on_press:root.pay_all(*args)

    FloatLayout:
        MngGrayBackButton:
            text:'<'
            on_release: app.root.sm.current ='Table';
            on_press: root.btn_backtable()
        MngGrayFrontButton:
            text:'ΠΡΟΣΘΗΚΗ'
            on_press:root.btn_addorder()
            on_release: app.root.sm.current = 'Order';

'''
