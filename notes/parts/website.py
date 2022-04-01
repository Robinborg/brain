
from database.connection import connect_database
from utils.insert_database import insert_db
from bs4 import BeautifulSoup
import requests
from typing import List

class WebSite:
    def __init__(self):
        self.website_connection = connect_database(websites = True)

    def open_website(self, insert_link: str) -> BeautifulSoup:
        site = requests.get(insert_link).text
        soup = BeautifulSoup(site, "html.parser")
        return soup

    def text_website(self, website_bs) -> List[str]:
        return website_bs.get_text()

    def get_all_links(self, website_bs: BeautifulSoup)-> List[str]:
        all_links = [a["href"]
                     for a in website_bs('a')
                     if a.has_attr("href")]
        return all_links

    def insert_database(self, website: str, links=None):
        if links:
            insert_website = insert_db(write=website,
                                   review=links)
        else:
            insert_website = insert_db(write=website)
        push_db = self.website_connection.insert_one(insert_website)
        return print(f"Inserted one: {push_db.inserted_id}")


        

        

