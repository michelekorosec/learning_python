import pandas as pd
import numpy as np
import datetime

valid_book_formats = ["Audio", "Paperback", "Hardback", "e-book"]
valid_book_sources = ["Spotify","Overdrive","Library N","Library M","Gifted","Bought","Borrowed","Public Bookcase N"]
valid_reading_languages = ["English","German","French"]


class Book:

    def __init__(self,title,author,book_format,source,owned,date_started,date_finished,series,genre,pub_year,rating,num_times_read,reading_language):

        if book_format not in valid_book_formats:
            raise ValueError(str(book_format) +" is an invalid book type. Valid options are: " + str(valid_book_formats))

        if source not in valid_book_sources:
            raise ValueError(str(source)+" is an invalid book source. Valid options are: "+str(valid_book_sources))

        if reading_language not in valid_reading_languages:
            raise ValueError(str(reading_language)+" is an invalid reading language. Valid options are: "+str(valid_reading_languages))

        self.title = title
        self.author = author
        self.book_format = book_format
        self.source = source
        self.owned = owned
        self.date_started = date_started
        self.date_finished = date_finished
        self.series = series
        self.genre = genre
        self.pub_year = pub_year
        self.rating = rating
        self.num_times_read = num_times_read
        self.reading_language = reading_language