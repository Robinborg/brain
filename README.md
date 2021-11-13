# brain
The program started from me listening to a podcast. I have since forgotten the podcast and at the same time the name of the person who gave me the idea.
The idea was that he had created a “second-brain”, where he stored all his information and notes. He had different categories for groups of information and could easily retrieve the information at a later time. I have personally a lot of notebooks and general notes that I jot down. But keeping track of all these notebooks is not always easy and sometimes great or extremely interesting ideas I have are lost in the mass of notebooks. I thought I would one day create a central notebook with the general topics or headlines of my personal greatest ideas and that’s when it all came to me. I could just as easily create a program that used a NoSQL database that I could group the information exactly as I wanted and later change the grouping if needed. That is why I wanted to create this digital brain program. 


The first part of the program is just for notes. A simple program that prompts the user for input and then stores that information. 
    
    add_notes = Notes()
    add_notes.notes_db()
    


The second part of the program is for storing and searching websites. There are many times that I come across a very interesting website but then forget it or don’t write it down. Other times there is only a specific part of the website I want to remember. That is why I created a web scraper that would search keywords, emails or other relevant information that the user asks for.
    
    websites = WebSearcher()
    websites.website_opener(insert_link='your_website')
    websites.links_from_website()
    websites.websites_db(both=True)

The third part is for storing books and book reviews. Again a simple program that prompts the user to enter the book and the review, which is saved in the database.

    add_books = Books()
    add_books.books_db(both=True)

The fourth part is for storing podcasts. As of now, it’s just to store the name of the podcast and a note why it was stored. Later on the goal is to have an algorithm that searches for a specific part of the podcast with speech recognition and stores that in a written form.
The fifth and final part would be the program that is able to modify the database and the storage structure of the database.

    add_podcast = Podcast()
    add_podcast.podcast_db(both=True)
    

This way I will never forget a podcast where I get great ideas from.
