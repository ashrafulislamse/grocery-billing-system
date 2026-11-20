# Grocery Billing System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Dependencies](https://img.shields.io/badge/Dependencies-none-success)
![Platform](https://img.shields.io/badge/Platform-Console-lightgrey)

A menu-driven grocery checkout program built in Python for a pair assignment in BIT1054 Fundamental of Computational Thinking. The program manages a product catalogue, a shopping cart, tiered discount rules, and receipt printing, with input validation on every prompt so wrong input never crashes the program.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Discount Rules](#discount-rules)
- [Input Validation](#input-validation)
- [Project Structure](#project-structure)
- [Sample Output](#sample-output)
- [Team](#team)

## Features

- Menu-driven interface with six options
- Product catalogue of ten grocery items with prices in Ringgit Malaysia (RM)
- Shopping cart that combines repeated items into a single quantity
- Tiered bulk discount plus an extra member discount
- Itemised receipt printed after payment confirmation
- Input validation on every prompt

## Getting Started

### Prerequisites

- Python 3.6 or later

No external libraries are required. The program runs on the standard library alone.

### Running the Program

```bash
python main.py
```

## Usage

| Option | Action |
|---|---|
| 1 | View the product catalogue |
| 2 | Add an item to the cart (product number and quantity) |
| 3 | Remove an item from the cart |
| 4 | View the cart with line totals |
| 5 | Checkout: membership question, discounts, total, receipt |
| 6 | Exit the program |

Enter `0` at any product or item prompt to cancel the action and return to the menu.

## Discount Rules

| Rule | Discount |
|---|---|
| Subtotal of RM 200 or more | 10% |
| Subtotal of RM 100 or more (below RM 200) | 5% |
| Member, any subtotal | extra 5% |

Discounts stack: a member with a RM 250 subtotal gets 10% plus 5%.

## Input Validation

Every prompt checks its input and asks again on invalid entry:

| Invalid input | Program response |
|---|---|
| Letters where a number is expected | Invalid input. Please enter a number. |
| Menu choice outside 1 to 6 | Invalid choice. Please enter a number from 1 to 6. |
| Product number that does not exist | That product number does not exist. |
| Quantity of 0 or less | Quantity must be at least 1. |
| Answer other than y/n at a yes or no question | Please answer y (yes) or n (no). |
| Remove number not in the list | That number is not in the list. |

## Project Structure

```
grocery-billing-system/
├── main.py        # menu and user input, all validation happens here
├── products.py    # product catalogue (names and prices in RM)
├── billing.py     # cart and billing rules: add, remove, subtotal, discount, receipt
└── README.md
```

## Sample Output

The menu on startup:

```
========== GROCERY BILLING SYSTEM ==========
1. View products
2. Add item to cart
3. Remove item from cart
4. View cart
5. Checkout
6. Exit
=============================================
Enter your choice (1-6):
```

Adding an item and paying as a member:

```
Enter product number (0 to cancel): 1
Enter quantity: 2
Added 2 x Rice 5kg to your cart.
```

```
Are you a member? (y/n): y

Subtotal: RM 45.00
Discount: RM 2.25
Total payable: RM 42.75
Confirm payment? (y/n): y

========== GROCERY BILLING RECEIPT ==========
Rice 5kg x2 = RM 45.00
---------------------------------------------
Subtotal: RM 45.00
Discount: RM 2.25
TOTAL PAYABLE: RM 42.75
=============================================
Thank you for shopping with us!
Payment complete.
```

## Team

- **Islam Md Ashraful** (BCSSE)
- **Mahmud Husain** (BCSSE)

---

BIT1054 Fundamental of Computational Thinking, Assignment 2 (pair work).
Class 01-202609F0734, City University Malaysia.
