import pymongo
import Class.userClass as userClass

mongoclient = pymongo.MongoClient("mongodb://localhost:27017/")
mongodb=mongoclient["AMCS_DB"]

class userCollection:
    def __init__(self):
        self.client = mongoclient
        self.db = mongodb
        self.col = self.db["Users_Collection"]

    def insert(self, data): 
        self.col.insert_one(data)
    def find(self, data):
        return self.col.find(data)
    def update(self, data, newdata):
        self.col.update_one(data, newdata)
    def delete(self, data):
        self.col.delete_one(data)
    def find_one(self, data):
        return self.col.find_one(data)
    def loginControl(self, name, password):
        userClass.store.UserJson=self.col.find_one({"_Name": name, "_Password": password})
        return userClass.store.UserJson
    