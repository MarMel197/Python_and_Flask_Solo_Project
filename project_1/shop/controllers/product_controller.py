from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product

import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository

products_blueprint = Blueprint('products',__name__)


@products_blueprint.route('/products')
def products():
    products = product_repository.select_all()
    return render_template('products/index.html', all_products = products)


@products_blueprint.route('/products', methods=['POST'])
def create_product():
    product      = request.form['product_name']
    description  = request.form['product_description']
    inventory    = request.form['stock_on_hand']
    cost         = request.form['cost_price']
    sell         = request.form['sell_price']
    manufacturer_id = request.form['manufacturer_id']
    manufacturer = manufacturer_repository.select(manufacturer_id)
    product      = Product(product, description, inventory, cost, sell, manufacturer)

    product_repository.save(product)
    return redirect('/products')

@products_blueprint.route('/products/new')
def get_form():
    manufacturers = manufacturer_repository.select_all()
    return render_template('products/new.html', manufacturers= manufacturers)


@products_blueprint.route('/products/<id>', methods=['GET'])
def show_product(id):
    product = product_repository.select(id)
    return render_template('products/edit.html', product = product)

@products_blueprint.route('/products/<id>/edit', methods=['GET'])
def edit_product(id):
    product = product_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template('products/edit.html', product = product, manufacturers = manufacturers)


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




