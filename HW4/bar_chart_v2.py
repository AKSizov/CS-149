# bar_chart_v2.py
# hw 4.5

import math


def print_bar(label, length):
    """Print a single row of a bar chart.

    The length argument will be converted to an int in order to determine the
    number of "=" symbols to use.

    for example:

    >>> print_bar("Ruby", 3.9)
    Ruby     : ===

    Args:
        label (str): The label for this bar
        length (float): The length of the bar
    """
    length = math.floor(length)
    barchar = "="
    print(f"{label:8.8s} : {barchar * length}")


def print_border(data):
    """Print a correctly-sized border of '-' characters.

    Print a number of '-' symbols equal to the maximum value in data
    (converted to an integer), plus 11.

    Args:
        data: A list of floats
    """
    print("-----------" + "-"*math.floor(max(data)))


def print_bar_chart(labels, data):
    """Print a nicely formatted bar chart.

    The chart will have one row for each of the five entries in the two
    provided lists.

    Args:
        labels: A list of label strings
        data: A list of floats that will determine the length of the bars
    """
    print_border(data)
    print_bar(labels[0], data[0])
    print_bar(labels[1], data[1])
    print_bar(labels[2], data[2])
    print_bar(labels[3], data[3])
    print_bar(labels[4], data[4])
    print_border(data)
    print(f"min: {min(data):.2f} max: {max(data):.2f}")


if __name__ == "__main__":

    # Don't change this!  Just finish the functions above.

    l1 = ['Python', 'Java', 'JavaScript', 'C#', 'PHP']
    d1 = [29.9, 19.1, 8.2, 7.3, 6.2]
    print_bar_chart(l1, d1)
