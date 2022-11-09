"""Shopping cart class.

Author: CS 149 Instructors and Alex Sizov
Version: NOV/9/2022
Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""

PRICES = {
    'Air Fryer': 200,
    'Boots': 120,
    'Cat Toy': 8,
    'Dog Food': 15,
    'Electric Toothbrush': 12,
    'FitBit': 100,
    'Gaming Chair': 325,
    'Hydro Flask': 50
}


class ShoppingCart:
    """The ShoppingCart class represents a shopping cart.

    Attributes:
        contents (str): list containing items

    """

    contents = []

    # def __init__(self, contents):
    #     """Initialize a new empty Section.

    #     Args:
    #         course_code (str): The course identifier, e.g. 'CS 149'
    #         section_number (int): The number for this section
    #         capacity (int): The maximum number of students for this section

    #     """
    #     self.contents = contents

    def buy(self, product):
        """Adds item to cart.

        Misleading name, does not actually buy anything

        Args:
            product (string): Product to add to cart.

        """
        self.contents.append(product)

    def total_cost(self):
        """Returns total cost of all items in cart.

        Uses external datasource PRICES.

        Returns:
            int: sum of prices.

        """
        t = 0
        for i in self.contents:
            t += PRICES[i]
        return t


# cart = ShoppingCart()
# cart.buy("Boots")
# cart.buy("FitBit")
# print(cart.total_cost())
