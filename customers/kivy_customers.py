kv = """

<main>:
    ScreenManagement:
        LoginScreen:
            name: 'Login'
            FloatLayout:
                canvas.before:
                    Color:
                        rgb: 1,1,1,1 
                    Rectangle:
                        pos: self.pos
                        size: self.size
                        
                Label:
                    text:'Create Customer'
                    pos_hint: {'x' : .1 , 'y': .75}
                    font_size: self.height/3
                    size_hint_x: 0.7
                    size_hint_y: None
                    height: self.parent.height/10 
                    color:0,0,0,1

                TextInput:
                    text:"firstname"
                    id: firstname
                    pos_hint: {'x' : .1 , 'y': .65}
                    size_hint_x: 0.75
                    size_hint_y: None
                    height: self.parent.height/12
                    never_selected: False
                    on_focus: if self.never_selected == False: self.text = ''; self.never_selected = True

                TextInput:
                    text:"lastname"
                    id: lastname
                    pos_hint: {'x' : .1 , 'y': .55}
                    size_hint_x: 0.75
                    size_hint_y: None
                    height: self.parent.height/12
                    never_selected: False
                    on_focus: if self.never_selected == False: self.text = ''; self.never_selected = True

                TextInput:
                    text:"phone"
                    id: phone
                    pos_hint: {'x' : .1 , 'y': .45}
                    size_hint_x: 0.75
                    size_hint_y: None
                    height: self.parent.height/12
                    never_selected: False
                    on_focus: if self.never_selected == False: self.text = ''; self.never_selected = True

                TextInput:
                    text:"mobile"
                    id: mobile
                    pos_hint: {'x' : .1 , 'y': .35}
                    size_hint_x: 0.75
                    size_hint_y: None
                    height: self.parent.height/12
                    never_selected: False
                    on_focus: if self.never_selected == False: self.text = ''; self.never_selected = True

                TextInput:
                    text:"email"
                    id: email
                    pos_hint: {'x' : .1 , 'y': .25}
                    size_hint_x: 0.75
                    size_hint_y: None
                    height: self.parent.height/12
                    never_selected: False
                    on_focus: if self.never_selected == False: self.text = ''; self.never_selected = True

                Label:
                    color:1,0,0,1
                    pos_hint: {'x' : .1 , 'y': .25}
                      
                Button:
                    text: "Registration"
                    size_hint_x: None
                    size_hint_y: None
                    height: self.parent.height/14
                    width: self.parent.width/9
                    background_color: 1,1,1,1
                    pos_hint: root.button_front_pos_hint 
                    on_press: root.customer(firstname.text,lastname.text,phone.text,mobile.text,email.text);
                    color: 0,1,0,1

"""
