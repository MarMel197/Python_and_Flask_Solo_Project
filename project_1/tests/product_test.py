import unittest
from app.models.product import Product

class TestProduct(unittest.TestCase):
    
    def setUp(self):
        self.product = Product('Vegetable Soup', 'Tinned Products', 12, 0.65, 0.90)
    
    def test_product_has_description(self):
        self.assertEqual('Vegetable Soup', self.product.product_name)































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