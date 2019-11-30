
import dotenv
import os
dotenv.load_dotenv()
KEY = os.getenv("MONGO_PASS")



MONGO="mongodb+srv://{}:{}@mflix-pmskq.mongodb.net/test?retryWrites=true&w=majority"
USER='fran'