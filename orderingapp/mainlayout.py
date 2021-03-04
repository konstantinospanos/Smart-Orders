# -*- coding: utf-8 -*-
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.network.urlrequest import UrlRequest
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, NumericProperty, StringProperty, ListProperty, BooleanProperty,DictProperty
from kivy.utils import platform
#from jnius import autoclass
from boxlayouts import Confg_lay
from ordering_lay import mainlayout_str
from loginscreen_lay import loginscreen_str
from menuscreen_lay import menu_str
from profilscreen_lay import profil_str
from tablesscreen_lay import table_str
from management_orders_lay import Ordermanagement_str
from orderlist_lay import orderlist_str
from popups_lay import popups_str
from items_lay import items_str
from customerlistitems_lay import custom_str
import urllib

Builder.load_string(mainlayout_str)
Builder.load_string(loginscreen_str)
Builder.load_string(menu_str)
Builder.load_string(profil_str)
Builder.load_string(table_str)
Builder.load_string(Ordermanagement_str)
Builder.load_string(orderlist_str)
Builder.load_string(popups_str)
Builder.load_string(items_str)
Builder.load_string(custom_str)

from loginscreen import LoginScreen
from menuscreen import MenuScreen
from profilscreen import ProfilScreen
from tablesscreen import TableScreen
from managements_orders import Ordermanagement
from orderlist import OrderScreen

class MainLayout(BoxLayout):
    background = ListProperty([0.611, 0.124, 0.124, 1.0]) #red Color
    sm = ObjectProperty()# id reference change Screen
    settings_btn = ObjectProperty()
    addtable = ObjectProperty()# create table button 
    customer_id = StringProperty()
    user_id = StringProperty()

    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        file = open("confg.txt", "r")
        self.server_url = file.read()
        
        if platform == "android":
            #from android import activity
            self.PythonActivity = autoclass('org.kivy.android.PythonActivity')

        self.apikeydefault = 'bcc718ab-bc12-4232-9184-f68a1e6b308f-3fdb4ffd-70b4-4909-aa41-9ee34050f0ec'
        self.login_screen_setup()       #2
        self.menu_screen_setup()        #3
        self.profil_screen_setup()      #4
        self.table_screen_setup()       #5
        self.management_screen_setup()  #6
        self.order_screen_setup()       #7

    def login_screen_setup(self):       ########### Screen 2 ##########
        self.login_scr = LoginScreen()
        self.sm.add_widget(self.login_scr)

    def menu_screen_setup(self):        ########### Screen 3 ##########
        self.menu_scr = MenuScreen()
        self.sm.add_widget(self.menu_scr)

    def profil_screen_setup(self):      ############ Screen 4 ##########
        self.profil_scr = ProfilScreen()
        self.sm.add_widget(self.profil_scr)
    
    def table_screen_setup(self):       ########### Screen 5 ##########
        self.table_scr = TableScreen()
        self.sm.add_widget(self.table_scr)

    def management_screen_setup(self):   ########### Screen 6 ##########
        self.management_scr = Ordermanagement()
        self.sm.add_widget(self.management_scr)

    def order_screen_setup(self):        ########### Screen 7 ##########
        self.order_scr = OrderScreen()
        self.sm.add_widget(self.order_scr)

    def closer_confg_callback(self, *args):  ########### Screen1 close pop up ##########
        self.popup_confg.dismiss()

    def confg_pop(self): 
        popup_content = Confg_lay()
        self.popup_confg.content = popup_content
        self.popup_confg.title = u"Settings"
        self.popup_confg.auto_dismiss=False
        popup_content.confg_closer.bind(on_release = self.closer_confg_callback)
        popup_content.confg_back.bind(on_release = self.closer_confg_callback)


    def do_login_success(self, req, result): ########### Screen2 ##########
        if result.has_key(u'userdict'):
            user = result['userdict']
            self.apikey = str(user['api_key'])
            self.user_id = str(user['_id'])
            self.customer_id = str(user['customer_id'])
            self.user_name = str(user[u'username'])
            self.sm.current = 'menu'
            if platform=='android':
                self.PythonActivity.toastError('Επιτυχής Σύνδεση')
            else:
                print 'Επιτυχής Σύνδεση'
        else:
            self.connection = "Σύνδεση"
            if platform=='android':
                self.PythonActivity.toastError(result['resp'])
            else:
                print result['resp']
            
    def do_login(self, user, passwd): ########### Screen2 ##########
        payload = {'username': user, 'password': passwd} #,'datamenu':json.dumps(datamenu)
        params = urllib.urlencode(payload)
        if platform == 'android':
            self.PythonActivity.toastError('Γίνεται Σύνδεση')
        else:
            print 'Γίνεται Σύνδεση'
        self.url_request(self.server_url + 'login/'+self.apikeydefault, params, self.do_login_success, self.error_request, self.failure_request)
        
    def url_request(self, url, params, success_callback, error_callback, failure_callback, ca_file=None, verify=False):
        if platform == "android":
            if self.check_connectivity():
                UrlRequest(url, req_body=params, on_success=success_callback, on_error=error_callback, on_failure = failure_callback,on_redirect=None,req_headers=None,ca_file= ca_file,verify= verify)
            else:
                self.PythonActivity.toastError('Δεν υπάρχει σύνδεση')
        else:
            UrlRequest(url, req_body=params, on_success=success_callback, on_error=error_callback, on_failure = failure_callback,on_redirect=None,req_headers=None,ca_file= ca_file,verify= verify)

    def check_connectivity(self):
        activity = autoclass('org.kivy.android.PythonActivity').mActivity
        Context = autoclass('android.content.Context') 
        cm = activity.getSystemService(Context.CONNECTIVITY_SERVICE)
        if cm:
            info = cm.getActiveNetworkInfo()
            if info:
                return info.isConnectedOrConnecting()
        return False 

    def error_request(self, req, error):
        if platform == "android":
            self.PythonActivity.toastError(str(error))
        else:
            print str(error)

    def failure_request(self, req, result):
        if platform == "android":
            self.PythonActivity.toastError("Failure: Client or Server Error.")
        else:
            print 'Failure: Client or Server Error.'

