import pandas as pd
import numpy as np
import datetime
from book_class import Book

class Audio_Book(Book):

    valid_book_formats = ["Audio"]
    valid_book_sources = ["Spotify", "Overdrive", "Library N", "Library M", "Gifted", "Bought", "Borrowed"]

    def __init__(self,title,author,standalone,book_format,source,owned,date_started,date_finished,genre,pub_year,rating,num_times_read,reading_language,audio_length,series=None,num_book=None):

        if (type(audio_length) != type(datetime.timedelta())):
            raise TypeError(str(type(audio_length)) + " is an invalid data type. The valid data type is datetime.timedelta().")

        if book_format not in self.valid_book_formats:
            raise ValueError(str(book_format) +" is an invalid book type. Valid options are: " + str(self.valid_book_formats))

        if source not in self.valid_book_sources:
            raise ValueError(str(source)+" is an invalid book source. Valid options are: "+str(self.valid_book_sources))

        Book.__init__(self,title,author,standalone,book_format,source,owned,date_started,date_finished,genre,pub_year,rating,num_times_read,reading_language,series,num_book)
        self.audio_length = audio_length

    def __str__(self):
        return super(Audio_Book, self).__str__()+'\nLength of audio book: '+str(self.audio_length)+' (hh:mm:ss)'

    def authors(self):
        return super(Audio_Book,self).authors()