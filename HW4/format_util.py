# format_util.py
# hw 4.1


# $100,000.00
# 300.45 CHF
# 7:30:00
# 12:08:03


def format_money(prefix, value, suffix):
    """Return a string representation of the provided amount of money.

    The result will be comma separated, with two decimal places.

    Args:
        prefix (str): currency symbol to display before (e.g., "$")
        value (float): amount of money
        suffix (str): currency symbol to display after (e.g., "CHF")

    Returns:
        Correctly formatted money string
    """
    return f"{prefix}{value:,.2f} {suffix}"


def format_time(hour, minute, second):
    """Format the given time as HH:MM:SS in 24-hour format.

    The hour can be either 1 or 2 digits, but the minute and second must be
    two digits.

    Args:
        hour (int): the hour (0 to 23)
        minute (int): the minute (0 to 59)
        second (int): the second (0 to 59)

    Returns:
        Formatted time string
    """
    return f"{hour}:{minute:02d}:{second:02d}"


if __name__ == "__main__":
    # print four lines of test output (first is done for you)
    print(format_money("$", 100000.0, ""))
    print(format_money("", 300.45, "CHF"))
    print(format_time(7, 30, 0))
    print(format_time(12, 8, 3))
