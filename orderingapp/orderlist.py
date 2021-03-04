# -*- coding: utf-8 -*-
from kivy.uix.screenmanager import Screen
from kivy.uix.treeview import TreeView, TreeViewNode
from kivy.uix.treeview import TreeViewLabel
from kivy.uix.scrollview import ScrollView
from kivy.adapters.listadapter import ListAdapter
from kivy.adapters.simplelistadapter import SimpleListAdapter
from kivy.uix.listview import SelectableView,CompositeListItem,ListItemLabel,ListItemButton,ListView
from kivy.properties import ObjectProperty,NumericProperty,BooleanProperty,StringProperty #DictProperty,BooleanProperty
from listitemlabel import ProductListItemLabel, QuantityListItemLabel, MychoicestemLabel
from listitembutton import Level2ListItemButton,AddListItemButton,RemovelistItemButton,EditListItemButton,DelListItemButton
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.checkbox import CheckBox
from kivy.utils import platform
from datetime import timedelta
from datetime import date
#from bson import json_util
from kivy.app import App
import datetime
import datetime as dt
import urllib
import json


class OrderScreen(Screen):
    level1tv_oprop = ObjectProperty() # treeview BoxLayout id reference kv orderlist_lay
    tv_oprop = ObjectProperty()       ## treview ObjectProperty
    level2lv_oprop = ObjectProperty() # listview level2 BoxLayout id reference kv orderlist_lay
    level3lv_oprop = ObjectProperty() # listview  orderlist BoxLayout id reference kv orderlist_lay
    totalorder_nprop = NumericProperty() # total order 
    changeorder_oprop = ObjectProperty() #####button 'send order' id reference kv change 'send_orders' or 'update'
    product_name = StringProperty()
    edit_pop = ObjectProperty()         # popup edit orders 
    date = dt.date.isoformat(dt.date.today())
    
    def __init__(self, *args, **kwargs):
        super(OrderScreen, self).__init__(*args, **kwargs)

        self.scoll = ScrollView()
        app = App.get_running_app()
        self.tv_oprop = TreeView(size_hint_y=None,hide_root=True)                   #create trevview 
        self.tv_oprop.bind(minimum_height=self.tv_oprop.setter("height"))
        add = self.tv_oprop.add_node                                                
        self.tvfood = add(TreeViewButton(text='Food',size=(120, 40),is_open=False)) #TreeViewButton food
        for key in app.menu['Food'].keys():
            add(TreeViewButton(text=key,on_press=self.populate_level2,size=(120, 40),),self.tvfood)
        self.tvdrink = add(TreeViewButton(text='Drink',size=(120, 40),
        on_press=self.node_click,is_open=False))   
        self.tvfood.bind(on_press=self.node_click)
        for key in app.menu['Drink'].keys():                                        #TreeViewButton food
            add(TreeViewButton(text=key,on_press=self.populate_level2,size=(120, 40),),self.tvdrink)             
                
        self.args_converter_level2 = lambda row_index, rec: {'text': rec['text'], 
                                     'price':rec['price'],
                                     'level1':rec['level1'],
                                     'level2':rec['level2'],
                                     'choices':rec['choices'],
                                     'on_press':self.add_item
                                }

        self.level2_adapter = SimpleListAdapter(data=[],
                         args_converter=self.args_converter_level2,
                         selection_mode='single',
                         cls=Level2ListItemButton)
        
        self.args_converter_level3 = lambda row_index, rec: {'product':rec['product_name'],
                                                             'price':rec['price'],
                                                             'level1':rec['level1'],
                                                             'level2':rec['level2'],
                                                             'choices':rec['choices'],
                                                             'quantity':rec['quantity'],
                                                             'mychoices':rec['mychoices']}                   
                    
        self.level3_adapter = ListAdapter(data=[],
                            args_converter=self.args_converter_level3,
                            selection_mode='single',
                            allow_empty_selection=True,
                            template='OrderListItem')
        
        self.scoll.add_widget(self.tv_oprop)
        self.level1tv_oprop.add_widget(self.scoll,index=1)
        
        self.list_view_level2 = ListView(adapter=self.level2_adapter)        
        self.level2lv_oprop.add_widget(self.list_view_level2)

        self.list_view_level3 = ListView(adapter = self.level3_adapter)  
        self.level3lv_oprop.add_widget(self.list_view_level3,index=1)

    def node_click(self,btn,*args):# if node open close other node Food,Drink
        if btn.text=='Food':
            node1 = self.tvdrink 
            node2 = self.tvfood  
        elif btn.text=='Drink':
            node1 = self.tvfood  
            node2 = self.tvdrink 
        if node1.is_open:
            self.tv_oprop.toggle_node(node1)
        self.tv_oprop.toggle_node(node2)

    
    def populate_level2(self, btn, *args): #listview level2
        app = App.get_running_app()                              
        level1 = btn.parent_node.text
        l2 = [{'text':d['productname'],'price':d['price'],'level1':btn.parent_node.text,'level2':btn.text,'choices':d['choices']} for d in app.menu[level1][str(btn.text)]] #,'withwithout':d['withwithout']}
        self.level2_adapter.data = l2

    def add_item(self, btn, *args): #listview2 insert orderlistview
        myitem = None
        if self.level3_adapter.data:
            for index,item in enumerate(self.level3_adapter.data):
                if item['product_name'] == btn.text:       
                    myitem = self.level3_adapter.data.pop(index)
                    break
        if myitem:
            myitem['quantity'] = str(int(myitem['quantity'])+1)
            self.level3_adapter.data.insert(0,myitem)
            self.totalorder_nprop += myitem['price']
        else:
            self.level3_adapter.data.insert(0,{'product_name':btn.text,'price':btn.price,'level1':btn.level1,'level2':btn.level2,'choices':btn.choices,
                                                   'quantity':'1','mychoices':''})
            count = 0
            for items in self.level3_adapter.data:
                count += items['price'] * float(items['quantity'])
            self.totalorder_nprop = count

    def add_product(self,btn,*args): #button + add product
        amount = 0   
        row_id = btn.get_id   #id row from orderlistitem from kv_files
        quantity = btn.parent.children[3].text # quantity btn get ListItemLabel
        btn.parent.children[3].text =  str(int(quantity)+1) # ListItemLabel +1
        self.level3_adapter.data[row_id]['quantity'] = btn.parent.children[3].text #get item quantity for add product listorder,na krataei to quantity
        for items in self.level3_adapter.data:  # total price*quantity
            amount += items['price'] * float(items['quantity'])          
        self.totalorder_nprop = amount
        
    def remove_product(self, btn, *args): #button - remove product 
        amount = self.totalorder_nprop 
        row_id = btn.get_id     #id
        quantity = btn.parent.children[3].text
        if btn.parent.children[3].text > '1':
            btn.parent.children[3].text =  str(int(quantity)-1)
            self.level3_adapter.data[row_id]['quantity'] = btn.parent.children[3].text
            for items in self.level3_adapter.data:
                amount -= items['price'] * float(items['quantity'])
            self.totalorder_nprop -= amount

    def openchoice_pop(self,btn,*args):#open pop_up
        app = App.get_running_app()
        self.popup_content = EditProducts()
        self.product_name = btn.parent.children[5].text ## product name get label popup 
        row_id = btn.get_id
        self.items = self.level3_adapter.data[row_id]  #items row id
        self.popup_content.choices_adapter.data= [{'text':choice,'active':self.items['choices'][choice]} for choice in self.items['choices']]
        self.edit_pop.content = self.popup_content
        self.edit_pop.title = 'Choices'
        self.edit_pop.auto_dismiss=False
        self.edit_pop.open()
        
        firstitem = None
        if self.level3_adapter.data:
            for index,item in enumerate(self.level3_adapter.data):
                if int(item['quantity']) > 1 :
                    firstitem = self.level3_adapter.data.pop(index)
                    newitem = firstitem.copy()
                    newitem['quantity'] = str(int(item['quantity'])-1)
                    firstitem['quantity'] = '1'
                    self.level3_adapter.data.insert(0,item) 
                    self.level3_adapter.data.insert(0,newitem)

    def delete_product(self, btn, *args): #button delete product
        row_id = btn.get_id  
        price = self.level3_adapter.data[row_id]['price'] #price
        quantity = self.level3_adapter.data[row_id]['quantity']
        self.totalorder_nprop -= price * float(quantity) 
        del self.level3_adapter.data[row_id]

    def btn_back_managementorders_success(self, req, result): # result oders take accordion
        app = App.get_running_app()
        if result.has_key('resp'):
            if platform =='android':
               app.root.PythonActivity.toastError(result['resp'])
            else:
                print result['resp']
        else:
            app.root.sm.current = 'Table'
            if platform =='android':
                app.root.PythonActivity.toastError(result['respno'])
            else:
                print result['respno']

    def btn_back_managementorders(self,btn,*args):# button < back management order 
        app = App.get_running_app()
        app.root.sm.current = 'managementorders'
        payload = {'table': self.thesi_lbl.text.split(' ')[1]}
        params = urllib.urlencode(payload)
        app.root.url_request(app.root.server_url + 'data/backmanagement/'+app.root.apikey, params, self.btn_back_managementorders_success, app.root.error_request, app.root.failure_request)
        del self.level3_adapter.data[:]
        self.totalorder_nprop = 0
    
    def delete_order_success(self,req,result): 
        app = App.get_running_app()
        if result.has_key('resp'):
            orderstable = result['orderstablelist']
            app.root.management_scr.items_acc.clear_widgets()
            app.root.management_scr.createaccordion(orderstable)
        del self.level3_adapter.data[:] #list orderlist
        self.totalorder_nprop = 0
        if platform=='android':
            app.root.PythonActivity.toastError(result['resp'])
        else:
            print result['resp']

    def delete_order(self,*args): # delete order with orderid
        app = App.get_running_app()
        payload = {'order_id':app.root.management_scr.order_id,'table':self.thesi_lbl.text.split(' ')[1]}
        params = urllib.urlencode(payload)
        app.root.url_request(app.root.server_url + 'data/deleteorder/'+app.root.apikey, params, self.delete_order_success, app.root.error_request, app.root.failure_request)

    def order_btn_press(self,orderid,*args): #button send order,update 
        if self.changeorder_oprop.text == 'UPDATE ORDER': #update order
            self.send_data(neworder=False)
        else:
            self.send_data(neworder=True)

    def send_data_success(self, req, result):
        
        app = App.get_running_app()
        if result.has_key('save'):
            orderstable = result['getorder']
            app.root.management_scr.createaccordion(orderstable)
            if platform =='android':
                  app.root.PythonActivity.toastError(result['save'])
            else:
                print result['save']
        else:
            if platform =='android':
                 app.root.PythonActivity.toastError(result['up'])
            else:
                print result['up']
                app.root.management_scr.items_acc.clear_widgets()
                orderstable = result['getorder']
                print orderstable,'getorder'
                
                app.root.management_scr.createaccordion(orderstable)
        del self.level3_adapter.data[:]
        self.totalorder_nprop = 0
    
    def send_data(self,neworder=True,*args): #send order,table,total
        app = App.get_running_app()
        order_data = {}
        order_data['customer_id']= app.root.customer_id
        order_data['user_id']= app.root.user_id
        order_data['acount'] = ''
        order_data['items']= self.level3_adapter.data
        order_data['table'] = self.thesi_lbl.text.split(' ')[1]
        order_data['total']= self.totalorder_nprop
        order_data['status'] = 'new'
        order_data['date'] = str(self.date)
        order_data['datetime'] = str(self.date)
        order_data['saved'] = str(datetime.datetime.now())
        order_data['datetime'] = str(dt.date.isoformat(dt.date.today()))

        if app.root.apikey:
            if neworder:
                payload = {'order_data':json.dumps(order_data),'table':self.thesi_lbl.text.split(' ')[1],'total':self.totalorder_nprop}
                params = urllib.urlencode(payload)
                app.root.url_request(app.root.server_url + 'data/insertorder/'+app.root.apikey, params, self.send_data_success,app.root.error_request,app.root.failure_request)
            else:
                payload = {'_id':app.root.management_scr.order_id,'order_data':json.dumps(order_data),'table':self.thesi_lbl.text.split(' ')[1],'total':self.totalorder_nprop}
                params = urllib.urlencode(payload)
                print self.totalorder_nprop,'self.totalorder_nprop'
                app.root.url_request(app.root.server_url + 'data/updateorder/'+app.root.apikey, params, self.send_data_success,app.root.error_request,app.root.failure_request)

