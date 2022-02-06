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
    parser = argparse.ArgumentParser(description="Digital brain for storing you ideas and information")
    parser.add_argument("--note", action = "store_true")
    parser.add_argument("--website", nargs="?", default = "enter_web")
    parser.add_argument("--website_links", nargs="?", default = "enter_link")
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
    #For handling website scraping and entry
    elif args.website_links == "enter_link":
       website =  WebSite()
       enter_website = input("Enter website: ")
       web_open = website.open_website(enter_website)
       links = website.get_all_links(web_open)
       website.insert_database(links)

    elif args.website_links:
       website =  WebSite()
       web_open = website.open_website("".join(args.website_links))
       links = website.get_all_links(web_open)
       website.insert_database(links)

    elif args.website == "enter_web":
        website = WebSite()
        enter_website = input("Enter website: ")
        web_open = website.open_website(enter_website)
        website.insert_database(web_open)

    elif args.website:
        website = WebSite()
        w = website.open_website("".join(args.website))
        website.insert_database(w)
   #For handling podcasts
    elif args.podcast:
       enter_podcast = Podcasts()
       enter_podcast.insert_database()
    #For handling books
    elif args.book:
        enter_book = Books()
        enter_book.insert_database()

    #for showing data in db
    elif args.show_notes:
        show_whole_notes_collection()
    elif args.show_websites:
        show_whole_websites_collection()
    elif args.show_books:
        show_whole_books_collection()
    elif args.show_podcasts:
        show_whole_podcasts_collection()
    return True

if __name__ == "__main__":
    main()

