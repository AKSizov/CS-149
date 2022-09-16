# convert.py
# hw 4.3

def celsius_to_fahrenheit(x):
    return ((9/5)*x)+32


def kilometers_to_miles(x):
    return x/1.60934


def miles_to_kilometers(x):
    return x*1.60934


def meters_per_second_to_miles_per_hour(x):
    return kilometers_to_miles(x*3.6)


def miles_per_hour_to_meters_per_second(x):
    return miles_to_kilometers(x/3.6)