class MyCheckBox(SelectableView,CheckBox):
    pass

class TreeViewButton(Button, TreeViewNode): 
    pass

class OrderListItem(SelectableView, BoxLayout):  
    pass

class EditItemLabel(ListItemLabel):
    pass


class EditProducts(BoxLayout):
    
    active = BooleanProperty()
    choices_oprop = ObjectProperty() 
    comment = ObjectProperty()
    
    def __init__(self,*args,**kwargs):
        super(EditProducts, self).__init__(*args, **kwargs)
        args_converter_edit = lambda row_index, rec: \
        {'size_hint_y': None,
        'height': 30,
        'spacing':8,
        'is_selected':True,
        'text':rec['text'],
        'active':rec['active'],

        'cls_dicts':
                 [{'cls':ListItemLabel,
                    'kwargs': {'text':rec['text'],
                               'color': [0,0,0, 0.95],
                               'size_hint_x': .2,'size_hint_y': None,'height': 25, 'font_size': '12sp'}},
                 {'cls':MyCheckBox,
                   'kwargs': {'active':rec['active'],
                              'size_hint_x': .2,'size_hint_y': None,'height': 25, 'font_size': '12sp',
                              'on_press': self.on_active}}
        ]}
        self.choices_adapter = ListAdapter(data=[], #edit_adapter
                            args_converter=args_converter_edit,
                            selection_mode='none',
                            allow_empty_selection=True,
                            cls=CompositeListItem)
        self.list_view_choices = ListView(adapter=self.choices_adapter)
        self.choices_oprop.add_widget(self.list_view_choices)

    def on_active(self,checkbox):
        row_id = checkbox.index
        if checkbox.active:
            self.choices_adapter.data[row_id]['active'] = True
        else:
            self.choices_adapter.data[row_id]['active'] = False
            
    def close_pop(self,btn,*arg): #checkbox
        app = App.get_running_app()
        extra = self.choices_adapter.data
        mychoices = {item['text']:item['active'] for item in extra}
        app.root.order_scr.items['choices'].update(mychoices)
        app.root.order_scr.edit_pop.dismiss()
        



    
