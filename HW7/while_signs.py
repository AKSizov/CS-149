"""Sort positive and negative numbers.

Author: Alexander Sizov
Version: 10/19/2022

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""
# hw 7.1


def get_positive_negative():
    """Sorts positive and negative numbers.

    Returns:
        tuple: sorted numbers
    """
    negatives = []
    positives = []
    x = input("Input? ")
    while (not x.isalpha()):
        x = float(x)
        if (x < 0):
            negatives.append(x)
        elif (x > 0):
            positives.append(x)
        x = input("Input? ")
    return (positives, negatives)
