import pprint
from pymongo import MongoClient


def show_notes():
    with MongoClient("localhost", 27017) as client:
        db = client.digital_brain
        for doc in db.notes.find():
            pprint.pprint(doc)
