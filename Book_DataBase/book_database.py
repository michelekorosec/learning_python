import pandas as pd
import numpy as np

valid_author_genders = ["male","female","non-binary"]

class Author:

    def __init__(self,name,nationality,gender):

        if gender not in valid_author_genders:
            raise ValueError(str(gender)+" is an invalid author gender. Valid options are: "+str(valid_author_genders))

        self.name = name
        self.nationality = nationality
        self.gender = gender

valid_book_types = ["Audio","Physical"]
valid_book_sources = ["Spotify","Overdrive","Library N","Library M","Gifted","Bought","Borrowed","Public Bookcase N"]
valid_reading_languages = ["English","German","French"]

class Book:

    def __init__(self,title,author,type,source,owned,date_started,date_finished,series,genre,pub_year,rating,num_times_read,reading_language):

        if type not in valid_book_types:
            raise ValueError(str(type)+" is an invalid book type. Valid options are: "+str(valid_book_types))

        if source not in valid_book_sources:
            raise ValueError(str(source)+" is an invalid book source. Valid options are: "+str(valid_book_sources))

        if reading_language not in valid_reading_languages:
            raise ValueError(str(reading_language)+" is an invalid reading language. Valid options are: "+str(valid_reading_languages))

        self.title = title
        self.author = author
        self.type = type
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

charles_duhigg = Author("Charles Duhigg","USA","male")
the_power_of_habit = Book("The Power of Habit",charles_duhigg,"Audio","Overdrive",False,np.datetime64("2022-02-02"),np.datetime64("2022-02-14"),False,"Selfhelp NF",2012,4.0,1,"English")
print(the_power_of_habit.author.gender)