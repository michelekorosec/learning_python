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