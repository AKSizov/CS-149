"""Calculator in Python to calculate the annual return on your investment.

Author: Alexander Sizov
Version: 10/17/2022

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""
# hw 6.3


def sales_tax(amount, category, age):
    """Calculates sales tax.

    Args:
        amount (float): the dollar amount to be taxed.
        category (string): a string representing the category of the goods:
            the food category is represented as 'food'.
            the baby items category is represented as 'baby items'.
            any other string is permissible, taxed at the base rate of 5%.
        age (int): the age of the customer in years.

    Returns:
        float: Earnings.

    """
    final = 0
    if (age >= 90):
        return 0
    if (category == "food"):
        if (amount > 200):
            final = ((amount-200)*0.04)+(200*0.03)
        else:
            final = amount*0.03

    elif (category == "baby items"):
        final = amount*0.035

    else:
        final = amount*0.05
    if (age >= 65):
        final = final/2
    return final


print(sales_tax(250, "food1", 87))
