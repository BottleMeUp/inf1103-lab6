import json
import os
FILENAME = "inventory.json"

inventory = [
    {"ID": "P001", "Name": "Laptop", "Price": "$1200.00", "Stock": 15},
    {"ID": "P002", "Name": "Mouse", "Price": "$25.50", "Stock": 40},
    {"ID": "P003", "Name": "Keyboard", "Price": "$45.50", "Stock": 25}
]

def add_product():
    print("Add New Product")
    product_id = input("Enter Product ID: ").strip()
    product_name = input("Enter Product Name: ").strip()
    price = input("Enter Price: ").strip()
    stock_qty = int(input("Enter Stock Quantity: "))

    new_item = {
        "ID": product_id,
        "Name": product_name,
        "Price": price,
        "Stock": stock_qty
    }

    inventory.append(new_item)
    print("Product added successfully!")

    return

def display_all():
    print("Current Inventory\n")
    print("------------------------------------------------ ")
    for item in inventory:
        print(f"ID: {item['ID']} | Name: {item['Name']} | Price: {item['Price']} | Stock: {item['Stock']}")
    print("------------------------------------------------ ")

             
def load_inventory():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Warning: inventory.json is empty or invalid. Starting with empty inventory.")
        return []


def save_inventory():
    print("Saving inventory... ")
    with open(FILENAME, "w") as f:
        json.dump(inventory, f)
    print("Inventory saved successfully to inventory.json.")

def update_product():
    print("Update Stock")
    product_id = input("Enter Product ID: ").strip()
    new_quantity = int(input("Enter New Stock Quantity: "))

    for item in inventory:
        if item["ID"].upper() == product_id.upper():
            print("\nProduct Found:")
            print(f"Name: {item["Name"]}")
            print(f"Current Stock: {item["Stock"]}")
            print("")

            item["Stock"] = new_quantity
            print(f"\nNew Stock Quantity: {new_quantity}")
            print("\nStock updated successfully! ")
            return
        else:
            print("Product Not Found")


def search_product():
    print("Search Product")
    product_id = input("Enter Product ID: ").strip()

    for item in inventory:
        if item["ID"].upper() == product_id.upper():
            print(f"""
Product Found 
------------------------------------------------ 
ID: {item["ID"]} 
Name: {item["Name"]}
Price: {item["Price"]}
Stock: {item["Stock"]} 
------------------------------------------------
            """)
            return
        else:
            print("Product not found.")

def exit():
    save_inventory()
    print("""Thank you for using Inventory Management System. 
             Program terminated.""")




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

inventory = load_inventory()

while True:
    try:
        options = int(input("Enter option (1-6): "))
    except ValueError:
        print("Please enter a number from 1 to 6.")
        continue

    match options:
        case 1:
            display_all()
        case 2:
            add_product()
        case 3:
            update_product()
        case 4:
            search_product()
        case 5:
            save_inventory()
        case 6: 
            exit()
            break
        case _:
            print("Invalid choice, please try again.")

    

            







    