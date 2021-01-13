import unittest
from src.drinks import Drinks

class TestDrinks(unittest.TestCase):

    def setUp(self):
        self.drinks = Drinks("Platform C", 5.00)


    def test_drink_has_name(self):
        self.assertEqual("Platform C", self.drinks.name)    