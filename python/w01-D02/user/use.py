
class User:		
    def __init__(self):
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.email = "adaLovelace@gmail.com"
        self.age = 42
        
user_ada = User()
print(user_ada.first_name) 

user_lovelace = User()
print(user_lovelace.last_name)

user_lovelace = User()
print(user_lovelace.email)

user_age = User()
print(42)

class Shoe:
    def __init__(self, brand, shoe_type, price):
        self.brand = brand
        self.type = shoe_type
        self.price = price
        self.in_stock = True
    
        
        def on_sale_by_percent(self, percent_off):
                self.price = self.price * (1-percent_off)
                
    def total_with_tax(self, tax_rate):
        tax = self.price * tax_rate
        total = self.price + tax
        return total
    
    def cut_price_by(self, amount):
        if amount < self.price:
                self.price -= amount
        else:
            print("Price deduction too large.")
my_shoe = Shoe("Converse", "Low-tops", 36.00)
print(my_shoe.total_with_tax(0.05))
my_shoe.cut_price_by(10)
print(my_shoe.price)