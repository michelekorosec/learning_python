import pandas as pd
import numpy as np
import datetime
from book_class import Book


class Physical_Book(Book):

    valid_book_formats = ["Paperback", "Hardback", "e-book"]
    valid_book_sources = ["Overdrive", "Library N", "Library M", "Gifted", "Bought", "Borrowed",
                          "Public Bookcase N"]

    def __init__(self,title,author,standalone,book_format,source,owned,date_started,date_finished,genre,pub_year,rating,num_times_read,reading_language,pages,series=None,num_book=None):

        if book_format not in self.valid_book_formats:
            raise ValueError(str(book_format) +" is an invalid book type. Valid options are: " + str(self.valid_book_formats))

        if source not in self.valid_book_sources:
            raise ValueError(str(source)+" is an invalid book source. Valid options are: "+str(self.valid_book_sources))

        Book.__init__(self,title,author,standalone,book_format,source,owned,date_started,date_finished,genre,pub_year,rating,num_times_read,reading_language,series,num_book)
        self.pages = pages

    def __str__(self):
        return super(Physical_Book, self).__str__()+'\nNumber of pages: '+str(self.pages)

    def authors(self):
        return super(Physical_Book,self).authors()