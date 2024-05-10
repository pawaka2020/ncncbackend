# models/mongodb/create_collections.py

import json
from .db import db
from bson import ObjectId

def create_starting_collection(list, collection_name, starting_dataset):
    if collection_name not in list:
        db.create_collection(collection_name)
        with open(starting_dataset) as file:
            file_data = json.load(file)
            for item in file_data:
                db[collection_name].insert_one(item)
        print("Collection created for", collection_name)
    else:
        return

def create_empty_collection(list, collection_name):
    if collection_name not in list:
        db.create_collection(collection_name)
        print("Empty collection created for", collection_name)
    else:
        return

# Creates starting collections for the backend app. 
def create_collections():
    print("Creating collections for the backend")
    list = db.list_collection_names()
    create_starting_collection(list, "fullnews", 'starting_datasets/fullnews.json')
    create_starting_collection(list, "bannernews", 'starting_datasets/bannernews.json')
    create_starting_collection(list, "menuitem", 'starting_datasets/menuitem.json')
    create_starting_collection(list, "vouchers", 'starting_datasets/vouchers.json')
    create_empty_collection(list, "users")
    create_empty_collection(list, "orders")
    create_empty_collection(list, "cartitem")