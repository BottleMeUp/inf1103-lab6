import json
import os
from inventory import Inventory
from product import Product

FILENAME = "inventory.json"


def load_inventory(inventory):
    if not os.path.exists(FILENAME):
        return
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("Warning: inventory.json is empty or invalid. Starting with empty inventory.")
        return

    for item in data:
        price = float(str(item["Price"]).replace("$", ""))
        inventory.add_product(Product(item["ID"], item["Name"], price, item["Stock"]))


def save_inventory(inventory):
    print("Saving inventory... ")
    data = []
    for product in inventory.get_all_products():
        data.append({
            "ID": product.get_product_id(),
            "Name": product.get_name(),
            "Price": product.get_price(),
            "Stock": product.get_stock()
        })
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)
    print("Inventory saved successfully to inventory.json.")


def exit_program(inventory):
    save_inventory(inventory)
    print("Thank you for using Inventory Management System.\nProgram terminated.")


def show_menu():
    print("""
----------- MENU -----------
1. Display All Products
2. Add Product
3. Update Stock
4. Search Product
5. Save Inventory
6. Exit
----------------------------
""")


main_inventory = Inventory()
load_inventory(main_inventory)

while True:
    show_menu()
    try:
        option = int(input("Enter option (1-6): "))
    except ValueError:
        print("Please enter a number from 1 to 6.")
        continue

    match option:
        case 1:
            main_inventory.display_all()
        case 2:
            try:
                product_id = input("Enter Product ID: ").strip()
                name = input("Enter Name: ").strip()
                price = float(input("Enter Price: "))
                stock = int(input("Enter Stock: "))
            except ValueError:
                print("Invalid price or stock value.")
                continue
            main_inventory.add_product(Product(product_id, name, price, stock))
            print("Product added.")
        case 3:
            product_id = input("Enter Product ID: ").strip()
            product = main_inventory.search_product(product_id)
            if product is None:
                print("Product not found.")
                continue
            try:
                new_quantity = int(input("Enter New Stock Quantity: "))
            except ValueError:
                print("Please enter a whole number.")
                continue
            product.update_stock(new_quantity)
        case 4:
            product_id = input("Enter Product ID: ").strip()
            product = main_inventory.search_product(product_id)
            if product:
                product.display_information()
            else:
                print("Product not found.")
        case 5:
            save_inventory(main_inventory)
        case 6:
            exit_program(main_inventory)
            break
        case _:
            print("Invalid choice, please try again.")