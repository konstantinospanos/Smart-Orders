# -*- coding: utf-8 -*-
custom_str='''
[ManagerListItem@SelectableView+BoxLayout]:#manageScreen customer Listview
    size_hint_y: None
    height: '100sp'
    index: ctx.index
    height: dp(60)
    
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            ProductListItemLabel:#product name
                text: ctx.product
                size_hint_x: 3
                size_hint_y: .3
                font_size: '11sp'

            PriceListItemLabel:#product price
                text: str(ctx.price)
                size_hint_x: 1
                size_hint_y: .3
                index: ctx.index
                font_size: '11sp'            

[OrderListItem@SelectableView+BoxLayout]: #orderScreen customer Listview 
    
    index: ctx.index
    height: dp(60)

    ProductListItemLabel:#product name
        canvas.before:
            Color:
                rgb: 0.968,0.576,0.113,1
            Rectangle:
                pos: self.pos
                size: self.size
        text: ctx.product 
        size_hint_x: 3
        size_hint_y: .3
        font_size: '11sp'

    AddListItemButton:#add product
        text: '+'
        size_hint_x: 1
        size_hint_y: .3
        get_id: ctx.index 
        on_press:app.root.order_scr.add_product(*args)

    QuantityListItemLabel:# quantity product 
        size_hint_x: 1
        size_hint_y: .3
        text: str(ctx.quantity)

    RemovelistItemButton: # subtraction product
        text: '-'
        size_hint_x: 1
        size_hint_y: .3
        get_id: ctx.index
        on_press:app.root.order_scr.remove_product(*args)
        
    EditListItemButton: #edit product choices open popup, popup_lay<EditProducts>
        size_hint_x: 1
        size_hint_y: .3
        get_id: ctx.index
        text: 'edit'
        on_press:app.root.order_scr.openchoice_pop(*args)

    DelListItemButton:# delete product 
        size_hint_x: 1
        size_hint_y: .3
        text: 'x'
        get_id: ctx.index
        on_press:app.root.order_scr.delete_product(*args)

'''
