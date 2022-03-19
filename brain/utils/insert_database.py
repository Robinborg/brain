from datetime import datetime
from typing import Dict

date_today = datetime.now().strftime("%d/%m/%Y")

def insert_db(write: str = None,
              review: str = None) -> Dict:
    assert write, "You have to enter something"
    if not review:
        insert_one = {
            "date": date_today,
            "note": write
        }
        return insert_one
    else:
        insert_both = {
            "date": date_today,
            "note": write,
            "review": review
        }
        return insert_both



