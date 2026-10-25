from payments.cart import cart

def make_receipt(total):
    lines = [f'{i["name"]} x{i["qty"]}' for i in cart]
    return "\n".join(lines + [f"TOTAL: {total}"])
