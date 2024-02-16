
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Database of used clothing items
clothes = [
    {"id": 1, "name": "T-shirt", "size": "M", "color": "Red", "price": 15.00},
    {"id": 2, "name": "Jeans", "size": "L", "color": "Blue", "price": 20.00},
    {"id": 3, "name": "Dress", "size": "S", "color": "Black", "price": 25.00},
]

# Shopping cart
cart = []

# Browse all clothes items
@app.route('/')
def browse():
    return render_template('index.html', clothes=clothes)

# Search for clothes items
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        size = request.form.get('size')
        color = request.form.get('color')
        type = request.form.get('type')
        
        results = [item for item in clothes if (size == item['size'] or size == 'All') and (color == item['color'] or color == 'All') and (type == item['name'] or type == 'All')]
        return render_template('index.html', clothes=results)
    else:
        return render_template('search.html')

# View details of a specific clothes item
@app.route('/item_detail/<int:id>')
def item_detail(id):
    item = [item for item in clothes if item['id'] == id][0]
    return render_template('item_detail.html', item=item)

# Add a clothes item to the shopping cart
@app.route('/add_to_cart/<int:id>')
def add_to_cart(id):
    item = [item for item in clothes if item['id'] == id][0]
    cart.append(item)
    return redirect(url_for('show_cart'))

# View the shopping cart
@app.route('/show_cart')
def show_cart():
    return render_template('cart.html', cart=cart)

# Checkout
@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)
