from db.run_sql import run_sql

from models.product import Product
from models.manufacturer import Manufacturer

def select_all():
    products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        product = Product(row['product_name'], row['product_description'], row['stock_on_hand'], row['cost_price'], row['sell_price'], row['id'] )
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
    sql = "INSERT INTO products (product_name, product_description, stock_on_hand, cost_price, sell_price) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [product.product_name, product.product_description, product.stock_on_hand, product.cost_price, product.sell_price]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

def update(user):
    sql = "UPDATE product SET (product_name, product_description, stock_on_hand, cost_price, sell_price) = (%s, %s, %s, %s, %s) WHERE id = %s"
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