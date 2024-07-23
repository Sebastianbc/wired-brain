from flask import Flask, jsonify, request

products = [
    {'id': 1, 'name': 'Mug brain'},
    {'id': 3, 'name': 'Stairway gray mug'}
]

app = Flask(__name__)

# curl http://localhost:5000/products
# Default http method for Flask's routes is GET
@app.route('/products')
def get_products():
    #If products list is not null
    if products:
        return jsonify(products), 200
    return f'There are no products available', 404

# curl http://localhost:5000/products/Mug%20brain
@app.route('/products/<name>')
def get_product(name):
    product = [product for product in products if product['name'] == name]
    if product:
        #Return the product in a suitable json format
        return jsonify(product), 200
    
    return f'No product available with that information.', 404

# For PowerShell terminal use: Invoke-WebRequest -Uri http://localhost:5000/product -Method POST -Content-Type "application/json" -Body '{"name": "Gigantic nose mug"}' 
# For CMD terminal use: curl -X POST -Uri http://localhost:5000/product --header "Content-Type: application/json" --data "{\"name\": \"Fuzzy key\"}"
@app.route('/product', methods=['POST'])
def post_product():
    #Retrieve the request data (product)
    request_product = request.json

    #Generate id for the current product
    product_id = max([product['id'] for product in products]) + 1

    #Create a new product
    new_product = {'id': product_id, 'name': request_product['name']}

    #Append new product to current products list
    products.append(new_product)

    #Return the new product back
    return jsonify(new_product), 201

# curl -X PUT http://localhost:5000/product/3 --header "Content-Type: application/json" --data "{\"name\": \"Super Shaker\"}"
@app.route('/product/<int:id>', methods=['PUT'])
def put_product(id):
    #Retrieve request json body
    update_product = request.json
    print(update_product)
    for product in products: 
        if product['id'] == id:
            product['name'] = update_product['name']
            return jsonify(product), 200
        
    return f'Product with {id} id not found', 404

# curl -X DELETE http://localhost:5000/product/Gig%20nose%20mug
@app.route('/product/<name>', methods=['DELETE'])
def delete_product(name):
    product = [product for product in products if product['name'] == name]
    
    # If product is not null
    if product:
        #Remove product from products list
        products.remove(product[0])
        return f'{name} product has been removed', 200
    
    return f'{name} product not found', 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')