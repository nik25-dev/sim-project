from payments.pricing import subtotal
from payments.discounts import apply_discount
from payments.tax import add_tax

def checkout(code=""):
    return add_tax(apply_discount(subtotal(), code))
