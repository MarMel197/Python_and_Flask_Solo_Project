from flask import Flask, render_template, request, redirect
from flas import Blueprint
from app.models.product import Product

import app.repositories.product_repository as product repository
import app.repositories.manufacturer_repository as manufacturer_repository

products_blueprint = Blueprint('products',__name__)


@products_blueprint.route('/products')
def products():
    products = product_repository.select_all()
    return render_template('products/index.html', all_products = products)


@products_blueprint.route('/products', methods=['POST'])
def create_product():
    product      = request.form['product']
    description  = request.form['description']
    inventory    = request.form['inventory']
    cost         = request.form['cost']
    sell         = request.form['sell']

    manufacturer = manufacturer_repository.select(manufacturer_id)
    product      = Product(product, description, inventory, cost, sell)

    product_repository.save(product)
    return redirect('/products')


@products_blueprint.route('/products/<id>', methids=['GET'])
def show_product(id):
    product = product_repository.select(id)
    return render_template('products/find_product.html', product = product)

@products_blueprint.route('/product/<id>/edit', methods=['GET'])
def edit_product(id):
    product = product_repository.select(id)
    manufacturer = manufacturer_repository.select_all()
    return render_template('products/edit_product.html', product = product, all_manufacturers = manufacturers)


@products_blueprint.route('/products/<id>', methods=['POST'])
def  update_product(id):
    product      = request.form['product']
    description  = request.form['description']
    inventory    = request.form['inventory']
    cost         = request.form['cost']
    sell         = request.form['sell']

    manufacturer = manufacturer_repository.select(manufacturer_id)
    product      = Product(product, description, inventory, cost, sell)

    product_repository.update(product)
    return redirect('/products')


@products_blueprint.route('/product/<id>/delete', methods=['POST'])
def delete_product(id):
    product_repository.delete(id)
    return redirect('/products')


# product_name
# product_description
# stock_on_hand
# out_of_stock
# cost_price
# sell_price

