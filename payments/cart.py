cart = []

def add_item(name, price, qty=1):
    cart.append({"name": name, "price": price, "qty": qty})

def clear_cart():
    cart.clear()
