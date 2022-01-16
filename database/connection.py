from pymongo import MongoClient

def connect_database(notes: bool = False,
                     websites: bool = False,
                     books: bool = False,
                     podcasts: bool = False) -> MongoClient:
    client = MongoClient(host = "localhost", port = 27017)
    if notes:
        db = client.notes
        my_notes = db.my_notes
        return my_notes
    if websites:
        db = client.websites
        my_websites = db.my_websites
        return my_websites
    if books:
        db = client.books
        my_books = db.my_books
        return my_books
    if podcasts:
        db = client.podcasts
        my_podcasts = db.my_podcasts
        return my_podcasts



