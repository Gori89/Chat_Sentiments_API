from pymongo import MongoClient
from src.constants import DB, COLL_MESSEGE , COLL_USER

class ChatDB:

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client[DB]
        self.messege=db[COLL_MESSEGE]
        self.user=db[COLL_USER]
        

        
    def addDocumentMessege(self,document):
        return self.messege.insert_one(document).inserted_id

    def addDocumentUser(self,document):
        return self.user.insert_one(document.inserted_id
    
    def getlastIdUser():
        
    
    def addUser(self, user):
        document={'idUser':self.getlastIdUser()+1,
                'name':user}
        return self.addDocumentUser(document), idUser
