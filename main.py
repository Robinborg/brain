import pandas as pd
import matplotlib as mpl
from bs4 import BeautifulSoup
import requests

'''The goal of this program is to create a secondary brain. This program will
function for notetaking, saving links and fetching the important information,
saving the data in a database which can be formed to the users liking and
plotting the information for further learning'''
#How should I represent the data?
#Binarytree, Graph, or what?

def link(insert_link):
    '''open link and open with bs4'''
    website = requests.get(insert_link)
    soup = BeautifulSoup(website.content, 'html.parser')
    print(soup.prettify())
def information_out_of_site(link):
    '''what information to search for?'''
    pass

def podcast(insert_podcast):
    '''save podcast and ask for timestamps'''

def idea(inser_idea):
    '''take idea, write idea under right category and write to file'''

def book(inser_book):
    '''take book, ask for category, ask for input about book and write to file under right category'''
class Brain:
    '''structure the writing to file and loops to keep getting input'''

link('https://xgboost.ai')
