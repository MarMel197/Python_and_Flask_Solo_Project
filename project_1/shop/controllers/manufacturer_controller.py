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
    manufacturer_name = request.form['manufacturer_name']
    product      = request.form['product_type']
    # manufacturer = manufacturer_repository.find_by_name(manufacturer_name)
    manufacturer = Manufacturer(manufacturer_name, product)

    manufacturer_repository.save(manufacturer)
    return redirect('/manufacturers')

@manufacturers_blueprint.route('/manufacturers/new')
def get_form():
    return render_template('manufacturers/new.html')


@manufacturers_blueprint.route('/manufacturers/<id>', methods=['GET'])
def show_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('manufacturers/find_manufacturer.html', manufacturer = manufacturer)

@manufacturers_blueprint.route('/manufacturers/<id>/edit', methods=['GET'])
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('manufacturers/edit.html', manufacturer = manufacturer)


@manufacturers_blueprint.route('/manufacturers/<id>', methods=['POST'])
def  update_manufacturer(id):
    manufacturer_name = request.form['manufacturer_name']
    product      = request.form['product_type']
    manufacturer = Manufacturer(manufacturer_name, product,id)
    manufacturer_repository.update(manufacturer)
    return redirect('/manufacturers')


@manufacturers_blueprint.route('/manufacturers/<id>/delete', methods=['POST'])
def delete_manuyfacturer(id):
    manufacturer_repository.delete(id)
    return redirect('/manufacturers')