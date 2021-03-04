# -*- coding: utf-8 -*-
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.adapters.listadapter import ListAdapter
from kivy.app import App
from kivy.utils import platform

import datetime
import datetime as dt
import urllib

class MenuScreen(Screen):

    button_front_pos_hint = ObjectProperty({'x': .84, 'y': .05}) 
    button_back_pos_hint = ObjectProperty({'x': .05, 'y': .05})  
    user_name = StringProperty()
    date = dt.date.isoformat(dt.date.today())
        
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)

    def ordersuser_success(self,req,result):
        app = App.get_running_app()
        total_user_orders = 0
        if result.has_key('ordersuser'):
            app.root.profil_scr.ordersuser_adapter.data = result['ordersuser']
            for item in result['ordersuser']:
                total_user_orders += float(item['total'])
            self.total_user = total_user_orders            
            app.root.profil_scr.lb_total.text = str(self.total_user)
            if platform=='android':
                app.root.PythonActivity.toastError(result['myorders'])
            else:
                print result['myorders']
        elif result.has_key('nonorder'):
            if platform=='android':
                app.root.PythonActivity.toastError(result['nonorder'])
            else:
                print result['nonorder']

    def ordersuser(self,*args): #orders users status new not pay
        app = App.get_running_app()    
        payload = {'userid': app.root.user_id}#login
        params = urllib.urlencode(payload)                       
        app.root.url_request(app.root.server_url + 'vieworders_user/'+app.root.apikey, params, self.ordersuser_success, app.root.error_request, app.root.failure_request)

