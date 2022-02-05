import sys
from pymongo import MongoClient
import argparse
from notes.note import Notes
from websites.website import WebSite
from podcasts.podcast import Podcasts
from books.book import Books
import pprint
from utils.print_data import show_whole_notes_collection,\
    show_whole_websites_collection, show_whole_books_collection,\
    show_whole_podcasts_collection

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--note", action = "store_true")
    parser.add_argument("--website", action = "store_true")
    parser.add_argument("--podcast", action = "store_true")
    parser.add_argument("--book", action = "store_true")
    parser.add_argument("--show_notes", action = "store_true")
    parser.add_argument("--show_websites", action = "store_true")
    parser.add_argument("--show_podcasts", action = "store_true")
    parser.add_argument("--show_books", action = "store_true")
    args = parser.parse_args()
    #for entering data to db
    if args.note:
        enter_note = Notes()
        enter_note.insert_database()
    if args.website:
       enter_website = WebSite()
       enter_website.insert_database()
    if args.podcast:
       enter_podcast = Podcasts()
       enter_podcast.insert_database()
    if args.book:
        enter_book = Books()
        enter_book.insert_database()

    #for showing data in db
    if args.show_notes:
        show_whole_notes_collection()
    if args.show_websites:
        show_whole_websites_collection()
    if args.show_books:
        show_whole_books_collection()
    if args.show_podcasts:
        show_whole_podcasts_collection()
    return True

if __name__ == "__main__":
    main()

