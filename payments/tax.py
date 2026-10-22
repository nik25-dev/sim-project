TAX_RATE = 0.05

def add_tax(amount):
    return round(amount * (1 + TAX_RATE), 2)
