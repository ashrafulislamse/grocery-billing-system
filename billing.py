# Cart and billing functions for the Grocery Billing System
# these functions do the calculations only, all input happens in main.py

from products import products

def add_item(cart, name, quantity):
    # add a product to the cart, quantity adds on top if it is already there
    if name in cart:
        cart[name] = cart[name] + quantity
    else:
        cart[name] = quantity

def remove_item(cart, name):
    # del removes the product from the cart dictionary
    del cart[name]

def view_cart(cart):
    # show every item in the cart with its line total
    if len(cart) == 0:
        print()
        print("Your cart is empty.")
        return
    print()
    print("----- YOUR CART -----")
    for name in cart:
        price = products[name]
        quantity = cart[name]
        line_total = price * quantity
        # :.2f = money format with 2 decimal places
        print(f"{name} x{quantity} = RM {line_total:.2f}")
    print("Different items in cart:", len(cart))
    print("---------------------")

def calculate_subtotal(cart):
    # add up price x quantity for every item in the cart
    total = 0
    for name in cart:
        total = total + products[name] * cart[name]
    return total

def calculate_discount(subtotal, is_member):
    # work out the discount in RM using the shop rules
    # 10% off RM 200 or more, 5% off RM 100 or more, members extra 5%
    if subtotal >= 200:
        bulk_rate = 0.10
    elif subtotal >= 100:
        bulk_rate = 0.05
    else:
        bulk_rate = 0

    discount = subtotal * bulk_rate
    if is_member == True:
        discount = discount + subtotal * 0.05
    return discount

def print_receipt(cart, subtotal, discount, total):
    # print the final receipt after payment
    print()
    print("========== GROCERY BILLING RECEIPT ==========")
    for name in cart:
        line_total = products[name] * cart[name]
        print(f"{name} x{cart[name]} = RM {line_total:.2f}")
    print("---------------------------------------------")
    print(f"Subtotal: RM {subtotal:.2f}")
    print(f"Discount: RM {discount:.2f}")
    print(f"TOTAL PAYABLE: RM {total:.2f}")
    print("=============================================")
    print("Thank you for shopping with us!")
