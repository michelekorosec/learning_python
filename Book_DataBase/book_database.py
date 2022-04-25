class Author:

    def __init__(self,name,nationality,gender):

        self.name = name
        self.nationality = nationality
        self.gender = gender


class Book:

    def __init__(self,title,author,type,source,owned,date_started,date_finished,series,genre,pub_year,rating,num_times_read,reading_language):

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