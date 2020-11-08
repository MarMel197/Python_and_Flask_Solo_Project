from app.db.run_sql import run_sql

from app.models.product import Product
from app.models.manufacturer import Manufacturer
import app.repositories.manufacturer_repository as manufacturer_repository

def select_all():
    products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturers_id'])
        product = Product(row['product_name'], row['product_description'], row['stock_on_hand'], row['item_cost'], row['item_sell'], row['id'] )
        products.append(product)
    return products

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        product = Product(result['product_name'], result['product_description'], result['stock_on_hand'], result['cost_price'], result['sell_price'], result['id'])
    return product

def save(product):
    sql = "INSERT INTO products (product_name, product_description, stock_on_hand, item_cost, item_sell, manufacturers_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.product_name, product.product_description, product.stock_on_hand, product.cost_price, product.sell_price, product.manufacturer.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

def update(product):
    sql = "UPDATE product SET (product_name, product_description, stock_on_hand, item_cost, item_sell) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.product_name, product.product_description, product.stock_on_hand, product.cost_price, product.sell_price]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE  FROM products"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def products(manufacturer):
    products = []

    sql = "SELECT * FROM products WHERE manufacturer_id = %s"
    values = [manufacturer.id]
    results = run_sql(sql, values)

    for row in results:
        product = Product(row['product_name'], row['product_description'], row['stock_on_hand'], row['cost_price'], row['sell_price'], row['id'] )
        products.append(product)
    return products




        # product_name
        # product_description
        # stock_on_hand
        # out_of_stock
        # cost_price
        # sell_price
        # self.id = id