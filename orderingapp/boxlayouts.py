from kivy.uix.boxlayout import BoxLayout

class Confg_lay(BoxLayout):
    
    def __init__(self, **kw):
        super(Confg_lay, self).__init__(**kw)
        
        file = open("confg.txt", "r") 
        self.confg_server_url.text = file.read()

    def change_confg_txt(self):
        file = open("confg.txt", "w")
        file.write(str(self.confg_server_url.text))
