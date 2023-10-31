#### Try to use map and reduce in the next 3 exercises
# 1)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#
import pandas as pd
from functools import reduce

simba=["Simba and Nala are lions.", "I laugh in the face of danger.", "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]

def count_simba(list_of_strings: list):
    return reduce(lambda x,y: x+y, map(lambda x: x.count("Simba"), list_of_strings))

count_simba(simba)

# 2)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 
import datetime

dates=[datetime.date(2001, 1, 1), datetime.date(2032, 1, 2), datetime.date(2019, 1, 3), datetime.date(2019, 1, 4), datetime.date(2019, 1, 5), datetime.date(2019, 1, 6), datetime.date(2019, 1, 7), datetime.date(2019, 1, 8), datetime.date(2019, 1, 9), datetime.date(2019, 1, 10)]

def get_day_month_year(list_of_dates: list):
    return pd.DataFrame(map(lambda x: {"day": x.day, "month": x.month, "year": x.year}, list_of_dates))

get_day_month_year(dates)

# 3) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#

from functools import reduce
from geopy.distance import geodesic as GD

coordinates=[((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]    

def compute_distance(list_of_coordinates: list):
    return list(map(lambda x: GD(x[0], x[1]).km, list_of_coordinates))

compute_distance(coordinates)

# 4)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13

from functools import reduce


list_1=[[2], 3, [[1,2],5]] 

def sum_general_int_list(list_of_integers: list):
    return reduce(lambda x,y: x+y, map(lambda x: sum_general_int_list(x) if type(x)==list else x, list_of_integers))

sum_general_int_list(list_1)