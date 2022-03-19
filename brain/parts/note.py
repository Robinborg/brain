if __name__ == "__main__" and __package__ is None:
    import sys
    from os import path
    path_name = path.dirname(path.abspath(__file__)) + "/.."
    sys.path.append(path_name)

from database.connection import connect_database
from utils.insert_database import insert_db

class Notes:
    def __init__(self):
        self.note_connection = connect_database(notes = True)

    def insert_database(self):
        enter_note = input("Enter note:\n")
        insert_note = insert_db(write = enter_note)
        push_db = self.note_connection.insert_one(insert_note)
        print(f"One insertion: {push_db.inserted_id}")


