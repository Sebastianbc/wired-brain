from flask import Flask, jsonify, request
from db import db # Import SQL Alchemy from db.py file
from product import Product

products = [
    {'id': 1, 'name': 'Mug brain'},
    {'id': 3, 'name': 'Stairway gray mug'}
]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@db/products'
db.init_app(app) # Initialize flask app

# curl http://localhost:5000/products
# Default http method for Flask's routes is GET
@app.route('/products')
def get_products():
    products = [product.json for product in Product.find_all()]
    if products:
        return jsonify(products), 200
    return f'There are no products available', 404

# curl http://localhost:5000/products/Mug%20brain
@app.route('/products/<name>')
def get_product(name):
    product = Product.find_by_name(name)
    if product:
        #Return the product in a suitable json format
        return jsonify(product.json), 200
    return f'No product available with that information.', 404

# For PowerShell terminal use: Invoke-WebRequest -Uri http://localhost:5000/product -Method POST -Content-Type "application/json" -Body '{"name": "Gigantic nose mug"}' 
# For CMD terminal use: curl -X POST -Uri http://localhost:5000/product --header "Content-Type: application/json" --data "{\"name\": \"Fuzzy key\"}"
@app.route('/product', methods=['POST'])
def post_product():
    #Retrieve the request data (product)
    request_product = request.json

    #Create a new product
    product = Product(None, request_product['name'])

    #Save the product to the database
    product.save_to_db()

    #Return the new product back
    return jsonify(product.json), 201

# curl -X PUT http://localhost:5000/product/3 --header "Content-Type: application/json" --data "{\"name\": \"Super Shaker\"}"
@app.route('/product/<int:id>', methods=['PUT'])
def put_product(id):
    #Retrieve request json body
    update_product = request.json
    
    existing_product = Product.find_by_id(id)
    
    if existing_product:
        existing_product.name = update_product['name']
        existing_product.save_to_db()
        return jsonify(existing_product.json), 200
        
    return f'Product with {id} id not found', 404

# curl -X DELETE http://localhost:5000/product/Gig%20nose%20mug
@app.route('/product/<name>', methods=['DELETE'])
def delete_product(name):
    product = Product.find_by_name(name)
    
    # If product is not null
    if product:
        #Remove product from products list
        product.delete_from_db()
        return jsonify({
            f'{name} product has been removed'
        }), 200
    
    return f'{name} product not found', 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')