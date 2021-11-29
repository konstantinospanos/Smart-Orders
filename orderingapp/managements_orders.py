# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty,NumericProperty,StringProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.listview import ListView,ListItemLabel,ListItemButton
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import SelectableView
from functools import partial
from listitemlabel import ProductListItemLabel,PriceListItemLabel
from kivy.utils import platform
import urllib

class Ordermanagement(Screen):
    total_orders = NumericProperty()
    items_acc = ObjectProperty()        #accordion  BoxLayout id reference
    order_id = StringProperty()
    lv_accordion = ObjectProperty()

    def __init__(self, **kwargs):
        super(Ordermanagement, self).__init__(**kwargs)

    def createaccordion(self,orderstable): #accordion view orders
        app = App.get_running_app()
        self.myaccordion = Accordion(orientation='vertical',size_hint=(1.0, 1.0))
        if type(orderstable)==list:             #new orders save view accordion
            for element in orderstable:
                orderid =  element['_id']
                acc_item = MyAccordionItem(title='order')
                self.lv_accordion = ListView()              #listview inside accordion

                args_converter_accordion = lambda row_index, rec: \
                {'product':rec['product_name'],
                 'price':rec['price'],
                 'mychoices':rec['mychoices']}

                lvaccordion_adapter = ListAdapter(data=[],
                            args_converter = args_converter_accordion,
                            selection_mode='none',
                            allow_empty_selection=True,
                            cls='ManagerListItem')

                self.lv_accordion.adapter = lvaccordion_adapter
                acc_item.add_widget(self.lv_accordion) 
                self.lv_accordion.adapter.data = element['items'] 
                acc_item.add_widget(SqrYelButton(text='pay',pos_hint={'x': .2, 'y': .10},
                                                 on_press=partial(self.pay_order,orderid)))
                acc_item.add_widget(SqrYelButton(text='edit',pos_hint={'x': .2, 'y': .10},
                                                 on_press=partial(self.edit,orderid)))
                self.myaccordion.add_widget(acc_item)
        else:                                                   #view for update view accordion
            orderid =  orderstable['_id']
            acc_item = MyAccordionItem(title='order')  
            self.lv_accordion = ListView()
            args_converter_accordion = lambda row_index, rec: \
            {'product':rec['product_name'],
            'price':rec['price'],
            'mychoices':rec['mychoices']}
            
            lvaccordion_adapter = ListAdapter(data=[],
                        args_converter = args_converter_accordion,
                        selection_mode='none',
                        allow_empty_selection=True,
                        cls='ManagerListItem')

            self.lv_accordion.adapter = lvaccordion_adapter
            acc_item.add_widget(self.lv_accordion)
            self.lv_accordion.adapter.data = orderstable['items']
            acc_item.add_widget(SqrYelButton(text='pay',pos_hint={'x': .2, 'y': .10},
                                             on_press=partial(self.pay_order,orderid)))
            acc_item.add_widget(SqrYelButton(text='edit',pos_hint={'x': .2, 'y': .10},
                                             on_press=partial(self.edit,orderid)))
            self.myaccordion.add_widget(acc_item)
            
        self.total_order()
        app.root.management_scr.items_acc.add_widget(self.myaccordion)
            
    def total_order_success(self,req,result):
        if result.has_key('totalorder'):
            self.total_orders = result['totalorder']
            
    def total_order(self,*args):
        app = App.get_running_app()
        payload = {'table':app.root.order_scr.thesi_lbl.text.split(' ')[1]} 
        params = urllib.urlencode(payload)
        app.root.url_request(app.root.server_url.replace("\n","") + 'total/'+app.root.apikeydefault, params, self.total_order_success, app.root.error_request, app.root.failure_request)
        
    def edit(self,orderid,btn,*args): #get order in orderlist
        app = App.get_running_app()
        lv = btn.parent.children[2]
        order = lv.adapter.data
        app.root.order_scr.level3_adapter.data = order
        self.order_id = orderid
        app.root.order_scr.changeorder_oprop.text = 'UPDATE ORDER' #change button to update order
        count = 0
        for items in order:
            count += items['price']
        app.root.order_scr.totalorder_nprop = count
        app.root.sm.current = 'Order'

    def pay_order_success(self,req,result):      
        app = App.get_running_app()    
        if result.has_key('resp'):
            self.total_order()
            if platform=='android':
                app.root.PythonActivity.toastError(result['resp'])
            else:
                print result['resp']

    def pay_order(self,orderid,btn,*args):
        app = App.get_running_app()               
        payload = {'order_id':orderid}
        params = urllib.urlencode(payload)
        app.root.url_request(app.root.server_url.replace("\n","") + 'pay/'+app.root.apikeydefault, params,self.pay_order_success,app.root.error_request,app.root.failure_request)
        accordionitem = btn.parent.parent.parent.parent
        accordionitem.clear_widgets()

    def pay_all_success(self,req,result):
        if result.has_key('resp'):
            app = App.get_running_app()
            self.total_orders=0
            app.root.sm.current = 'Table'
            if platform=='android':
                app.root.PythonActivity.toastError(result['resp'])
            else:
                print result['resp']
        
    def pay_all(self,orderid,*args):
        app = App.get_running_app()
        payload = {'table':app.root.order_scr.thesi_lbl.text.split(' ')[1]}
        params = urllib.urlencode(payload)
        app.root.url_request(app.root.server_url.replace("\n","") + 'payall/'+app.root.apikey, params, self.pay_all_success,app.root.error_request, app.root.failure_request)
        self.items_acc.clear_widgets()
        
    def btn_backtable(self,*args):
        self.items_acc.clear_widgets()
        self.total_orders=0

    def btn_addorder(self,*args):
        app = App.get_running_app()
        app.root.order_scr.changeorder_oprop.text = 'SEND ORDER'

class MyAccordionItem(AccordionItem):
    pass

class ManagerListItem(SelectableView, BoxLayout):
    pass

class SqrYelButton(Button):
    pass



