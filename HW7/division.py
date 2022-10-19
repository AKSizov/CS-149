"""Division algorithm.

Author: Alexander Sizov
Version: 10/19/2022

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""
# hw 7.2


def divide(n, d):
    """Performs the division algorithm.

    Args:
        n (int): numerator.
        d (int): denominator.

    Returns:
        tuple: quotient, remainder.

    """
    q = 0
    r = n
    while (r >= d):
        q = q+1
        r = r-d
    return (q, r)
