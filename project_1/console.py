import pdb
from models.manufacurer import Manufacturer
from models.product import Product

import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

manufacturer_repository.delete_all()
product_repository.delete_all()

product1 = Product ('Lentil Soup', 'Tinned Products', 12, False, 0.50, 0.80)
#product_repository.save(product1)
product2 = Product ('Oxtail Soup', 'Tinned Products', 12, False, 0.50, 0.80)
#product_repository.save(product2)
product3 = Product ('Tomato Soup', 'Tinned Products', 12, False, 0.50, 0.80)
#product_repository.save(product3)
product4 = Product ('Royal Game Soup', 'Tinned Products', 12, False, 0.65, 0.90)
#product_repository.save(product3)
product3 = Product ('Lentil & Bacon Soup', 'Tinned Products', 12, False, 0.65, 0.90)
#product_repository.save(product3)

#user_repository.select_all()

manufacturer_1 = Manufacturer('Heinz', 'Food products')
#manufacturer_repository.save(manufacturer_1)

manufacturer_2 = Manufacturer('Baxters', 'Food products')
#manufacturer_repository.save(manufacturer_2)

pdb.set_trace()