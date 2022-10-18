"""Sort even and odd numbers.

Author: Alexander Sizov
Version: 10/17/2022

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""
# 6.4

card_tuple = ('0', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10')
royal_cards = ('J', 'Q', 'K')


def get_value(card):
    """Gets card value.

    Args:
        card (string): the card.

    Returns:
        int: number value.

    """
    if card == 'A':
        return 1
    if card.isalpha():
        return 10
    else:
        return int(card)


def dealer_hits(card1, card2):
    """Checks if the dealer should hit.

    Args:
        card1 (string): the first card in the hand.
        card2 (string): the second card in the hand.

    Returns:
        bool: if the dealer should hit.

    """
    total_val = get_value(card1) + get_value(card2)
    if (card1 == 'A' and card2 in str(royal_cards)):
        return False
    if (card2 == 'A' and card1 in str(royal_cards)):
        return False
    if (total_val < 17):
        return True
    if (total_val >= 17):
        return False


print(dealer_hits('A', 'J'))
