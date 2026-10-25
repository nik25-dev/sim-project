RULES = {"STUDENT10": 0.10, "FEST20": 0.20}

def apply_discount(amount, code=""):
    return amount * (1 - RULES.get(code, 0))
