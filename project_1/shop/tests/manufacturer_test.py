import unittest
from app.models.manufacturer import Manufacturer

class TestManufacturer(unittest.TestCase):
    
    def setUp(self):
        self.manufacturer = Manufacturer('Heinz', 'Food products')
        self.manufacturer1 = Manufacturer('Baxters', 'Canned food products')
    
    def test_manufacturer_has_name(self):
        self.assertEqual('Heinz', self.manufacturer.manufacturer_name)
    
    def test_another_manufacturer_has__name(self):
        self.assertEqual('Baxters', self.manufacturer1.manufacturer_name)

    def test_manufacturer_has_type(self):
        self.assertEqual('Food products', self.manufacturer.product_type)
    
    def test_another_manufacturer_has__type(self):
        self.assertEqual('Canned food products', self.manufacturer1.product_type)

# manufacturer_name
# product_type