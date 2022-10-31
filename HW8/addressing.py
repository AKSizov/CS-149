"""Exercise 8.2 Street Addresses.

Author: Alex Sizov
Version: 8/26/2022

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""
# hw 8.2


def generate_addresses(street, addr, addr_lim, interval):
    """Generates a list of addresses.

    Args:
        street(string): street to place addresses on.
        addr(int): first number on street.
        addr_lim(int): last number on street.
        interval(int): interval between addresses

    Returns:
        list: list of string addresses
    """
    fin_list = []
    for i in range(addr, addr_lim, interval):
        fin_list.append("%s %s" % (i, street))

    return fin_list
