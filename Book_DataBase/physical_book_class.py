import pandas as pd
import numpy as np
import datetime
from book_class import Book


class Physical_Book(Book):

    def __init__(self,title,author,book_format,source,owned,date_started,date_finished,series,genre,pub_year,rating,num_times_read,reading_language,pages):

        if book_format != ("Hardback" or "Paperback" or "e-book"):
            raise ValueError(str(book_format) +" is an invalid book type in this class. Only 'Paperback' or 'Hardback' or 'e-book' books are allowed.")

        Book.__init__(self,title,author,book_format,source,owned,date_started,date_finished,series,genre,pub_year,rating,num_times_read,reading_language)
        self.pages = pages

