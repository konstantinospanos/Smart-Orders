kv = """

<SqrYelButton@Button>:  
    size_hint_x: None
    size_hint_y: None
    height: self.parent.height/14
    width: self.parent.width/9
    background_color: 0.968,0.576,0.113,1
    background_normal: ''

<WhtButton@Button>: 
    size_hint_x: None
    size_hint_y: None
    height: self.parent.height/14
    width: self.parent.width/6
    background_color: 1,1,1,1
    background_normal: ''
    color: 0.968,0.576,0.113,1

<YelButton@Button>:  
    size_hint_x: None
    size_hint_y: None
    height: self.parent.height/14
    width: self.parent.width/6
    background_color: 0.968,0.576,0.113,1
    background_normal: ''

<TotalLabel@Label>:
    size_hint_x: None
    size_hint_y: None

<MainLayout>:
    sm:sm.__self__
    sm_user:sm_user.__self__
    sm_order:sm_order.__self__
    sm_account:sm_account.__self__
    lv_users_box:lv_users_box.__self__
    lv_orders_box:lv_orders_box.__self__
    acount_lbl:acount_lbl.__self__

    orientation: 'vertical'
    ScreenManager:
        id: sm
        canvas.before:
            Color:
                rgba: app.red_color
            Rectangle:
                pos: self.pos
                size: self.size       
        Screen:
            name: 'login'
            FloatLayout:
                Label:
                    text:"Username"
                    font_size: self.height/3
                    size_hint_x: 0.85
                    pos_hint: {'x' : .1 , 'y': .8}
                    size_hint_y: None
                    height: self.parent.height/14
                    text_size: self.size
                    halign: 'left'
                    valign: 'middle'
                TextInput:
                    id: username
                    font_size: self.height/2
                    pos_hint: {'x' : .1 , 'y': .75}
                    size_hint_x: 0.85
                    size_hint_y: None
                    height: self.parent.height/14 
                Label:
                    text:"Password"
                    font_size: self.height/3
                    multiline:False
                    pos_hint: {'x' : .1 , 'y': .65}
                    size_hint_x: 0.85
                    size_hint_y: None
                    height: self.parent.height/14
                    text_size: self.size
                    halign: 'left'
                    valign: 'middle'
                TextInput:
                    id: password
                    font_size: self.height/2
                    multiline:False
                    password:True
                    pos_hint: {'x' : .1 , 'y': .6}
                    size_hint_x: 0.85
                    size_hint_y: None
                    height: self.parent.height/14
                YelButton:
                    id: btm_login
                    text: "Login"
                    disabled: False
                    pos_hint: {'center_x' : .5 , 'y': .45}
                    on_press:app.do_login(username.text, password.text);  
                Label:
                    canvas.before:
                        Color:
                            rgba: 0,0,0,1
                        Rectangle:
                            pos: self.pos
                            size: self.size
                    text: app.stingmessage
                    size_hint_x: 1
                    size_hint_y: None
                    height: 30
                    pos_hint: {'left': 1 , 'bottom': 1}
        Screen:
            name: 'tabs'
            TabbedPanel:
                id:tp
                do_default_tab: False
                tab_width: self.size[0]/len(self.tab_list)
                TabbedPanelItem:
                    text: 'USERS'
                    font_size: self.height/3
                    text_size: self.size
                    halign: 'center'
                    valign: 'middle'
                    on_press: root.view_users()

                    ScreenManager:
                        id: sm_user
                        canvas.before:
                            Color:
                                rgba: app.red_color
                            Rectangle:
                                pos: self.pos
                                size: self.size

                        Screen:
                            name: 'users'
                            FloatLayout:
                                id: uslayout
                                FloatLayout:
                
                                    YelButton:
                                        text:"CREATE NEW"
                                        font_size: self.height/4
                                        pos_hint: {'x' : .78 , 'y': .9}
                                        on_press:
                                            sm_user.current = 'createuser'
                                            #btn_edituser.disabled = True
                                     

                                    #The header of list view
                                    BoxLayout:
                                        orientation: 'vertical'
                                        size_hint_x: 0.9
                                        size_hint_y: None
                                        height: self.parent.height/12
                                        pos_hint: {'x': .05 , 'y': .8}
                                        BoxLayout:
                                            Label:
                                                text: "NAME"
                                                bold: '1'
                                                font_size: self.height/4
                                                size_hint_x: .2
                                            Label:
                                                text: "LAST NAME"
                                                bold: '1'
                                                font_size: self.height/4
                                                size_hint_x: .2
                                            Label:
                                                text: "ROLE"
                                                bold: '1'
                                                font_size: self.height/4
                                                size_hint_x: .2
                                            Label:
                                                text: "EDIT"
                                                bold: '1'
                                                font_size: self.height/4
                                                size_hint_x: .2
                                            Label:
                                                text: "DELETE"
                                                bold: '1'
                                                font_size: self.height/4
                                                size_hint_x: .2
                                 
                                                
                                    #The list view           
                                    BoxLayout:
                                        id: lv_users_box
                                        size_hint_x: 0.9
                                        size_hint_y: None
                                        height: self.parent.height/1.4
                                        pos_hint: {'x': .05 , 'y': .1}

                                    Label:
                                        canvas.before:
                                            Color:
                                                rgba: 0,0,0,1
                                            Rectangle:
                                                pos: self.pos
                                                size: self.size
                                        text: app.stingmessage
                                        size_hint_x: 1
                                        size_hint_y: None
                                        height: 30
                                        pos_hint: {'left': 1 , 'bottom': 1}

                        Screen:
                                
                            name: 'createuser'
                            FloatLayout:
                                id: createuserlayout
                                FloatLayout:

                                    Label:
                                        text:" Name:"
                                        font_size: self.height/4
                                        size_hint_x: 0.45
                                        pos_hint: {'x' : .05 , 'y': .9}
                                        size_hint_y: None
                                        height: self.parent.height/14
                                        text_size: self.size
                                        halign: 'left'
                                        valign: 'middle'

                                    Label:
                                        text:" Last Name:"
                                        font_size: self.height/4
                                        size_hint_x: 0.45
                                        pos_hint: {'x' : .5 , 'y': .9}
                                        size_hint_y: None
                                        height: self.parent.height/14
                                        text_size: self.size
                                        halign: 'left'
                                        valign: 'middle'

                                    TextInput:
                                        id: firstname_txt
                                        font_size: self.height/2
                                        size_hint_x: 0.45
                                        pos_hint: {'x' : .05 , 'y': .85}
                                        size_hint_y: None
                                        height: self.parent.height/14 
                                        multiline: False

                                    TextInput:
                                        id: lastname_txt
                                        font_size: self.height/2
                                        size_hint_x: 0.45
                                        pos_hint: {'x' : .5 , 'y': .85}
                                        size_hint_y: None
                                        height: self.parent.height/14 
                                        multiline: False

                                    Label:
                                        text: " Username:"
                                        font_size: self.height/4
                                        size_hint_x: 0.9
                                        pos_hint: {'x' : .05 , 'y': .75}
                                        size_hint_y: None
                                        height: self.parent.height/14
                                        text_size: self.size
                                        halign: 'left'
                                        valign: 'middle'

                                    TextInput:
                                        id: username_txt
                                        font_size: self.height/2
                                        size_hint_x: .9
                                        pos_hint: {'x' : .05 , 'y': .7}
                                        size_hint_y: None
                                        height: self.parent.height/14
                                        text_size: self.size
                                        halign: 'left'
                                        valign: 'middle'
                                        multiline: False

                                    Label:
                                        text: " E-mail:"
                                        font_size: self.height/4
                                        size_hint_x: 0.9
                                        pos_hint: {'x' : .05 , 'y': .6}
                                        size_hint_y: None
                                        height: self.parent.height/14
                                        text_size: self.size
                                        halign: 'left'
                                        valign: 'middle'

                                    TextInput:
                                        id: email_txt
                                        font_size: self.height/2
                                        size_hint_x: .9
                                        pos_hint: {'x' : .05 , 'y': .55}
                                        size_hint_y: None
                                        height: self.parent.height/14
                                        text_size: self.size
                                        halign: 'left'
                                        valign: 'middle'
                                        multiline: False

                                    Button:
                                        id: btn_role
                                        font_size: self.height/4
                                        text: "SELECTION ROLE USER"
                                        color: 0,0,0,1 
                                        background_color: 1,1,1,1
                                        background_normal: ''
                                        size_hint_x: .45
                                        pos_hint: {'x' : .05 , 'y': .4}
                                        size_hint_y: None
                                        height: self.parent.height/14

                            FloatLayout:
                                WhtButton:
                                    text:'BACK'
                                    font_size: self.height/4
                                    pos_hint: {'x' : .05 , 'y': .1}
                                    on_press:
                                        sm_user.current = 'users'
                                        root.clear_textinputs()
                                YelButton:
                                    id: btn_change_pass
                                    disabled: False
                                    text:'CHANGE PASSWORD'
                                    font_size: self.height/4
                                    pos_hint: {'x' : .42 , 'y': .1}
                                    on_press: root.change_password()
                                YelButton:
                                    id: btn_edituser
                                    disabled: True
                                    text:'SAVE'
                                    font_size: self.height/4
                                    pos_hint: {'x' : .6 , 'y': .1}
                                    on_press: root.edit_user(firstname_txt.text,lastname_txt.text,username_txt.text, email_txt.text,btn_role.text)
                                YelButton:
                                    id: btn_createuser
                                    disabled: False
                                    text:'CREATE USER'
                                    font_size: self.height/4
                                    pos_hint: {'x' : .78 , 'y': .1}
                                    on_press:
                                        root.warning_fill_user()
                                        if firstname_txt.text!='' and lastname_txt.text!='' and username_txt.text !='' and btn_role.text!='change Users':root.create_user()
                                Label:
                                    canvas.before:
                                        Color:
                                            rgba: 0,0,0,1
                                        Rectangle:
                                            pos: self.pos
                                            size: self.size
                                    text: app.stingmessage
                                    size_hint_x: 1
                                    size_hint_y: None
                                    height: 30
                                    pos_hint: {'left': 1 , 'bottom': 1} 

                                            
                TabbedPanelItem:       
                    text: 'ORDERS'
                    font_size: self.height/3
                    text_size: self.size
                    halign: 'center'
                    valign: 'middle'
                    on_press:root.orders()
                
                    ScreenManager:
                        id: sm_order
                        canvas.before:
                            Color:
                                rgba: app.red_color
                            Rectangle:
                                pos: self.pos
                                size: self.size
                        Screen:
                            name: 'acount'
                            BoxLayout:
                                orientation: 'vertical'
                                size_hint_x: 0.9
                                size_hint_y: None
                                height: self.parent.height/12
                                pos_hint: {'x': .05 , 'y': .8}
                                BoxLayout:
                                    Label:
                                        text: "A/A"
                                        bold: '1'
                                        font_size: self.height/4
                                        size_hint_x: .2
                                    Label:
                                        text: "TABLE"
                                        bold: '1'
                                        font_size: self.height/4
                                        size_hint_x: .2
                                    Label:
                                        text: "STATUS"
                                        bold: '1'
                                        font_size: self.height/4
                                        size_hint_x: .2
                                    Label:
                                        text: "PRICE"
                                        bold: '1'
                                        font_size: self.height/4
                                        size_hint_x: .2
                                    
                            BoxLayout:
                                id: lv_orders_box
                                size_hint_x: 0.9
                                size_hint_y: None
                                height: self.parent.height/1.4
                                pos_hint: {'x': .05 , 'y': .1}

                            Label:
                                canvas.before:
                                    Color:
                                        rgba: 0,0,0,1
                                    Rectangle:
                                        pos: self.pos
                                        size: self.size
                                text: app.stingmessage
                                size_hint_x: 1
                                size_hint_y: None
                                height: 30
                                pos_hint: {'left': 1 , 'bottom': 1}
                                
                TabbedPanelItem:       
                    text: 'BILL'
                    font_size: self.height/3
                    text_size: self.size
                    halign: 'center'
                    valign: 'middle'
                    on_press:root.currentaccount()

                    ScreenManager:
                        id: sm_account
                        canvas.before:
                            Color:
                                rgba: app.red_color
                            Rectangle:
                                pos: self.pos
                                size: self.size
                        Screen:
                            name: 'account'
                            FloatLayout:
                                TotalLabel:
                                    text: "CURRENT BILL"
                                    pos_hint: {'center_x' : .5 , 'y': .7}
                                    bold: '2'
                                    font_size: self.height/5
                                TotalLabel:
                                    id:acount_lbl
                                    pos_hint: {'center_x' : .5 , 'y': .5}
                                    bold: '2'
                                    font_size: self.height/2
                                    size_hint_x: .2
                                Label:
                                    canvas.before:
                                        Color:
                                            rgba: 0,0,0,1
                                        Rectangle:
                                            pos: self.pos
                                            size: self.size
                                    text: app.stingmessage
                                    size_hint_x: 1
                                    size_hint_y: None
                                    height: 30
        
                TabbedPanelItem:
                    text: 'SETTING'
                    font_size: self.height/3
                    background_color: app.yellow_color
                    background_normal: ''
                    text_size: self.size
                    halign: 'center'
                    valign: 'middle'
                    on_press: root.view_confg()

                    FloatLayout:
                        canvas.before:
                            Color:
                                rgba: app.back_color
                            Rectangle:
                                pos: self.pos
                                size: self.size

                        FloatLayout:
                            Label:
                                text:" Server"
                                font_size: self.height/4
                                size_hint_x: 0.45
                                pos_hint: {'x' : .05 , 'y': .95}
                                size_hint_y: None
                                height: self.parent.height/14
                                text_size: self.size
                                halign: 'left'
                                valign: 'middle'
                            Label:
                                text:" URL:"
                                bold: '1'
                                font_size: self.height/4
                                size_hint_x: 0.45
                                pos_hint: {'x' : .05 , 'y': .92}
                                size_hint_y: None
                                height: self.parent.height/14
                                text_size: self.size
                                halign: 'left'
                                valign: 'middle'
                            TextInput:
                                id: url
                                font_size: self.height/2
                                size_hint_x: 0.6
                                pos_hint: {'x' : .05 , 'y': .87}
                                size_hint_y: None
                                height: self.parent.height/14 
                                multiline: False
                            YelButton:
                                text: "SAVE"
                                pos_hint: {'x' : .68 , 'y': .87}
                                on_press: root.change_confg_txt()
                            Label:
                                canvas.before:
                                    Color:
                                        rgba: 0,0,0,1
                                    Rectangle:
                                        pos: self.pos
                                        size: self.size
                                text: app.stingmessage
                                size_hint_x: 1
                                size_hint_y: None
                                height: 30
                                pos_hint: {'left': 1 , 'bottom': 1}
                TabbedPanelItem:
                    text: 'LOGOUT'
                    font_size: self.height/3
                    #background_normal: ''
                    text_size: self.size
                    halign: 'center'
                    valign: 'middle'
                    on_press: app.do_logout()
           
"""
