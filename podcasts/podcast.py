if __name__ == "__main__" and __package__ is None:
    import sys
    from os import path
    path_name = path.dirname(path.abspath(__file)) + "/.."
    sys.path.append(path_name)

from database.connection import connect_database
from utils.insert_database import insert_db

class Podcasts:
    def __init__(self):
        self.podcast_connection = connect_database(podcasts = True)

    def insert_database(self, enter_mode: int):
        if enter_mode == 1:
            podcast_name = input("Enter podcast name:\n")
            podcast_review = input("Enter review:\n")
            insert_podcast = insert_db(write = podcast_name,
                                       review = podcast_review)
            push_db = self.podcast_connection.insert_one(insert_podcast)
            print(f"One insertion: {push_db.inserted_id}")
        if enter_mode == 2:
            podcast_name = input("Enter name:\n")
            insert_podcast = insert_db(write = podcast_name)
            push_db = self.podcast_connection.insert_one(insert_podcast)
            print(f"One insertion: {push_db.inserted_id}")
