class Product:

    def __init__(self):
        self.product_id = int(input("Enter Product ID: "))
        self.name = input("Enter Product Name: ")
        self.price = float(input("Enter Price: "))
        self.stock_quantity = int(input("Enter Stock Quantity: "))

    def show(self):
        print("Product ID:", self.product_id)
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Stock:", self.stock_quantity)

    def update_stock(self, quantity1, quantity2):
        self.stock_quantity += quantity1
        self.stock_quantity -= quantity2

    def get_product_info(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Stock: {self.stock_quantity}"


class Order:

    def __init__(self, order_id, product, quantity_ordered):
        self.order_id = order_id
        self.product = product
        self.quantity_ordered = quantity_ordered

    def calculate_total(self):
        if self.quantity_ordered > self.product.stock_quantity:
            print(f"Not enough stock for {self.product.name}! Only {self.product.stock_quantity} left.")
            return 0

        self.product.update_stock(0, self.quantity_ordered)
        total = self.quantity_ordered * self.product.price
        return total





print("--- Enter Laptop details ---")
laptop = Product()

print("--- Enter Headphones details ---")
headphones = Product()

print("--- Enter Mouse details ---")
mouse = Product()


order1 = Order(101, laptop, 2)
order2 = Order(102, headphones, 3)

print("\n--- Order Totals ---")
print("Order 1 total:", order1.calculate_total())
print("Order 2 total:", order2.calculate_total())


print("\n--- Updated Product Info ---")
print(laptop.get_product_info())
print(headphones.get_product_info())
print(mouse.get_product_info())