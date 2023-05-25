
class User:		
    def __init__(self):
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.email = "adaLovelace@gmail.com"
        self.age = 42
# Now that you have a class set up with a constructor 
# You can assign new variables to new users in the outer scope!
user_ada = User()
print(user_ada.first_name) # prints Ada

user_lovelace = User()
print(user_lovelace.last_name)

user_lovelace = User()
print(user_lovelace.email)

user_age = User()
print(42)


# # declare a class and give it name Shoe
# class Shoe:		
#     def __init__(self):
#         self.brand = "Vans"
#         self.type = "Classic Sk8-Hi"
#         self.price = 69.99
#         self.in_stock = True 


# skater_shoe = Shoe()
# dress_shoe = Shoe()
# # Accessing the instance's attributes
# print(skater_shoe.type) # Classic Sk8-Hi
# print(dress_shoe.type)	# Classic Sk8-Hi



# skater_shoe.type = "Low-top Trainers"
# print(skater_shoe.type)
# # output: Low-top Trainers
# dress_shoe.type = "Ballet Flats"
# print(dress_shoe.type)
# # output: Ballet Flats



# class Shoe:
#     # now our method has 4 parameters (including self)!
#     def __init__(self, brand, shoe_type, price):
#     # we assign them accordingly
#         self.brand = brand
#         self.type = shoe_type
#         self.price = price
#     # the status is set to True by default
#         self.in_stock = True
# skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
# dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
# print(skater_shoe.type)	# output: Low-top Trainers
# print(dress_shoe.type)	# output: Ballet Flats


# adrien = User("Adrien", "adion@codingdojo.com")
# cool_person = User("Sadie", "sflick@codingdojo.com")
    
# adrien.greeting()
# # prints Hello, my name is Adrien
    
# cool_person.greeting()
# # prints Hello, my name is Sadie

# class Shoe:
#     # now our method has 4 parameters (including self)!
#     def __init__(self, brand, shoe_type, price):
#     # we assign them accordingly
#         self.brand = brand
#         self.type = shoe_type
#         self.price = price
#         # the status is set to True by default
#         self.in_stock = True
    
# # Create two shoe instances
# skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
# dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
        
# # The skater shoes go on sale by 20% reduced price:
# skater_shoe.price = skater_shoe.price * (1 - 0.2)
        
# # The dress shoes go on sale by 10% reduction:
# dress_shoe.price = dress_shoe.price * (1 - 0.1)
        
# # The skater shoes go on sale AGAIN by another 10%:
# skater_shoe.price = skater_shoe.price * (1 - 0.1)

class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
    # we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        # the status is set to True by default
        self.in_stock = True
    
    
        Takes a float/percent as an argument and reduces the
            price of the item by that percentage.
        def on_sale_by_percent(self, percent_off):
              self.price = self.price * (1-percent_off)

#Returns a total with tax added to the price.
    def total_with_tax(self, tax_rate):
        tax = self.price * tax_rate
        total = self.price + tax
        return total
    
    # Reduces the price by a fixed dollar amount.
    def cut_price_by(self, amount):
        if amount < self.price:
                self.price -= amount
        else:
            print("Price deduction too large.")

# Create some shoes. Call some methods on those shoes. Print your shoe's attributes..
my_shoe = Shoe("Converse", "Low-tops", 36.00)
print(my_shoe.total_with_tax(0.05))
my_shoe.cut_price_by(10)
print(my_shoe.price)