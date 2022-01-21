# Digital brain
A program to keep track of your information.
## Description
The program stores notes, podcasts, books and websites (the website module is able to webscrape).
## Prerequisites 
python 3.8 or newer. Link for [python](https://www.python.org/downloads/)
## Installing mongodb on macos

    brew tap mongodb/brew
    brew install mongodb-community@5.0
Starting mongodb:

    brew services start mongodb-community@5.0
Stopping mongodb:

    brew services stop mongodb-community@5.0
    
## Installation
    git clone https://github.com/Robinborg/digital_brain
    cd digital_brain
    python3 -m pip install -r requirements.txt

## Commands
    
    #Start prompt to enter notes
    python3 main.py -n or python3 main.py --note 
    #Start prompt to enter website and search it for links
    python3 main.py -w or python3 main.py --website
    #Start prompt to enter podcast
    python3 main.py -p or python3 main.py --podcast
    #Start prompt to enter book
    python3 main.py -b or python3 main.py --book 
    
    #Show notes collection
    python3 main.py -sn or python3 main.py --show_notes
    #Show websites collection
    python3 main.py -sw or python3 main.py --show_websites
    #Show podcasts collection
    python3 main.py -sp or python3 main.py --show_podcasts
    #Show books collection
    python3 main.py -sb or python3 main.py --show_books
## About
The program uses:

[Mongodb](https://www.mongodb.com) 

[requests](https://docs.python-requests.org/en/latest/)

[beautifulsoup4](https://beautiful-soup-4.readthedocs.io/en/latest/)

[pymongo](https://pymongo.readthedocs.io/en/stable/index.html)
