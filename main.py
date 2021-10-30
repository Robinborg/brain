'''Program that stores information and retrieves information'''
from bs4 import BeautifulSoup
import requests
from datetime import datetime, date
#from mongoengine import connect, Document, StringField
from pymongo import MongoClient
import pprint


#class BaseTemplateMongo(Document):
#    current_date = StringField(required=True, max_length=12)
#    take_note = StringField(requied=True)

    
class websearcher:
    def __init__(self):
        pass

    def website_opener(self, insert_link: str):
        '''get website and html of said site'''
        self.insert_link = insert_link
        self.website = requests.get(insert_link)
        self.soup = BeautifulSoup(website.content, 'html.parser')
        print(soup.prettify())

    def links_from_website(self):
        all_links = [a["href"]
                     for a in self.soup('a')
                     if a.hast_attr("href")]


class Notes:
    def __init__(self):
        """ start client and switch over to the right database and collection """

        self.client = MongoClient(host="localhost", port=27017)
        db = self.client.notes
        self.my_notes= db.my_notes
                
    def insert_a_new_note(self, write_note: str):
        assert write_note, "Write a note"

        self.write_note = write_note

        insert_note = {
                "date": datetime.now().strftime("%d/%m/%Y"),
                "Note": self.write_note
                }
        self.my_notes.insert_one(insert_note)
        self.client.close()

class Books:
    def __init__(self):
        """ start client and switch over to the right database and collection """

        self.client = MongoClient(host="localhost", port=27017)
        db = self.client.books
        self.my_books= db.my_books
                
    def insert_a_new_book(self, write_book: str, review_of_book: str):
        assert write_book, "Write a book"

        self.write_book = write_book 
        self.review_of_book = review_of_book

        insert_book = {
                "date": datetime.now().strftime("%d/%m/%Y"),
                "Books name": self.write_book,
                "The books review": self.review_of_book
                }
        self.my_books.insert_one(insert_book)

        print(f"inserted: {self.my_books.inserted_id}")
        self.client.close()

class Podcasts:
    def __init__(self):
        """ start client and switch over to the right database and collection """

        self.client = MongoClient(host="localhost", port=27017)
        db = self.client.podcasts
        self.my_podcasts = db.my_podcasts
                
    def insert_a_new_podcast(self, write_podcast: str, review_of_podcast: str = None):
        assert write_podcast, "Write a podcast."

        self.write_podcast = write_podcast
        self.review_of_podcast = review_of_podcast

        insert_podcast = {
                "date": datetime.now().strftime("%d/%m/%Y"),
                "Podcasts name": self.write_podcast,
                "Review of podcast": self.review_of_podcast
                }
        self.my_podcasts.insert_one(insert_podcast)

        print(f"inserted: {self.my_podcasts.inserted_id}")
        self.client.close()


#for doc in my_thoughts.find():
#    pprint.pprint(doc)
#
#with MongoClient(host="localhost", port=27017) as client:
#    db = client.brain
#    for doc in db.ideas.find():
#        pprint.pprint(doc)
#

using_podcasts = Podcasts()
using_podcasts.insert_a_new_podcast("Lex Friedman episode 234", "This was an episode about Stephen Wolframs theory")

using_notes = Notes()
using_notes.insert_a_new_note("How are you?")

using_books = Books()
using_books.insert_a_new_book("Maths on the back of an envelope", "Extremely useful book for doing arthimetics!")




