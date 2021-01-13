import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Henry", 10.00)


    def test_customer_has_name(self):
        self.assertEqual("Henry", self.customer.name)    
    

    def test_customer_has_wallet(self):
        self.assertEqual(10.00, self.customer.wallet)