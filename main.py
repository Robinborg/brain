import sys
from pymongo import MongoClient
from notes.note import Notes
from websites.website import WebSite
from podcasts.podcast import Podcasts
from books.book import Books
import pprint
from utils.print_data import show_notes

show_notes()



def main(sysargv):
    if sysargv == '-n':
        enter_note = Notes()
        enter_note.insert_database()
    if sysargv == '-w':
        search_website = WebSite()
        search_website.insert_database(2)
    if sysargv == '-p':
        enter_podcast = Podcasts()
        enter_podcast.insert_database(2)
    if sysargv == '-b':
        enter_book = Books()
        enter_book.insert_database(2)

if __name__ == "__main__":
    args = sys.argv[1]
    main(args)

