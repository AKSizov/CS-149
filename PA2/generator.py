"""Simplified 7 little words game.

Author: Alex Sizov
Version: NOV/25/2022
Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""
# pa 2


def word_splicer(solutions):
    """Splits words into slices.

    This function cuts every word in the list into 2 peices and returns a list.

    Args:
        solutions (list): The list of words to split

    Returns:
        list: The split words.

    """
    return_list = []
    for solution in solutions:
        return_list.append(solution[:len(solution)//2])
        return_list.append(solution[len(solution)//2:])
    return return_list


def clue_to_string(clues):
    """Makes clues user friendly.

    Returns the clues in a user-friendly format.

    Args:
        clues (list): The clues to print

    Returns:
        string: user-friendly clue string

    """
    user_index = 1
    result_string = ""
    for clue in clues:
        result_string += "%i) %s\n" % (user_index, clue)
        user_index += 1
    return result_string


def board_to_string(board):
    """Prints the slices out nicely.

    Returns string containing the board with the slices in it.

    Args:
        board (list): The slices to print out

    Returns:
        string: the board string

    """
    user_index = 1
    result_string = ""
    for slice in board:
        num_dashes = (len(slice)+9)
        result_string += "-"*num_dashes+"\n"
        result_string += "| %02d | %s |" % (user_index, slice)+"\n"
        result_string += "-"*num_dashes+"\n"
        user_index += 1
    return result_string
