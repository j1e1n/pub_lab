import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer


class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink_1 = Drink("cider", 4.00)
        self.drink_2 = Drink("beer", 3.50)
        self.customer_1 = Customer("Henry", 10.00)



    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_can_find_drink_by_name(self):
        self.pub.add_drink(self.drink_1)
        self.pub.add_drink(self.drink_2)
        drink = self.pub.find_drink_by_name("cider")
        self.assertEqual("cider", drink.name)  


    def test_can_add_to_till(self):
        self.pub.add_to_till(5.00)
        self.assertEqual(105.00, self.pub.till)


    def test_can_remove_customer_cash(self):
        self.pub.remove_customer_cash(5.00, self.customer_1)
        self.assertEqual(5.00, self.customer.wallet)
       


