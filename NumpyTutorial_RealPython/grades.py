import numpy as np

CURVE_CENTER = 80

grades = np.array([72, 35, 64, 88, 51, 90, 74, 12])

def curve(grades):

    average = grades.mean()
    change = CURVE_CENTER - average
    new_grades = grades + change
    return np.clip(new_grades,grades,100)

print(curve(grades))