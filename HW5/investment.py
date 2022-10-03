"""Calculator in Python to calculate the annual return on your investment.

Author: Alexander Sizov
Version: 10/3/2022

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""

# investment.py
# lab 5.1

percent_return = 0.12


def calculate_earnings(investment):
    """Calculates earnings given ROI.

    Args:
        investment (float): Initial investment.

    Returns:
        float: Earnings.

    """
    return investment*percent_return


def update_return(rate):
    """Updates global variable.

    Args:
        rate (float): rate of return.

    """
    global percent_return
    percent_return = rate
