"""Exercise 8.3 Shift Cipher.

Author: Alex Sizov
Version: 8/26/2022

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""
# hw 8.3


def encode(input, offset):
    """Caesar cipher.

    Args:
        input(string): text to shift
        offset(int): amount to offset text

    Returns:
        string: encoded text
    """
    fin = ""
    for c in input:
        if (c.isalpha()):
            ind = ord(c) + offset
            if (ind > 122):
                ind = ind-26
            if (ind < 97):
                ind = ind+26
            fin = fin+chr(ind)
        else:
            fin = fin+c
    return fin


# print(encode("the quick brown fox.", 4))
