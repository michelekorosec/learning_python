import pandas as pd
import numpy as np
import datetime
import json
from book_class import Book
from audio_book_class import Audio_Book
from author_class import Author
from physical_book_class import Physical_Book


# Use Case1: Create author object
charles_duhigg = Author("Charles Duhigg","USA","male")

# Use Case2: Create audio book object & associated queries
the_power_of_habit = Audio_Book("The Power of Habit", charles_duhigg, "Audio", "Overdrive", False,
                                np.datetime64("2022-02-02"), np.datetime64("2022-02-14"), False, "Selfhelp NF", 2012,
                                4.0, 1, "English", datetime.timedelta(hours=10, minutes=53))
print(the_power_of_habit.author.gender)
print(the_power_of_habit.audio_length)


# Use Case3: Create Physical Book with multiple authors & associated queries
amy_kaufman = Author("Amy Kaufman","Australia","female")
jay_kristoff = Author("Jay Kristoff","Australia","male")
illuminae = Physical_Book("Illuminae",[amy_kaufman,jay_kristoff],"Hardback","Library N",False,np.datetime64("2022-01-29"),np.datetime64("2022-02-19"),True,"Sci-Fi",2015,1.0,1,"German",608)
print(illuminae.pages)
print(illuminae.author[1].gender)