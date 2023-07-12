# import
from character import Character
class Barbarian(Character): #! Inheritance
    def __init__(self, name):
        super().__init__(name)
        self.power+=30 #! Polymorphism change parent attribute
        self.health+=20  #! Polymorphism change parent attribute
        self.rage = 30  #! Polymorphism add new attribute