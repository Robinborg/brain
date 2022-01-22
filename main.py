import sys
from pymongo import MongoClient
from notes.note import Notes
from websites.website import WebSite
from podcasts.podcast import Podcasts
from books.book import Books
import pprint
from utils.print_data import show_whole_notes_collection,\
    show_whole_websites_collection, show_whole_books_collection,\
    show_whole_podcasts_collection

def main(sysargv: str) -> None:
    #for entering data to db
    if sysargv == '-n' or sysargv == "--note":
        enter_note = Notes()
        enter_note.insert_database()
    if sysargv == '-w' or sysargv == "--website":
        search_website = WebSite()
        search_website.insert_database()
    if sysargv == '-p' or sysargv == "--podcast":
        enter_podcast = Podcasts()
        enter_podcast.insert_database()
    if sysargv == '-b' or sysargv == "--book":
        enter_book = Books()
        enter_book.insert_database()

    #for showing data in db
    if sysargv == '-sn' or sysargv == "--show_notes":
        show_whole_notes_collection()
    if sysargv == '-sw' or sysargv == "--show_websites":
        show_whole_websites_collection()
    if sysargv == '-sb' or sysargv == "--show_books":
        show_whole_books_collection()
    if sysargv == '-sp' or sysargv == "--show_podcasts":
        show_whole_podcasts_collection()
    return True

if __name__ == "__main__":
    args = sys.argv[1]
    main(args)

