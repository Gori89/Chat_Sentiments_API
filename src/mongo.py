from pymongo import MongoClient
from src.constants import MONGO, USER, KEY, DB, COLL_MESSEGE , COLL_USER
class ChatDB:

    def __init__(self):
        self.client = MongoClient(MONGO.format(USER,KEY))
        self.db = self.client[DB]
        self.messege=self.db[COLL_MESSEGE]
        self.user=self.db[COLL_USER]
        

        
    def addDocumentMessege(self,document):
        return self.messege.insert_one(document).inserted_id

    def addDocumentUser(self,document):
        return self.user.insert_one(document).inserted_id

    def findUser(self, query, projection):
        return self.user.find(query,projection)
    
    def getlastIdUser(self):
        return list(self.user.find({},{"idUser":1,"_id":0}).sort([('idUser',-1)]).limit(1))[0]['idUser']

    def addUser(self, user):
        idUser=self.getlastIdUser()+1
        document={'idUser':idUser,
                'name':user}
        return self.addDocumentUser(document), idUser
