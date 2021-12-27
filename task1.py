import requests
from pymongo import MongoClient

class Suman:
    connection = MongoClient("mongodb://localhost:27017/")

    def mongo_connection(self):
        if self.connection:
            return True
        else:
            return False
    
    def create_new_collection(self, db_name, new_collection):
        if self.connection:
            db_name = self.connection[db_name]
            new_collection = db_name[new_collection]
            return(new_collection)
        else:
            return("ERROR(404) : MongoDB Connection Failed !")

    def insert_data(self, db_name,collection_name,data):
        if self.connection:
            self.connection[db_name][collection_name].insert_one(data)
            return("SUCCESS : Data Inserted !")
        else:
            return("ERROR : Unable to insert data")
    
    def hit_url(self,url):
      response=requests.get(url)
      data=response.json()
      json_leng=len(data)
      heading = []
      for data in data:
         self.insert_data('datab','task',data)
    def tab_url(self,url):
     response=requests.get(url)
     data=response.json()
     json_leng=len(data)
     head=list(data[0].keys())
     print(*head)
     print()
     for j in range(0,len(data)): 
      for i in head:
       print(data[j][i],end=' ')
       print()
url="https://fruityvice.com/api/fruit/all"
s=Suman()  
s.tab_url(url)  
s.create_new_collection('datab','task')
s.hit_url(url)