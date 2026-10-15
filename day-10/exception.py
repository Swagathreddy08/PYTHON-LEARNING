def read_quantity(text):
    try:
        return int(text)
    except ValueError as exc:
        raise ValueError("quantity must be a whole number") from exc
text2="When one exception occurs while handling another, Python can preserve both causes. This is useful when translating a low-level failure into a domain-specific message."
t2="124553"
print(read_quantity(t2))
print(read_quantity(text2))

