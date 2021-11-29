# -*- coding: utf-8 -*-
from kivy.config import Config
Config.set('graphics', 'width', '650')
Config.set('graphics', 'height', '650')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.lang import Builder
from kv_orderingatools import kv
from kivy.utils import platform
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.properties import ObjectProperty,ListProperty,StringProperty
from kivy.uix.listview import ListView
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import CompositeListItem,ListItemLabel,ListItemButton
from kivy.network.urlrequest import UrlRequest
import urllib
import datetime

Builder.load_string(kv)

class MainLayout(BoxLayout):
    sm = ObjectProperty()
    tp = ObjectProperty()
    sm_user = ObjectProperty()
    sm_order = ObjectProperty()
    sm_account = ObjectProperty()
    account = ObjectProperty()
    acount_lbl = ObjectProperty()
    lv_users_box = ObjectProperty()
    lv_orders_box = ObjectProperty()
    graph_days = ObjectProperty()
    btn_pie = ObjectProperty()
    pie_current = ObjectProperty()
    dr_users = DropDown()

    useroles = ['manager','user']
    dr_role = DropDown()

    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        
        self.args_converter = lambda row_index, rec: \
        {'size_hint_y': None,
        'height': 30,
         'spacing':8,
        'is_selected':False,
        'cls_dicts': [{'cls':ListItemLabel,
                        'kwargs': {'text': rec['firstname'],'size_hint_x': .2,'size_hint_y': None,'height': 25, 'font_size': '12sp'}},
                      {'cls': ListItemLabel,
                        'kwargs': {'text': rec['lastname'],'size_hint_x': .2,'size_hint_y': None,'height': 25,'font_size': '12sp'}},
                      {'cls': ListItemLabel,
                        'kwargs': {'text': rec['role'],'size_hint_x': .2,'size_hint_y': None,'height': 25,'font_size': '12sp'}},
                      {'cls': MyListItemButton,
                        'kwargs': {'text': u'edit','size_hint_x': .2,'size_hint_y': None,'height': 25,'font_size': '12sp', 'disabled': False,
                                  'on_press':self.find_user}}, 
                      {'cls': MyListItemButton,
                        'kwargs': {'text': u'delete','size_hint_x': .2,'size_hint_y': None,'height': 25,'font_size': '12sp','disabled': False, 
                                  'on_press':self.delete_user}},
                      ]}
    
        self.list_adapter = ListAdapter(data=[],
                               args_converter=self.args_converter,
                               selection_mode='none',
                               allow_empty_selection=True,
                                   cls=CompositeListItem)

        list_view = ListView(adapter= self.list_adapter)
        self.lv_users_box.add_widget(list_view)

        self.args_converter_order = lambda row_index, rec: \
        {'size_hint_y': None,
        'height': 30,
         'spacing':8,
        'is_selected':False,
        'cls_dicts': [{'cls':ListItemLabel,
                        'kwargs': {'text': str(row_index+1),'size_hint_x': .2,'size_hint_y': None,'height': 25, 'font_size': '12sp'}},
                      {'cls': ListItemLabel,
                        'kwargs': {'text': rec['table'],'size_hint_x': .2,'size_hint_y': None,'height': 25,'font_size': '12sp'}},
                      {'cls': ListItemLabel,
                        'kwargs': {'text': rec['status'],'size_hint_x': .2,'size_hint_y': None,'height': 25,'font_size': '12sp'}},
                      {'cls': ListItemLabel,
                        'kwargs': {'text': str(rec['total']),'size_hint_x': .2,'size_hint_y': None,'height': 25,'font_size': '12sp'}}, 
                      ]}
    
        self.order_adapter = ListAdapter(data=[],
                               args_converter=self.args_converter_order,
                               selection_mode='none',
                               allow_empty_selection=True,
                                   cls=CompositeListItem)

        self.list_view_order = ListView(adapter = self.order_adapter)
        self.lv_orders_box.add_widget(self.list_view_order)

        self.choice_role_user()#dropdown
        
    def view_users(self):
        app = App.get_running_app()
        self.list_adapter.data = app.allusers
        
    def orders_success(self, req, result):
        if result.has_key('orderlist'):
            self.order_adapter.data = result['orderlist']

    def orders(self,*args):
        app = App.get_running_app()
        payload = {'customerid': app.customerid}
        params = urllib.urlencode(payload)
        app.url_request(app.server_url.replace("\n","") + 'view_order/'+app.apikey,params,
                        self.orders_success, app.error_request, app.failure_request)
        
    def currentaccount_success(self,req,result):
        app = App.get_running_app()
        if result.has_key('statuspay'):
            self.acount_lbl.text = str(result['statuspay'])
        elif result.has_key('status'):
            app.stingmessage = result['status'].encode('UTF-8')
        
    def currentaccount(self,*args):
        app = App.get_running_app()
        payload = {'customerid': app.customerid}
        params = urllib.urlencode(payload)
        app.url_request(app.server_url.replace("\n","") + 'account/'+app.apikey, params,
                        self.currentaccount_success,app.error_request, app.failure_request)
                 
    def choice_role_user(self):
        self.ids.btn_role.bind(on_release = self.dr_role.open)
        self.dr_role.bind(on_select=lambda instance, x: setattr(self.ids.btn_role, 'text', x.encode('UTF-8')))
        self.dr_role.clear_widgets()
        for i in self.useroles:
            b = Button(text=i,size_hint_y=None, height=35, font_size='12sp', background_color= (0.968,0.576,0.113,1),background_normal=('') )
            self.dr_role.add_widget(b)
            b.bind(on_release = lambda b: self.dr_role.select(b.text))

    def clear_textinputs(self):  
        self.ids.firstname_txt.text=''
        self.ids.lastname_txt.text=''
        self.ids.username_txt.text=''
        self.ids.email_txt.text=''
        self.ids.btn_role.text='SELECTION ROLE USER'

    def warning_fill_user(self):
        app = App.get_running_app()
        if self.ids.firstname_txt.text=='':
            app.stingmessage = 'Please fill in a name'
        elif  self.ids.lastname_txt.text=='':
            app.stingmessage = 'Please fill in a last name'
        elif  self.ids.username_txt.text=='':
            app.stingmessage = 'Please fill in a username'
        elif self.ids.btn_role.text=='SELECTION ROLE USER':
            app.stingmessage = 'Please fill in a role user'

    def change_password_success(self, req, result):
        app = App.get_running_app()
        if result.has_key('resp'):
            app.stingmessage = result['resp']
            self.list_adapter.data = result['allusers']

    def change_password(self):
        app = App.get_running_app()
        if app.apikey:
            payload = {'firstname':self.ids.firstname_txt.text.encode('UTF-8'), 
                       'lastname':self.ids.lastname_txt.text.encode('UTF-8'),
                       'username':self.ids.username_txt.text, 'email':self.ids.email_txt.text, 
                       'role':self.ids.btn_role.text.encode('UTF-8'), 'usereditid':self.user_edit_id}
            params = urllib.urlencode(payload)
            app.url_request(app.server_url.replace("\n","") + 'users/changepass/'+app.apikey,  params, 
                            self.change_password_success, on_error=app.error_request, 
                            on_failure = app.failure_request, verify=False)
            self.ids.btn_change_pass.disabled = True

    def create_user_success(self, req, result):
        app = App.get_running_app()
        if result.has_key('resp'):
            app.stingmessage = result['resp'].encode('UTF-8')
            Clock.schedule_once(app.timer, 10)
            if result.has_key('allusers'):
                self.list_adapter.data = result['allusers']
                
    def create_user(self, *args):
        app = App.get_running_app()
        payload = {'firstname':self.ids.firstname_txt.text.encode('UTF-8'), 
                   'lastname':self.ids.lastname_txt.text.encode('UTF-8'),
                   'username':self.ids.username_txt.text,'email':self.ids.email_txt.text, 
                   'role':self.ids.btn_role.text.encode('UTF-8')}
        params = urllib.urlencode(payload)
        if app.apikey:
            app.url_request(app.server_url.replace("\n","") + 'users/createuser/'+app.apikey, params, 
                            self.create_user_success,
                            app.error_request,app.failure_request)

    def delete_user_success(self, req, result):
        app = App.get_running_app()
        if result.has_key('resp'):
            app.stingmessage = result['resp']
            Clock.schedule_once(app.timer, 5)
            self.list_adapter.data = result['allusers']
        
    def delete_user(self, btn, *args):
        app = App.get_running_app()
        row_id = btn.index
        user_id = self.list_adapter.data[row_id]['user_id']
        payload = {'userid':user_id}
        params = urllib.urlencode(payload)
        if app.apikey:
            app.url_request(app.server_url.replace("\n","") + 'users/deleteuser/'+app.apikey, params, 
                            self.delete_user_success,
                            app.error_request,  app.failure_request)
   
    def change_password_success(self, req, result):
        app = App.get_running_app()
        if result.has_key('resp'):
            app.stingmessage = result['resp']
            Clock.schedule_once(app.timer, 5)
            if result.has_key('allusers'):
                self.list_adapter.data = result['allusers']

    def change_password(self):
        app = App.get_running_app()
        if app.apikey:
            payload = {'firstname':self.ids.firstname_txt.text.encode('UTF-8'), 
                       'lastname':self.ids.lastname_txt.text.encode('UTF-8'),
                       'username':self.ids.username_txt.text, 'email':self.ids.email_txt.text, 
                       'role':self.ids.btn_role.text.encode('UTF-8'), 'usereditid':self.user_edit_id}
            params = urllib.urlencode(payload)
            app.url_request(app.server_url.replace("\n","") + 'users/changepass/'+app.apikey,  params, 
                            self.change_password_success,
                            app.error_request, app.failure_request)

    def edit_user_success(self, req, result):
        app = App.get_running_app()
        if result.has_key('resp'):
            app.stingmessage = result['resp']
            Clock.schedule_once(app.timer, 5)
            self.list_adapter.data = result['allusers']

    def edit_user(self, firstname, lastname, username, email, role):
        app = App.get_running_app()
        if app.apikey:
            payload = {'firstname':firstname.encode('UTF-8'), 'lastname':lastname.encode('UTF-8'),
                       'username':username,'email':email, 'role':role.encode('UTF-8'), 
                       'usereditid':self.user_edit_id}
            params = urllib.urlencode(payload)
            app.url_request(app.server_url.replace("\n","") + 'users/edituser/'+app.apikey,  params, 
                            self.edit_user_success,
                            app.error_request, app.failure_request)
                      
    def find_user(self, btn, *args):
        row_id = btn.index
        self.user_edit_id = self.list_adapter.data[row_id]['user_id']
        self.sm_user.current = 'createuser'
        self.ids.btn_createuser.disabled = True
        self.ids.btn_edituser.disabled = False
        self.ids.firstname_txt.text = self.list_adapter.data[row_id]['firstname']
        self.ids.lastname_txt.text = self.list_adapter.data[row_id]['lastname']
        self.ids.username_txt.text = self.list_adapter.data[row_id]['username']
        self.ids.email_txt.text = self.list_adapter.data[row_id]['email']
        self.ids.btn_role.text = self.list_adapter.data[row_id]['role'].encode('UTF-8')

    def view_confg(self):
        file = open("confg.txt", "r")
        self.ids.url.text = file.read()

    def change_confg_txt(self):
        file = open("confg.txt", "w")
        file.write(str(self.ids.url.text))

