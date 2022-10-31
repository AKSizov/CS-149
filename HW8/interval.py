"""Exercise 8.1 Intervals.

Author: Alex Sizov
Version: 8/26/2022

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""
# hw 8.1


def in_interval(f_list, lb, ub, closed=True):
    """Checks if float is within interval.

    Args:
        f_list(list): list of floats.
        lb(float): lower bound of the interval.
        ub(float): upper bound of the interval.
        closed(bool): if the interval is closed.

    Returns:
        list: list of floats within interval.
    """
    a_list = []
    for num in f_list:
        if (closed and num == lb):
            a_list.append(num)
        if (closed and num == ub):
            a_list.append(num)
        if (num > lb and num < ub):
            a_list.append(num)
    return a_list


print(in_interval([20.1, 0.0, 2.5, 1.4, -6.0], 0.0, 5.0))
