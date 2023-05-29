class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price * (percent_change / 100)
        else:
            self.price -= self.price * (percent_change / 100)
    
    def print_info(self):
        print("Product Name:", self.name)
        print("Category:", self.category)
        print("Price:", self.price)


class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
    
    def add_product(self, new_product):
        self.products.append(new_product)
    
    def sell_product(self, id):
        if id < len(self.products):
            product = self.products.pop(id)
            product.print_info()
        else:
            print("Invalid product ID")
    
    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
    
    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)


# Example usage
store = Store("My Store")

product1 = Product("Laptop", 1000, "Electronics")
product2 = Product("Shirt", 20, "Clothing")
product3 = Product("Book", 15, "Books")

store.add_product(product1)
store.add_product(product2)
store.add_product(product3)

store.sell_product(1)
store.inflation(10)
store.set_clearance("Clothing", 20)
