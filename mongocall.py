from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd

# Set the value of MONGODB_URI to your Atlas connection string.
MONGODB_URI = "mongodb+srv://<name>:<password>@myatlasclusteredu.oseoepr.mongodb.net/?retryWrites=true&w=majority"

# Connect to your MongoDB cluster.
client = MongoClient(MONGODB_URI)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Set which db and collection to use
db = client['Bjj_data']
collection = db['bjj_data']

# Open the CSV file and read the lines
df = pd.read_csv("data_new_sep.csv")
data_dict = df.to_dict("records")
collection.insert_many(data_dict)

