# Editor.md

Open terminal 

MongoDB Create Administrator User

~$ mongodb or mongo
     
       db.createUser({user: "user",pwd: "password",roles:[{role: "userAdminAnyDatabase" , db:"admin"}]})

open connection_admin_mongo.py

You are required to user password api address
URI  is a sequence of characters that distinguishes one resource from another.

     uri = '''mongodb://user:password@api address/admin'''

Run connection_admin_mongo.py You get api_key
API key is a code used to identify and authenticate an application or user


> Web2py 

ordering/customersapp.py

You give you api_key:

      if request.args[1]=='api_key':

Similar and the rest: ordering/default.py   ordering/orderingapp.py

ordering/db.py
Connect with mongodb databases
You give you api address:

      uri = '''mongodb://testUser:testPass@api address/orderingdb'''

You give your email and password 
   
      server.login("email","password")

sendemail.py sendpasswors.py


> Application

 customers/creatcustomer.py

You give api_key:
      
       self.apikey = 'api_key':

You give api address:
       
       req = UrlRequest('https://api_key/ordering/customersapp/customers/add_customer/'+self.apikey,
                         req_body=params,on_success=self.customer_success,verify=False)

Similar and the rest: orderingapp/mainlayout.py  orderingtools/orderingatools.py

orderingapp  change to confg.txt api address or when you run app orderingapp/main.py change manual api address
orderingtools  change to confg.txt api address






