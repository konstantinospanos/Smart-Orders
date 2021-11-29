# -*- coding: utf-8 -*-
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty,NumericProperty
from kivy.uix.button import Button
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import CompositeListItem,ListView,ListItemLabel,ListItemButton,ListView,SelectableView
from listitemlabel import TableListItemLabel,TotalListItemLabel
import datetime
import datetime as dt
from kivy.app import App
import urllib

class ProfilScreen(Screen):

    total_user = NumericProperty()
    date = dt.date.isoformat(dt.date.today())
    user_name = StringProperty()
    lv_ordersuser_box = ObjectProperty()
    lb_total = ObjectProperty()

    
    def __init__(self, *args, **kwargs):

        super(ProfilScreen,self).__init__(*args, **kwargs)
        self.ordersuser_converter = lambda row_index, rec:{'text':rec['table'],'on_press':self.details_table}
        self.ordersuser_adapter = ListAdapter(data=[],
                            args_converter=self.ordersuser_converter,
                            selection_mode='single',
                            allow_empty_selection=True,
                            cls='MyListItemButton')

        list_view_ordersuser = ListView(adapter = self.ordersuser_adapter)
        self.lv_ordersuser_box.add_widget(list_view_ordersuser)
    
    def details_table_success(self,req,result): 

        app = App.get_running_app()
        if result.has_key('resp'):
            orderstable = result['allorderstable']          
            app.root.management_scr.createaccordion(orderstable)
            app.root.sm.current = 'managementorders'

    def details_table(self,btn): # view orders not pay
        app = App.get_running_app()
        tableusers = 'ΤΡΑΠΕΖΙ'.decode('utf8') +" "+ btn.text.split(u'Ι')[1]
        app.root.order_scr.thesi_lbl.text = tableusers
        payload = {'table':btn.text.split(u'Ι')[1]}      
        params = urllib.urlencode(payload)
        if app.root.apikey:                    
            app.root.url_request(app.root.server_url.replace("\n","") + 'details/'+app.root.apikey, params, self.details_table_success, app.root.error_request, app.root.failure_request)

    def do_logout(self):
        app = App.get_running_app()
        app.root.sm.current = 'Login'
        app.root.login_scr.ids.us.text = ''
        app.root.login_scr.ids.pa.text = ''
           
class MyListItemButton(ListItemButton,SelectableView):
    pass
