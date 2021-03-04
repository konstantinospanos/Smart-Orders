# -*- coding: utf-8 -*-
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty#, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.utils import platform
import urllib

class TableScreen(Screen):

    addtable_obj = ObjectProperty() # id GridLayout add widget table 

    def __init__(self, *args, **kwargs):
        super(TableScreen,self).__init__(*args, **kwargs)
        for i in range(22):
            btn = Button(text="TABLE %s" % (i+1),
            background_color= (0.858,0.839,0.839,1))
            btn.bind(on_press=self.table)
            self.addtable_obj.add_widget(btn)  # GridLayout id object create tables

    def table_success(self,req,result):
        print 'table_succes '
        app = App.get_running_app()
        if result.has_key('allorderstable'):  #get all order table # check orders tables
            print result['allorderstable']
            orderstable  = result['allorderstable']
            app.root.management_scr.items_acc.clear_widgets()
            app.root.management_scr.createaccordion(orderstable) #call fuction managerscreen view accordion  
            app.root.sm.current = 'managementorders'
            if platform =='android':
                app.root.PythonActivity.toastError(result['resp'])
            else:
                print result['resp']
        elif result.has_key('nonorder'):
            print 'nonorder'
            app.root.order_scr.changeorder_oprop.text = 'SEND ORDER'     # button change 
            app.root.sm.current = 'Order'
            if platform =="android":
                app.root.PythonActivity.toastError(result['nonorder'])
            else:
                print result['nonorder']
            
    def table(self,btn,*args):
        app = App.get_running_app()             
        app.root.management_scr.items_acc.clear_widgets()
        app.root.order_scr.thesi_lbl.text = btn.text  # get table on label orderscreen
        print btn.text,'tabletabletabletable'
        payload = {'table':btn.text.split(' ')[1]}    # get table request
        params = urllib.urlencode(payload)
        if app.root.apikey:                           
            app.root.url_request(app.root.server_url + 'vieworder/'+app.root.apikey, params, self.table_success, app.root.error_request, app.root.failure_request)

