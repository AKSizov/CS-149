"""Terminal UI for interacting with generator.py.

Author: Alex Sizov
Version: NOV/25/2022
Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""
# pa 2


import generator as generator


def prompt_for_string(message, min):
    """Prompts the user for a string and returns the result.

    This function performs limited validation on the user's input.

    Args:
        message (str): The prompt for the user
        min (int): The minimum amount of characters to accept

    Returns:
        string: The user's response to the prompt

    """
    userInput = input("%s: " % message)
    while (len(userInput) < min):
        userInput = input("%s: " % message)
    return userInput


def prompt_for_int(message, max):
    """Prompts the user for a number and returns the result.

    This function performs limited validation on the user's input.

    Args:
        message (str): The prompt for the user
        max (int): The max value to be accepted for the number

    Returns:
        int: the user's value

    """
    userInput = 0
    while (userInput < 1 or userInput > max):
        userInput = int(input("%s: " % message))
    return userInput


def prompt_n_display_hints(solution):
    """Repetitively asks the user if they want a hint.

    This function asks the user for what kind of hint they'd like.
    f for first letter of the solution word,
    s for the first 'slice' of the solution word,
    and w for the whole solution word.
    The user can press anything else to refuse hints.

    Args:
        solution (str): The solution word

    """
    PROMPT = """Want a hint? Enter
"f" for first letter
"s" for first slice
"w" for whole word
"n" for none: """
    while (True):
        userInput = input(PROMPT)
        if (userInput == "f"):
            print(solution[0])
        elif (userInput == "s"):
            print(generator.word_splicer([solution])[0])
        elif (userInput == "w"):
            print(solution)
        else:
            return
