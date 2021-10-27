'''Program that stores information and retrieves information'''
from bs4 import BeautifulSoup
import requests
from datetime import datetime, date
from mongoengine import connect, Document, StringField

class BaseTemplateMongo(Document):
    current_date = StringField(required=True, max_length=12)
    take_note = StringField(requied=True)

    
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


class NoteTaking:
    def __init__(self):
        connect(db="notes", host="localhost", port=27017)

    def writing_ideas(self, idea: str):
        self.today = datetime.today().strftime("%d/%m/%Y")
        self.idea = idea
        self.start_ideas = BaseTemplateMongo(
                current_date = self.today,
                take_note = self.idea
                )
        self.start_ideas.save()

    def show_all_ideas(self):
        pass

class Books:
    def __init__(self):
        self.stored_books = {}

    def noted_book(self, book):
        self.book = book
        self.date_today = datetime.today().strftime("%d-%m-%Y")
        self.stored_books[self.date_today] = self.book


#my_second_note = NoteTaking()
#my_second_note.writing_ideas("Does the mongo server get this")

#for doc in BaseTemplateMongo.objects:
#    print(doc.take_note)

client = MongoClient()
col = client.mydb.test

result = col.insert_one({'x':1})
result.insert_id

