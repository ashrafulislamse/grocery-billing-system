# Grocery Billing System - main program
# handles the menu and all user input

from products import display_products, get_product_name
from billing import add_item, remove_item, view_cart, calculate_subtotal, calculate_discount, print_receipt

def read_number(prompt):
    # keep asking until the user types a valid whole number
    while True:
        text = input(prompt)
        # isdigit() is True only for whole numbers, so letters are rejected
        if text.isdigit():
            return int(text)
        print("Invalid input. Please enter a number.")

def ask_yes_no(prompt):
    # ask a yes or no question, True for yes and False for no
    while True:
        answer = input(prompt).lower()
        if answer == "y" or answer == "yes":
            return True
        if answer == "n" or answer == "no":
            return False
        print("Please answer y (yes) or n (no).")

def main():
    cart = {} # shopping cart, each product name with its quantity

    print("Welcome to the Grocery Billing System!")

    while True:
        print()
        print("========== GROCERY BILLING SYSTEM ==========")
        print("1. View products")
        print("2. Add item to cart")
        print("3. Remove item from cart")
        print("4. View cart")
        print("5. Checkout")
        print("6. Exit")
        print("=============================================")
        choice = read_number("Enter your choice (1-6): ")

        if choice == 1:
            # show the catalogue
            display_products()

        elif choice == 2:
            # add an item to the cart
            display_products()
            number = read_number("Enter product number (0 to cancel): ")
            if number == 0:
                print("Cancelled.")
            else:
                name = get_product_name(number)
                if name == "":
                    print("That product number does not exist.")
                else:
                    quantity = read_number("Enter quantity: ")
                    if quantity == 0:
                        print("Quantity must be at least 1.")
                    else:
                        add_item(cart, name, quantity)
                        print("Added", quantity, "x", name, "to your cart.")

        elif choice == 3:
            # remove an item from the cart
            if len(cart) == 0:
                print("Your cart is empty. Nothing to remove.")
            else:
                # list the cart items with numbers, in the order they were added
                cart_list = []
                count = 0
                print()
                print("----- ITEMS IN YOUR CART -----")
                for name in cart:
                    count = count + 1
                    cart_list.append(name)
                    print(count, ".", name, "- quantity:", cart[name])
                print("-----------------------------")

                number = read_number("Enter number of the item to remove (0 to cancel): ")
                if number == 0:
                    print("Cancelled.")
                else:
                    if number > len(cart_list):
                        print("That number is not in the list.")
                    else:
                        name = cart_list[number - 1]
                        remove_item(cart, name)
                        print("Removed", name, "from your cart.")

        elif choice == 4:
            # show the cart
            view_cart(cart)

        elif choice == 5:
            # checkout: apply the shop rules and print the receipt
            if len(cart) == 0:
                print("Your cart is empty. Add items before checkout.")
            else:
                subtotal = calculate_subtotal(cart)
                is_member = ask_yes_no("Are you a member? (y/n): ")
                discount = calculate_discount(subtotal, is_member)
                total = subtotal - discount

                print()
                # :.2f = money format with 2 decimal places
                print(f"Subtotal: RM {subtotal:.2f}")
                print(f"Discount: RM {discount:.2f}")
                print(f"Total payable: RM {total:.2f}")

                confirm = ask_yes_no("Confirm payment? (y/n): ")
                if confirm == True:
                    print_receipt(cart, subtotal, discount, total)
                    cart = {}  # empty the cart for the next customer
                    print("Payment complete.")
                else:
                    print("Checkout cancelled. Your cart is kept.")

        elif choice == 6:
            # exit the program
            print("Thank you for using the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


main()
