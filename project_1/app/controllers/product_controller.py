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

    