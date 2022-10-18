"""Color manipulation utilities.

Author: Alexander Sizov
Version: 10/17/2022

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""
# hw 6.5


def adjust_brightness(color, offset):
    """Adds to all channels.

    Args:
        color (list): list of RGB values.
        offset (int): amount to increase brightness by.

    Returns:
        list: list of new RGB values.

    """
    n_color = [0, 0, 0]
    n_color[0] = add(color[0], offset)
    n_color[1] = add(color[1], offset)
    n_color[2] = add(color[2], offset)
    return tuple(n_color)


def add(a, b):
    """Adds with clipped values (0-255).

    Args:
        a (int): int1.
        b (int): int2.

    Returns:
        int: clipped int

    """
    c = a + b
    if (c > 255):
        return 255
    if (c < 0):
        return 0
    return c


def same_color(color1, color2, tolerance):
    """Checks if colors are the same within a tolerance.

    Args:
        color1 (list): first color.
        color2 (list): second color.
        tolerance (int): tolerance between channels.

    Returns:
        bool: if colors are acceptably the same.

    """
    if (abs(color1[0] - color2[0]) > tolerance):
        return False
    if (abs(color1[1] - color2[1]) > tolerance):
        return False
    if (abs(color1[2] - color2[2]) > tolerance):
        return False
    return True
