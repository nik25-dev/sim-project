from payments.cart import cart

def subtotal():
    return sum(item["price"] * item["qty"] for item in cart)
