from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
from database.connection import connect_database
from utils.insert_database import insert_db
from notes.note import Notes
from websites.website import WebSearch
from podcasts.podcast import Podcasts
from books.book import Books



#for doc in my_thoughts.find():
#    pprint.pprint(doc)
#with MongoClient(host="localhost", port=27017) as client:
#    db = client.brain
#    for doc in db.ideas.find():
#        pprint.pprint(doc)

if __name__ == "__main__":
    enter_note = Notes()
    enter_note.insert_database()
    search_website = WebSearch()
    search_website.insert_database(2)
    enter_podcast = Podcasts()
    enter_podcast.insert_database(2)
    enter_book = Books()
    enter_book.insert_database(2)

