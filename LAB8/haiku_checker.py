"""Simulate a magic 8-ball. Original code by Arch Harris and Nancy Harris.

Author: Alex Sizov
Version: 8/21/2022

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""
# lab 8


from pysyllables import get_syllable_count


def check_n_syllables(words, num):
    """Checks if list has n number of syllables.

    Args:
        words(list): list of words on line.
        num(int): number of syllables to check.

    Returns:
        int: This function should return a -1 if the total syllables is < n,
            0 if total syllables = n,
            and 1 if total syllables > n.
    """
    t = 0
    for word in words:
        t += get_syllable_count(word)
    if (t > num):
        return 1
    if (t == num):
        return 0
    if (t < num):
        return -1


def validate_haiku(lines):
    """Checks if haiku is valid.

    Args:
        lines(list): list of list of words.

    Returns:
        string:
            "Valid haiku": if syllables in each line are 5, 7, 5.
            "Invalid haiku, not 3 lines.": if not 3 lines.
            "Line <n> too short. ": if line too short.
            "Line <n> too long. ": if line too long.
    """
    LINES = 3
    PATTERN = [5, 7, 5]

    if (len(lines) != LINES):
        return "Invalid haiku, not 3 lines."

    i = 0
    err_msg = ""
    while i < len(lines):
        if (check_n_syllables(lines[i], PATTERN[i]) < 0):
            err_msg += "Line %s too short. " % (i+1)
        if (check_n_syllables(lines[i], PATTERN[i]) > 0):
            err_msg += "Line %s too long. " % (i+1)
        i += 1

    if (len(err_msg) > 0):
        return err_msg
    else:
        return "Valid haiku"
