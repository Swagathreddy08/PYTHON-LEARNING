# discount_calculator.py

price = float(input("Enter product price: "))
customer_type = input("Enter customer type (regular/member/vip): ").lower()
promo = input("Do you have a promotional code? (yes/no): ").lower()

if price < 0:
    print("Invalid price")

elif customer_type == "regular":
    if promo == "yes":
        discount_rate = 0.10
    else:
        discount_rate = 0.05

elif customer_type == "member":
    if promo == "yes":
        discount_rate = 0.20
    else:
        discount_rate = 0.15

elif customer_type == "vip":
    if promo == "yes":
        discount_rate = 0.30
    else:
        discount_rate = 0.25

else:
    print("Invalid customer type")
    discount_rate = 0

# Calculate discount
discount_amount = price * discount_rate
final_price = price - discount_amount

print("\nOriginal Price:", price)
print("Discount Amount:", discount_amount)
print("Final Price:", final_price)