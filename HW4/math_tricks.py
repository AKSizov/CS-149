# math_tricks.py
# hw 4.4
from statistics import NormalDist
from math import pi


def sphere_volume(radius):
    return (4/3)*pi*(radius**3)


def normal_pdf(m, s, x):
    return NormalDist(mu=m, sigma=s).pdf(x)
