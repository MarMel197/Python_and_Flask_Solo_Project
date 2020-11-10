from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.product import Product


# manufacturer_name
# product_type

def select_all():
    manufacturers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(row['manufacturer_name'], row['product_type'], row['id'] )
        manufacturers.append(manufacturer)
    return manufacturers

def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = Manufacturer(result['manufacturer_name'], result['product_type'], result['id'] )
    return manufacturer


def save(manufacturer):
    sql = "INSERT INTO manufacturers (manufacturer_name, product_type) VALUES (%s, %s) RETURNING *"
    values = [manufacturer.manufacturer_name, manufacturer.product_type]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id
    return manufacturer

def delete_all():
    sql = "DELETE  FROM manufacturers"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(manufacturer):
    sql = "UPDATE manufacturers SET (manufacturer_name, product_type) = (%s, %s) WHERE id = %s"
    values = [manufacturer.manufacturer_name, manufacturer.product_type, manufacturer.id]
    run_sql(sql, values)

def manufacturers(product):
    manufacturers = []

    sql = "SELECT * FROM manufacturers WHERE manufacturer_id = %s"
    values = [manufacturer.id]
    results = run_sql(sql, values)

    for row in results:
        manufacturer = Manufacturer(row['manufacturer_name'], row['product_type'], row['id'])
        manufacturer.append(product)
    return tasks