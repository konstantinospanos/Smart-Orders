from kivy.app import App
from kivy.lang import Builder
from kivy_customers import kv
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.network.urlrequest import UrlRequest 
import urllib
import platform

Builder.load_string(kv)

class ScreenManagement(ScreenManager):
    pass

class LoginScreen(Screen):
    pass

class main(BoxLayout):
    button_front_pos_hint = ObjectProperty({'x': .76, 'y': .05})
    def __init__(self,**kwargs):
        super(main, self).__init__(**kwargs)
        self.apikey = '53a209fc-d5cc-4187-bb0a-a3dd3fd641c5-5f0d14c7-8dfa-42d0-81a3-a9d051253cca'
        
    def customer_success(self, req, result):
        if result.has_key('errorobj'):
            if platform.system()=='Linux':
                print result['resp'], result['errorobj']
        elif result.has_key('newcustomer'):
            new_customer = result['newcustomer']
            if platform.system()=='Linux':
                print result['resp']
        elif result.has_key('resp'):
            if platform.system()=='Linux':
                print result['resp']

    def customer(self,firstname,lastname,phone,mobile,email):
        payload = {'firstname':firstname,'lastname':lastname,'phone':phone,'mobile':mobile,'email':email}
        params = urllib.urlencode(payload)
        req = UrlRequest('https://192.168.2.10/ordering/customersapp/customers/add_customer/'+self.apikey,
                         req_body=params,on_success=self.customer_success,verify=False)

class customer(App):
    
    def build(self):
        return main()

if __name__ == '__main__':
    customer().run()



    


