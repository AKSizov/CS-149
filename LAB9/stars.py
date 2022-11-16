"""Produce star patterns demonstrating nested for loops.

Adapted from Lewis and Loftus by Nancy and Arch Harris.
Converted to Python by Alvin Chao and Nathan Sprague

Author: Alex Sizov
Version: Nov 16, 2022
"""


def example(num_rows):
    """First example.

    prints example.

    Args:
        num_rows (int): number of rows to print

    Returns:
        pattern(str): string pattern

    """
    pattern = ""
    for row in range(num_rows):
        star_count = row + 1
        for col in range(star_count):
            pattern += "*"
        pattern += "\n"
    return pattern


def pattern_a(num_rows):
    """Pattern A.

    **********
    *********
    ********
    *******
    ******
    *****
    ****
    ***
    **
    *.

    Args:
        num_rows (int): number of rows to print

    Returns:
        pattern(str): string pattern

    """
    pattern = ""
    for row in reversed(range(num_rows)):
        star_count = row + 1
        for col in range(star_count):
            pattern += "*"
        pattern += "\n"
    return pattern


def pattern_b(num_rows):
    """Pattern B.

             *
            **
           ***
          ****
         *****
        ******
       *******
      ********
     *********
    **********.

    Args:
        num_rows (int): number of rows to print

    Returns:
        pattern(str): string pattern

    """
    pattern = ""
    for row in reversed(range(num_rows)):
        star_count = row
        for col in range(star_count):
            pattern += " "
        pattern += "*"*(num_rows-star_count)
        pattern += "\n"
    return pattern


def pattern_c(num_rows):
    """Pattern C.

    **********
     *********
      ********
       *******
        ******
         *****
          ****
           ***
            **
             *.


    Args:
        num_rows (int): number of rows to print

    Returns:
        pattern(str): string pattern

    """
    pattern = ""
    for row in range(num_rows):
        star_count = row
        for col in range(star_count):
            pattern += " "
        pattern += "*"*(num_rows-star_count)
        pattern += "\n"
    return pattern


if __name__ == "__main__":
    """Main method."""
    num_rows = int(input("Enter a positive integer for the number of rows: "))

    while (num_rows <= 0):
        print("\nYou did not enter a POSITIVE number.")
        print(f"You entered {num_rows}!\n")
        num_rows = input("Enter a positive number",
                         "for the number of rows: ")

    # first example: stars per row goes from 1 to num_rows
    print("First Example")
    print("-----------------")
    print(example(num_rows))
    print("-----------------")  # separator between patterns
    print(pattern_a(num_rows))
    print("-----------------")  # separator between patterns
    print(pattern_b(num_rows))
    print("-----------------")  # separator between patterns
    print(pattern_c(num_rows))
