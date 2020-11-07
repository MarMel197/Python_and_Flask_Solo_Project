import unittest
from app.models.manufacturer import Manufacturer

class TestManufacturer(unittest.TestCase):
    
    def setUp(self):
        self.manufacturer = Manufacturer('Heinz', 'Food products')
        self.manufacturer1 = Manufacturer('Baxters', 'Food products')
    
    def test_manufacturer_has_name(self):
        self.assertEqual('Heinz', self.manufacturer.manufacturer_name)
    
    def test_another_manufacturer_has__name(self):
        self.assertEqual('Baxters', self.manufacturer1.manufacturer_name)

# manufacturer_name
# product_type