from kivy.uix.listview import ListItemButton
from kivy.properties import NumericProperty,StringProperty,ObjectProperty,DictProperty,BooleanProperty

class Level2ListItemButton(ListItemButton): # listview level2

    price = NumericProperty()    
    level1 = StringProperty()    
    level2 = StringProperty()    
    choices = DictProperty()     
    thesi_lbl = StringProperty() 
    
    def __init__(self, **kwargs):
        super(Level2ListItemButton, self).__init__(**kwargs)

class AddListItemButton(ListItemButton): #add product +
    pass

class RemovelistItemButton(ListItemButton): #remove product -
    pass

class EditListItemButton(ListItemButton): #edit product 
    pass

class DelListItemButton(ListItemButton): # delete product
    pass


