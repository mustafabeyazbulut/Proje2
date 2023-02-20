import pymongo
import Class.userClass as userClass


class userCollection:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["AMCS_DB"]
        self.col = self.db["Users_Collection"]

    def insert(self, data):
        self.col.insert_one(data)

    def find(self, data):
        return self.col.find(data)
    
    def login(self, data):
        return self.col.find_one(data)

    def update(self, data, newdata):
        self.col.update_one(data, newdata)

    def delete(self, data):
        self.col.delete_one(data)
    
    
    def find_all(self):
        return self.col.find()
    
    def find_one(self, data):
        return self.col.find_one(data)
    def loginControl(self, name, password):
        login=self.col.find_one({"_Name": name, "_Password": password})
        userClass.store.UserJson=login
        return login
    