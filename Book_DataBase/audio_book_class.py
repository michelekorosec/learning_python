import pandas as pd
import numpy as np
import datetime
from book_class import Book

class Audio_Book(Book):
    def __init__(self,title,author,book_format,source,owned,date_started,date_finished,series,genre,pub_year,rating,num_times_read,reading_language,audio_length):

        if (type(audio_length) != type(datetime.timedelta())):
            raise TypeError(str(type(audio_length)) + " is an invalid data type. The valid data type is datetime.timedelta().")

        if book_format != "Audio":
            raise ValueError(str(book_format) +" is an invalid book type in this class. Only 'Audio' books are allowed.")

        Book.__init__(self,title,author,book_format,source,owned,date_started,date_finished,series,genre,pub_year,rating,num_times_read,reading_language)
        self.audio_length = audio_length