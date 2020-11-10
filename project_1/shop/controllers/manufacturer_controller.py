from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer

import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

manufacturers_blueprint = Blueprint('manufacturers',__name__)


@manufacturers_blueprint.route('/manufacturers')
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template('manufacturers/index.html', all_manufacturers = manufacturers)


@manufacturers_blueprint.route('/manufacturers', methods=['POST'])
def create_manufacturer():
    manufacturer      = request.form['manufacturer_name']
    product  = request.form['product_type']
    # 
    manufacturer_id = request.form['manufacturer_id']
    manufacturer = manufacturer_repository.select(manufacturer_id)
    manufacturer = Manufacturer(manufacturer, product)

    manufacturer_repository.save(manufacturer)
    return redirect('/manufacturers')

@manufacturers_blueprint.route('/manufacturers/new')
def get_form():
    #
    manufacturers = manufacturer_repository.select_all()
    return render_template('manufacturers/new.html', manufacturers= manufacturers)


@manufacturers_blueprint.route('/manufacturers/<id>', methods=['GET'])
def show_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('manufacturers/find_manufacturer.html', manufacturer = manufacturer)

@manufacturers_blueprint.route('/manufacturers/<id>/edit', methods=['GET'])
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    manufacturer = manufacturer_repository.select_all()
    #
    return render_template('manufacturers/edit.html', product = product, all_manufacturers = manufacturers)


@manufacturers_blueprint.route('/manufacturers/<id>', methods=['POST'])
def  update_manufacturer(id):
    manufacturer = request.form['manufacturer_name']
    product      = request.form['product_type']
#
    manufacturer = manufacturer_repository.select(manufacturer_id)
    product      = Product(product, description, inventory, cost, sell)
#
    manufacturer_repository.update(product)
    return redirect('/manufacturers')


@manufacturers_blueprint.route('/manufacturers/<id>/delete', methods=['POST'])
def delete_manuyfacturer(id):
    manufacturer_repository.delete(id)
    return redirect('/manufacturers')