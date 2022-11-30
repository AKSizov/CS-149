"""Classes for a transit monitoring application.

FINISHED

Author: Alexander Sizov
Version: Nov 30 2022
"""


class Bus:
    """Bus objects are used to track ridership on individual buses.

    Attributes:
        capacity (int): The maximum number of riders the bus can carry at once
        riders (int): The number of riders currently on the bus
        total_riders (int): The total number of people who have ever ridden
                            on the bus

    """

    def __init__(self, capacity):
        """Newly constructed buses will be empty.

        Args:
            capacity (int): The number of riders this bus can carry
        """
        self.capacity = capacity
        self.riders = 0
        self.total_riders = 0

    def board(self, rider_count):
        """Attempt to board the indicated number of riders.

        Any riders that would bring the bus above capacity are
        ignored.

        Args:
            rider_count (int): The number of riders attempting to board

        """
        seats_available = self.capacity - self.riders
        if rider_count < seats_available:
            self.riders += rider_count
            self.total_riders += rider_count
        else:
            self.riders += seats_available
            self.total_riders += seats_available

    def disembark(self, rider_count):
        """Remove the indicated number of riders from the bus.

        It should not be possible to have fewer than zero riders on
        the bus. If rider_count is greater than the number of riders
        on the bus, then the excess should be ignored.

        Args:
            rider_count (int): The number of riders disembarking.

        """
        self.riders -= rider_count
        if (self.riders < 0):
            self.riders = 0
