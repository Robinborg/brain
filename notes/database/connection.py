from pymongo import MongoClient

def connect_database(notes: bool = False,
                     websites: bool = False,
                     books: bool = False,
                     podcasts: bool = False) -> MongoClient:
    client = MongoClient("localhost", 27017)
    if notes:
        db = client.digital_brain
        my_notes = db.notes
        return my_notes
    if websites:
        db = client.digital_brain
        my_websites = db.websites
        return my_websites
    if books:
        db = client.digital_brain
        my_books = db.books
        return my_books
    if podcasts:
        db = client.digital_brain
        my_podcasts = db.podcasts
        return my_podcasts



