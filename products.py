# Product catalogue for the Grocery Billing System
# each product name with its price in RM
products = {
    "Rice 5kg": 22.50,
    "Cooking Oil 1L": 15.90,
    "Milk 1L": 6.90,
    "Eggs (30 pcs)": 13.50,
    "Bread Loaf": 4.50,
    "Sugar 1kg": 2.95,
    "Flour 1kg": 3.20,
    "Instant Noodles (5-pack)": 8.50,
    "Coffee 200g": 18.90,
    "Detergent 1kg": 12.30,
}

def display_products():
    # show every product with its number and price
    print()
    print("----- AVAILABLE PRODUCTS -----")
    number = 0
    for name in products:
        price = products[name]
        number = number + 1
        # :.2f shows the price with exactly 2 decimal places (money format)
        print(f"{number}. {name} - RM {price:.2f}")
    print("------------------------------")

def get_product_name(number):
    # find the product name for a catalogue number
    count = 0
    for name in products:
        count = count + 1
        if count == number:
            return name
    return ""
