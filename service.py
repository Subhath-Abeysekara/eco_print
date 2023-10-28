from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://icodeinnovahostingservice:pi1p1MQQcIRWOEHp@fitsixes.1begbkj.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)
db_Name = client['EcoPrint']

def connect_images():
    collection_name = db_Name["ImageDB"]
    return collection_name

def connect_plants():
    collection_name = db_Name["PlantDetails"]
    return collection_name

def connect_user():
    collection_name = db_Name["UserDetails"]
    return collection_name

def connect_undefined():
    collection_name = db_Name["UndefinePlants"]
    return collection_name

def connect_instructions():
    collection_name = db_Name["Instructions"]
    return collection_name

def connect_finetune():
    collection_name = db_Name["FinetuneImages"]
    return collection_name