class MyListItemButton(ListItemButton):
    pass
    
class OrderingApp(App):
    red_color = ListProperty([0.721, 0.137, 0.137, 1]) #red Color
    back_color = ListProperty([0.105, .458, .733, 1]) #Blue Color
    yellow_color = ListProperty([0.968,0.576,0.113,1]) #Yellow Color
    stingmessage = StringProperty()

    file = open("confg.txt","r")
    server_url = file.read()
    
    def __init__(self, *args, **kwargs):
        super(OrderingApp, self).__init__(*args, **kwargs)
        self.apikeydefault = 'api_key'

    def error_request(self, req, error):
        self.stingmessage = str(error)
    
    def failure_request(self, req, result):
        self.stingmessage = 'Failure: Client or Server Error.'

    def timer(self, dt):
        self.stingmessage = ''

    def do_login_success(self, req, result):
        if result.has_key(u'userdict'):
            self.user = result['userdict']
            self.apikey = str(self.user['api_key'])
            self.userid = self.user['_id']
            self.customerid = self.user['customer_id']
            self.allusers = result['allusers']
            self.root.sm.current = 'tabs'
            self.stingmessage = 'Successful Connection'
        else:
            self.stingmessage = result['resp']
            
        Clock.schedule_once(self.timer, 5)
    
    def do_login(self, username, password):
        app = App.get_running_app()
        payload = {'username': username, 'password': password}
        params = urllib.urlencode(payload)
        self.stingmessage = 'Wait for connection'
        self.url_request(self.server_url.replace("\n","") + 'login/'+self.apikeydefault, params, 
                         self.do_login_success, self.error_request, self.failure_request)
    
    def url_request(self, url, params, success_callback, error_callback, failure_callback, 
                    ca_file=None, verify=False):
        if platform == "android":
            if self.check_connectivity():
                UrlRequest(url, req_body=params, on_success=success_callback, on_error=error_callback,
                            on_failure = failure_callback,on_redirect=None,req_headers=None,
                            ca_file= ca_file,verify= verify)
            else:
                self.PythonActivity.toastError('Incorrect Connection')
        else:
            UrlRequest(url, req_body=params, on_success=success_callback, on_error=error_callback,
                        on_failure = failure_callback,on_redirect=None,req_headers=None,
                        ca_file= ca_file,verify= verify)

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

    def do_logout(self):
        self.root.sm.current = 'login'
        self.root.ids.username.text = ''
        self.root.ids.password.text = ''
        self.stingmessage = 'Logout'
        
    def build(self):
        return MainLayout()


if __name__ == '__main__':
    OrderingApp().run()
