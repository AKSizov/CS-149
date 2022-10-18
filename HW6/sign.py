"""Check if num is positive or negative.

Author: Alexander Sizov
Version: 10/17/2022

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""
# 6.1


def positive_negative(num):
    """Prints if number is positive or negative.

    Args:
        num (float/int): number
    """
    if (num > 0):
        print("%s is positive." % num)
    elif (num < 0):
        print("%s is negative." % num)
    elif (num == 0):
        print("0 is neither negative nor positive.")
