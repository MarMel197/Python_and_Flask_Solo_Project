import pdb
from app.models.manufacturer import Manufacturer
from app.models.product import Product

import app.repositories.manufacturer_repository as manufacturer_repository
import app.repositories.product_repository as product_repository

manufacturer_repository.delete_all()
product_repository.delete_all()

manufacturer_1 = Manufacturer('Heinz', 'Food products')
manufacturer_repository.save(manufacturer_1)

manufacturer_2 = Manufacturer('Baxters', 'Food products')
manufacturer_repository.save(manufacturer_2)

product1 = Product('Lentil Soup', 'Tinned Products', 12, 0.50, 0.80, manufacturer_1)
product_repository.save(product1)
product2 = Product('Oxtail Soup', 'Tinned Products', 12, 0.50, 0.80, manufacturer_1)
product_repository.save(product2)
product3 = Product('Tomato Soup', 'Tinned Products', 12, 0.50, 0.80, manufacturer_1)
product_repository.save(product3)
product4 = Product('Royal Game Soup', 'Tinned Products', 12, 0.65, 0.90, manufacturer_2)
product_repository.save(product4)
product5 = Product('Lentil & Bacon Soup', 'Tinned Products', 12, 0.65, 0.90, manufacturer_2)
product_repository.save(product5)

product_repository.select_all()



pdb.set_trace()