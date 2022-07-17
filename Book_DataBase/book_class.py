import pandas as pd
import numpy as np
import datetime





class Book:

    valid_book_formats = ["Audio", "Paperback", "Hardback", "e-book"]
    valid_book_sources = ["Spotify", "Overdrive", "Library N", "Library M", "Gifted", "Bought", "Borrowed",
                          "Public Bookcase N"]
    valid_reading_languages = ["English", "German", "French"]

    def __init__(self,title,author,standalone,book_format,source,owned,date_started,date_finished,genre,pub_year,rating,num_times_read,reading_language,series=None,num_book=None):

        if book_format not in self.valid_book_formats:
            raise ValueError(str(book_format) +" is an invalid book type. Valid options are: " + str(self.valid_book_formats))

        if source not in self.valid_book_sources:
            raise ValueError(str(source)+" is an invalid book source. Valid options are: "+str(self.valid_book_sources))

        if reading_language not in self.valid_reading_languages:
            raise ValueError(str(reading_language)+" is an invalid reading language. Valid options are: "+str(self.valid_reading_languages))

        self.title = title
        self.author = author
        self.standalone = standalone
        if standalone == True:
            self.series = None
            self.num_book = None
        else:
            self.series = series
            self.num_book = num_book
        self.book_format = book_format
        self.source = source
        self.owned = owned
        self.date_started = date_started
        self.date_finished = date_finished
        self.genre = genre
        self.pub_year = pub_year
        self.rating = rating
        self.num_times_read = num_times_read
        self.reading_language = reading_language

    def __str__(self):

        authorlist = ''
        if isinstance(self.author,list):
            for i in range(0,len(self.author)):
                if (i+1) != len(self.author):
                    authorlist = authorlist+str(self.author[i].name)+", "
                else:
                    authorlist = authorlist + str(self.author[i].name)
        else:
            authorlist = self.author.name

        standaloneseriesstring = ''
        if self.standalone == True:
            standaloneseriesstring = 'This is a Standalone book.'
        else:
            standaloneseriesstring = 'This is book number '+str(self.num_book)+' in a series of '+str(self.series.num_books)+' books total.'

        ownedstring = ''
        if self.owned == True:
            ownedstring = 'Yes'
        else:
            ownedstring = 'No'

        return 'Book Title: '+str(self.title)+'\nAuthor(s): '+str(authorlist)+'\n'+str(standaloneseriesstring)+'\nFormat read in: '+str(self.book_format)\
               +'\nI own this book: '+str(ownedstring)+'\nRead from '+str(self.date_started)+' to '+str(self.date_finished)+'\nGenre: '+str(self.genre)\
               +'\nRating: '+str(self.rating)+'/5\nNumber of times read: '+str(self.num_times_read)+'\nReading Language: '+str(self.reading_language)

    def authors(self):

        author_string = ''
        
        if (type(self.author) == type([])):
            author_string = 'Multiple authors: '
            for a in self.author:
                if a != self.author[-1]:
                    author_string += str(a.name)+ ' ('+str(a.gender)+', '+str(a.nationality) +'), '
                else:
                    author_string += str(a.name)+ ' ('+str(a.gender)+', '+str(a.nationality) +')'
        else:
            author_string = 'Author: '+str(self.author.name)+ ' ('+str(self.author.gender)+', '+str(self.author.nationality) +')'

        return author_string
