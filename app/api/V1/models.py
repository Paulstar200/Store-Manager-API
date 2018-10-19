from flask import jsonify, request, Blueprint

from flask_restful import Resource, Api


cart = []
salesList = []


class Product():
    # post product by admin
    def create_product(name, price):
        id = len(cart) + 1
        product = {"id": id, "price": price, "name": name}
        cart.append(product)
        return cart

    # get all product store owner and store attendant
    def get_all_products():
        return cart

    # get each product
    def get_each_product(id):
        return cart[id - 1]
