"""Unit tests for the ParkingLot class.

FINISHED

Author: Alexander Sizov
Version: Nov 30 2022
"""
import unittest
from transit import Bus


class TestTransit(unittest.TestCase):

    def test_constructor(self):
        bus = Bus(20)
        self.assertEqual(20, bus.capacity)

    def test_board(self):
        bus = Bus(20)
        bus.board(5)
        self.assertEqual(5, bus.riders)

    def test_board2(self):
        bus = Bus(20)
        bus.board(30)
        self.assertEqual(20, bus.riders)

    def test_disembark(self):
        bus = Bus(20)
        bus.board(5)
        bus.disembark(10)
        self.assertEqual(0, bus.riders)


if __name__ == "__main__":
    unittest.main()
