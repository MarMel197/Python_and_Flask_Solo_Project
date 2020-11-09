import unittest
from app.models.product import Product

class TestProduct(unittest.TestCase):
    
    def setUp(self):
        self.product = Product('Vegetable Soup', 'Tinned Products', 12, 0.65, 0.90)
        self.product1 = Product('Noodle soup', 'Tinned Products', 24, 0.45, 0.75)
    
    def test_product_has_name(self):
        self.assertEqual('Vegetable Soup', self.product.product_name)
    
    def test_another_product_has__name(self):
        self.assertEqual('Noodle soup', self.product1.product_name)

    def test_product_has_description(self):
        self.assertEqual('Tinned Products', self.product.product_description)
    
    def test_another_product_has__description(self):
        self.assertEqual('Tinned Products', self.product1.product_description)

    def test_product_has_stock_on_hand(self):
        self.assertEqual(12 , self.product.stock_on_hand)
    
    def test_another_product_has__stock_on_hand(self):
        self.assertEqual(24 , self.product1.stock_on_hand)

    def test_product_has_cost_price(self):
        self.assertEqual(0.65 , self.product.cost_price)
    
    def test_another_product_has__cost_price(self):
        self.assertEqual(0.45 , self.product1.cost_price)

    def test_product_has_sell_price(self):
        self.assertEqual(0.90 , self.product.sell_price)
    
    def test_another_product_has__sell_price(self):
        self.assertEqual(0.75 , self.product1.sell_price)

# product_name
# product_description
# stock_on_hand
# out_of_stock
# cost_price
# sell_price




























    # def test_task_has_description(self):
    #     self.assertEqual("Walk Dog", self.task.description)
        
        
    # def test_task_has_assignee(self):
    #     self.assertEqual("Ada Lovelace", self.task.assignee)
        
        
    # def test_task_has_duration(self):
    #     self.assertEqual(60, self.task.duration)
    
    
    # def test_task_completed_starts_false(self):
    #     self.assertEqual(False, self.task.completed)
        
    
    # def test_can_mark_test_complete(self):
    #     self.task.mark_complete()
    #     self.assertEqual(True, self.task.completed)