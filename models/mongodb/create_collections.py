# models/mongodb/create_collections.py
import json
from .db import db

def create_starting_collection(list, collection_name, starting_dataset):
    if collection_name not in list:
        db.create_collection(collection_name)
        with open(starting_dataset) as file:
            file_data = json.load(file)
            if ("_id") in file_data:
                del file_data["_id"]
            db[collection_name].insert_one(file_data)
    else:
        return

def create_collections():



    collist = db.list_collection_names()

    create_starting_collection(collist, "shit", 'starting_datasets/fullnews.json')
    if "customers3" not in collist:
        print("Customers3 collection created")
        db.create_collection("customers3")
        # Read data from JSON file
        with open('starting_datasets/fullnews.json') as f:
            data = json.load(f)
            print("data ", data)
            if "_id" in data:
                del data["_id"]
            db["customers3"].insert_one(data)
        print("Data inserted into customers3 collection")
    else:
        print("Customers3 collection already exists")
