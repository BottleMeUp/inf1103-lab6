class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity):
        print("Update Stock")
        if quantity < 0:
            print("Stock cannot be negative.")
            return
    
        self.__stock = quantity
        print(f"\nNew Stock Quantity: {self.__stock}")
        print("\nStock updated successfully! ")

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: {self.__price} | Stock: {self.__stock}")

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price
    
    def get_stock(self):
        return self.__stock






    

            







    