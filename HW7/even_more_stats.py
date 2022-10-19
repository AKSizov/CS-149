"""JMU basketball scoring for multiple people.

Author: Alexander Sizov
Version: 10/19/2022

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""
# hw 7.3

# > print_stats([('Bird', 500, 100, 50), ('Jordan', 450, 90, 45)])
# Bird scored 500 points, grabbed 100 rebounds, and made 50 assists.
# Jordan scored 450 points, grabbed 90 rebounds, and made 45 assists.
# Total Points: 950
# Total Rebounds: 190
# Total Assists: 95

# MUST USE WHILE LOOPS


def print_stats(stats):
    """Prints each player stats and a summary.

    Args:
        stats (list): list of tuples of players.

    """
    i = 0
    tp = 0
    tr = 0
    ta = 0
    while i < len(stats):
        tp += int(stats[i][1])
        tr += int(stats[i][2])
        ta += int(stats[i][3])
        print("%s scored %s points, grabbed %s rebounds, and made %s assists."
              % (stats[i][0], stats[i][1], stats[i][2], stats[i][3]))
        i += 1
    print("Total Points:   %s" % (tp))
    print("Total Rebounds: %s" % (tr))
    print("Total Assists:  %s" % (ta))
