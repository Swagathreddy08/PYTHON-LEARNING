def calculate_discount(price, rate):
    if price < 0:
        raise ValueError("price cannot be negative")
    if not 0 <= rate <= 1:
        raise ValueError("rate must be between 0 and 1")
    return price * (1 - rate)
print(calculate_discount(100, 1.10))
