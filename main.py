from bs4 import BeautifulSoup
import requests
from datetime import datetime
from pymongo import MongoClient
from typing import Dict

date_today = datetime.now().strftime("%d/%m/%Y")

def connect_database(
        notes: bool = False, websites: bool=False,
        books: bool = False, podcasts: bool = False):
    """Connect to the correct database"""
    client = MongoClient(host = "localhost", port = 27017)
    if notes:
        db = client.notes
        my_notes = db.my_notes
        return my_notes
    elif websites:
        db = client.websites
        my_websites = db.my_websites
        return my_websites
    elif books:
        db = client.books
        my_books = db.my_books
        return my_books
    elif podcasts:
        db = client.podcasts
        my_podcasts = db.my_podcasts
        return my_podcasts

def inserter(write: str = None, review: str = None) -> Dict:
    """Make the dictionary to be inserted into database"""
    assert write, "You need to write a note"
    if not review:
        insert_only_note = {
                "date": date_today,
                "Note": write
                }
        return insert_only_note
    else:
        insert_both = {
                "date": date_today,
                "Note": write,
                "Review": review
                }
        return insert_both

class WebSearcher:
    """ stores and searches web sites """
    def __init__(self):
        self.website_connection = connect_database(websites=True)

    def website_opener(self, insert_link: str):
        '''get website and html of said site'''
        self.insert_link = insert_link
        website = requests.get(insert_link)
        soup = BeautifulSoup(website.content, 'html.parser')
        print(soup.prettify())

    def links_from_website(self):
        self.all_links = [a["href"]
                     for a in self.soup('a')
                     if a.hast_attr("href")]
        

    def websites_db(self, insert_all_websites: Bool = False, both: Bool = False):
        """Insert website data into database"""
        if both:
            insert_note = input("Insert note: ")
            insert_review = input("Insert review: ")
            to_be_inserted = inserter(write=insert_note, review=insert_review)
            to_be_inserted['All links from website: '] = self.all_links
            inserted = self.website_connection.insert_one(to_be_inserted)
            print(f"One insertion: {inserted.inserted_id}")

        else:
            insert_note = input("Insert note: ")
            to_be_inserted = inserter(write=insert_note)
            to_be_inserted['All links from website: '] = self.all_links
            inserted = self.website_connection.insert_one(to_be_inserted)
            print(f"One insertion: {inserted.inserted_id}")

class Notes:
    """ note taking program that stores information in mongodb """
    def __init__(self):
        """ start client and switch over to the right database and collection """
        self.notes_connection = connect_database(notes=True)
                
    def note_to_db(self):
        insert_note = input("Insert note: ")
        to_be_inserted = inserter(insert_note)
        inserted = self.notes_connection.insert_one(to_be_inserted)
        print(f"One insertion: {inserted.inserted_id}")

class Books:
    def __init__(self):
        """ start client and switch over to the right database and collection """
        self.books_connection = connect_database(books=True)

    def book_db(self, both = False):
        """Insert website data into database"""
        if both:
            insert_note = input("Insert note: ")
            insert_review = input("Insert review: ")
            insert_pages = input("How many pages: ")
            to_be_inserted = inserter(write=insert_note, review=insert_review)
            to_be_inserted['Pages: '] = insert_pages
            inserted = self.books_connection.insert_one(to_be_inserted)
            print(f"One insertion: {inserted.inserted_id}")
        else:
            insert_note = input("Insert note: ")
            insert_page = input("How many pages: ")
            to_be_inserted = inserter(write=insert_note)
            to_be_inserted['Pages: '] = insert_page
            inserted = self.books_connection.insert_one(to_be_inserted)
            print(f"One insertion: {inserted.inserted_id}")

class Podcasts:
    def __init__(self):
        """ start client and switch over to the right database and collection """
        self.podcasts_connection = connect_database(podcasts=True)

    def podcast_db(self, both = False):
        """Insert website data into database"""
        if both:
            insert_note = input("Insert note: ")
            insert_review = input("Insert review: ")
            to_be_inserted = inserter(write=insert_note, review=insert_review)
            inserted = self.podcasts_connection.insert_one(to_be_inserted)
            print(f"One insertion: {inserted.inserted_id}")

        else:
            insert_note = input("Insert note: ")
            to_be_inserted = inserter(write=insert_note)
            inserted = self.podcasts_connection.insert_one(to_be_inserted)
            print(f"One insertion: {inserted.inserted_id}")


#for doc in my_thoughts.find():
#    pprint.pprint(doc)
#
#with MongoClient(host="localhost", port=27017) as client:
#    db = client.brain
#    for doc in db.ideas.find():
#        pprint.pprint(doc)

#using_podcasts = Podcasts()
#using_podcasts.podcast_db(both=True)

#using_notes = Notes()
using_books = Books()
using_books.book_db(both=True)




