##-*- coding: utf-8 -*-
items_str = '''

<SqrYelButton@Button>:#yellow button pay all managerscreen
    size_hint_x: None
    size_hint_y: None
    height: 40 
    width: 40 
    background_color: 0.968,0.576,0.113,1
    background_normal: ''
    
<MyListItemButton>: # custombusttons listview on detailsorders user screen profil
    color: [0,0,0, 0.95]
    selected_color: 1,1,1, 0.75
    deselected_color: 1,1,1, 0.5
    background_color: 1,1,1, 0.4
    size: (100, '48dp')

<YelDelButton@Button>:# two buttons popup first screen 
    size_hint: .15, .15
    background_color: 0.968,0.576,0.113,1
    background_normal: ''

<SqrGrayBackButton@Button>:  #button back '<'
    size_hint_x: None
    size_hint_y: None
    height: self.parent.height/14
    width: self.parent.width/9
    pos_hint: {'x': .05, 'y': .38}

<SqrGrayFrontButton@Button>: # button next '>'
    size_hint_x: None
    size_hint_y: None
    height: self.parent.height/14
    width: self.parent.width/9
    pos_hint: {'x': .84, 'y': .38}

<MngGrayBackButton@Button>: #button managerscreen back table_screen
    size_hint_x: None
    size_hint_y: None
    height: self.parent.height/13
    width: self.parent.width/9
    pos_hint:{'x': .05, 'y': .03}

<MngGrayFrontButton@Button>: #button managerscreen front order
    size_hint_x: None
    size_hint_y: None
    height: self.parent.height/13
    width: self.parent.width/2
    pos_hint:{'x': .45, 'y': .03}

<Level2ListItemButton>: # level2 listview 
    height: max(self.texture_size[1] + dp(40), dp(14))
    color: [0,0,0, 0.95]
    selected_color: 1,1,1, 0.75
    deselected_color: 1,1,1, 0.5
    background_color: 1,1,1, 0.4
    #size: (100, '48dp') scroll

<TreeViewButton>: # leve1 treeview
    color: [0,0,0, 0.95]
    selected_color: 1,1,1, 0.75
    deselected_color: 1,1,1, 0.5
    background_color: 1,1,1, 0.4

<OrdGrayBackButton@Button>: #button orderscreen back tablescreen or managerscreen
    pos_hint: {'x' : .1,'y':.03}
    height: self.parent.height/13
    width: self.parent.width/8
    size_hint: [.1,.1]

<OrdGreendelButton@Button>: # button 'delete orders'  
    size_hint: [.1,.1]
    background_color: 0.247,0.749,0.489,1
    background_normal: ''
    color: 0,0,0,1

<OrdGreenbtnorderButton@Button>: # button 'send orders','update'
    size_hint: [.1,.1]
    background_color: 0.247,0.749,0.489,1
    background_normal: ''
    color: 0,0,0,1

'''
