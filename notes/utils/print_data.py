import pprint
from pymongo import MongoClient


def show_whole_notes_collection():
    with MongoClient("localhost", 27017) as client:
        db = client.digital_brain
        for doc in db.notes.find():
            pprint.pprint(doc)

def show_whole_books_collection():
    with MongoClient("localhost", 27017) as client:
        db = client.digital_brain
        for doc in db.books.find():
            pprint.pprint(doc)

def show_whole_websites_collection():
    with MongoClient("localhost", 27017) as client:
        db = client.digital_brain
        for doc in db.websites.find():
            pprint.pprint(doc)

def show_whole_podcasts_collection():
    with MongoClient("localhost", 27017) as client:
        db = client.digital_brain
        for doc in db.podcasts.find():
            pprint.pprint(doc)
