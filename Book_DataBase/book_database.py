import pandas as pd
import numpy as np
import datetime

valid_author_genders = ["male","female","non-binary"]

class Author:

    def __init__(self,name,nationality,gender):

        if gender not in valid_author_genders:
            raise ValueError(str(gender)+" is an invalid author gender. Valid options are: "+str(valid_author_genders))

        self.name = name
        self.nationality = nationality
        self.gender = gender

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

class Audio_Book(Book):
    def __init__(self,title,author,book_format,source,owned,date_started,date_finished,series,genre,pub_year,rating,num_times_read,reading_language,audio_length):

        if (type(audio_length) != type(datetime.timedelta())):
            raise TypeError(str(type(audio_length)) + " is an invalid data type. The valid data type is datetime.timedelta().")

        if book_format != "Audio":
            raise ValueError(str(book_format) +" is an invalid book type in this class. Only 'Audio' books are allowed.")

        Book.__init__(self,title,author,book_format,source,owned,date_started,date_finished,series,genre,pub_year,rating,num_times_read,reading_language)
        self.audio_length = audio_length

class Physical_Book(Book):

    def __init__(self,title,author,book_format,source,owned,date_started,date_finished,series,genre,pub_year,rating,num_times_read,reading_language,pages):

        if book_format != ("Hardback" or "Paperback" or "e-book"):
            raise ValueError(str(book_format) +" is an invalid book type in this class. Only 'Paperback' or 'Hardback' or 'e-book' books are allowed.")

        Book.__init__(self,title,author,book_format,source,owned,date_started,date_finished,series,genre,pub_year,rating,num_times_read,reading_language)
        self.pages = pages

charles_duhigg = Author("Charles Duhigg","USA","male")
the_power_of_habit = Audio_Book("The Power of Habit", charles_duhigg, "Audio", "Overdrive", False,
                                np.datetime64("2022-02-02"), np.datetime64("2022-02-14"), False, "Selfhelp NF", 2012,
                                4.0, 1, "English", datetime.timedelta(hours=10, minutes=53))
print(the_power_of_habit.author.gender)
print(the_power_of_habit.audio_length)


amy_kaufman = Author("Amy Kaufman","Australia","female")
jay_kristoff = Author("Jay Kristoff","Australia","male")
illuminae = Physical_Book("Illuminae",[amy_kaufman,jay_kristoff],"Hardback","Library N",False,np.datetime64("2022-01-29"),np.datetime64("2022-02-19"),True,"Sci-Fi",2015,1.0,1,"German",608)
print(illuminae.pages)