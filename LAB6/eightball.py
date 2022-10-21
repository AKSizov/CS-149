"""Simulate a magic 8-ball. Original code by Arch Harris and Nancy Harris.

Author: Alex Sizov
Version: 8/21/2022

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""
import random


def input_yes_no(prompt):
    """Displays the given prompt followed by [yes/no].

    Returns true if the next line of user input is "y" or "yes"
    ignoring case, false otherwise.

    Args:
        prompt(string):  the text to display

    Returns:
        bool: return true if yes, false if no
    """
    x = input("%s [yes/no]: " % prompt)
    if (x.lower() == "yes" or x.lower() == "y"):
        return True
    else:
        return False


def get_question(prompt):
    """Gets the next question from the user.

    The length of the question must be between 1 and 60 characters, and the
    question must end with a '?'. This function keeps asking the user for a
    question until they enter a valid one.

    Args:
        prompt(string):  the text to display

    Returns:
        (string): the user's question
    """
    valid = False
    x = ""
    while (not valid):
        valid = True
        x = input(prompt)
        if (x[-1] != '?'):
            print("Your question must end with a ?")
            valid = False
        if (len(x) > 60):
            print("Your question is too long")
            valid = False
        if (len(x) < 1):
            print("Your question is blank")
            valid = False
    return x


if __name__ == '__main__':
    """Run Main function."""
    print("Magic 8 Ball\n")
    # Run the program as long as the user wants
    while (input_yes_no("\nDo you want to ask a question? ")):
        # get the next question
        question = get_question("What is your question? ")
        print()
        # pick a random answer
        answer_index = random.randint(1, 20)
        answers = ["", "Signs point to yes.", "Yes.", "Reply hazy, try again.",
                   "Without a doubt.",  "My sources say no.",
                   "As I see it, yes.", "You may rely on it.",
                   "Concentrate and ask again.",
                   "Outlook not so good.", "It is decidedly so.",
                   "Better not tell you now.", "Very doubtful.",
                   "Yes - definitely.", "It is certain.",
                   "Cannot predict now.", "Most likely.",
                   "Ask again later.", "My reply is no.",
                   "Outlook good.", "Don't count on it.", "HUH?"]
        answer_str = answers[answer_index]
        # output the results
        print(f"Question: {question}\n")
        print(f"  Answer: {answer_str}\n")
    print("Goodbye!")
