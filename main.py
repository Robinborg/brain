'''Program that stores information and retrieves information'''
from bs4 import BeautifulSoup
import requests
from sqlalchemy import create_engine

class websearcher:
    def __init__(self):
        '''storage'''
        self.stored_websites = []
        self.website_links = []
        self.stored_text_website = []

    def website_opener(self, insert_link):
        '''get website and html of said site'''
        self.insert_link = insert_link
        website = requests.get(insert_link)
        soup = BeautifulSoup(website.content, 'html.parser')
        print(soup.prettify())
        return soup

    def links_from_website(self.soup):
        pass

def podcast(insert_podcast):
    '''save podcast and ask for timestamps'''

class NoteTaking:
    def __init__(self):
        self.saved_ideas = []

    def writing_ideas(self, idea):
        self.idea = idea
        self.saved_ideas.append(idea)

class Books:
    def __init__(self):
        self.stored_books = []

    def noted_book(self, book):
        self.book = book
        self.stored_books.append(book)


class Brain:
    '''structure the writing to file and loops to keep getting input'''
    while True:
        idea()
        link()
        podcast()
        book()
        break



#SQL 
engine = create_engine('sqlite:///noted_ideas.db')

