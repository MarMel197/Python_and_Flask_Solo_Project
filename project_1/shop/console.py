import pdb
from models.manufacturer import Manufacturer
from models.product import Product

import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

product_repository.delete_all()
manufacturer_repository.delete_all()


manufacturer_1 = Manufacturer('Heinz', 'Food products')
manufacturer_repository.save(manufacturer_1)

manufacturer_2 = Manufacturer('Baxters', 'Food products')
manufacturer_repository.save(manufacturer_2)

product1 = Product('Lentil Soup', 'Tinned Products', 12, 1, 2, manufacturer_1)
product_repository.save(product1)
product2 = Product('Oxtail Soup', 'Tinned Products', 12, 1, 2, manufacturer_1)
product_repository.save(product2)
product3 = Product('Tomato Soup', 'Tinned Products', 12, 1, 2, manufacturer_1)
product_repository.save(product3)
product4 = Product('Royal Game Soup', 'Tinned Products', 12, 1, 2, manufacturer_2)
product_repository.save(product4)
product5 = Product('Lentil & Bacon Soup', 'Tinned Products', 12, 1, 2, manufacturer_2)
product_repository.save(product5)

product_repository.select_all()



# pdb.set_trace()