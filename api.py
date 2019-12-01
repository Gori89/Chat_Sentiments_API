from bottle import route, run, get, post, request
import random
from src.mongo import ChatDB
import bson



# ### 1. User endpoints
# - (POST) `/user/create` 
#   - **Purpose:** Create a user and save into DB
#   - **Params:** `username` the user name
#   - **Returns:** `user_id`

@get('/prueba')
def prueba():
    return 'prueba'
    
@post('/user/create')
def addUser():
    name=request.forms.get("name")
    idMongo, userId=connection.addUser(name)
    return {
        "inserted_doc": str(idMongo),
        "userId": userId
        }


# - (GET) `/user/<user_id>/recommend`  
#   - **Purpose:** Recommend friend to this user based on chat contents
#   - **Returns:** json array with top 3 similar users
# ​
# ### 2. Chat endpoints:
# - (GET) `/chat/create` 
#   - **Purpose:** Create a conversation to load messages
#   - **Params:** An array of users ids `[user_id]`
#   - **Returns:** `chat_id`
# - (GET) `/chat/<chat_id>/adduser` 
#   - **Purpose:** Add a user to a chat, this is optional just in case you want to add more users to a chat after it's creation.
#   - **Params:** `user_id`
#   - **Returns:** `chat_id`
# - (POST) `/chat/<chat_id>/addmessage` 
#   - **Purpose:** Add a message to the conversation. Help: Before adding the chat message to the database, check that the incoming user is part of this chat id. If not, raise an exception.
#   - **Params:**
#     - `chat_id`: Chat to store message
#     - `user_id`: the user that writes the message
#     - `text`: Message text
#   - **Returns:** `message_id`
# - (GET) `/chat/<chat_id>/list` 
#   - **Purpose:** Get all messages from `chat_id`
#   - **Returns:** json array with all messages from this `chat_id`
# - (GET) `/chat/<chat_id>/sentiment` 
#   - **Purpose:** Analyze messages from `chat_id`. Use `NLTK` sentiment analysis package for this task
#   - **Returns:** json with all sentiments from messages in the chat


connection= ChatDB()     

run(host='0.0.0.0', port=8080)
