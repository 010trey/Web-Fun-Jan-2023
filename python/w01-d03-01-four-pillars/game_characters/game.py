class Character :
        def __init__(self, name):
            self.name = name
            self.health = 50
            self.power = 50
            self.defense  = 30
            self.weapon = None

        def attack(self, target):

            print(f"[ATTACK] {self.name} attacked {target.name}.")
            damage = target.defend(self.power) #! Abstraction
            print(f"AND cause Damage equal {damage}")
            target.health -= damage
            return self

        def defend(self, damage):
            print(f"[DEFEND] {self.name} defended {damage} AND  reduce it by {self.defense}.")
            damage -= self.defense
            return damage



class Barbarian(Character): #! Inheritance
        def __init__(self, name):
            super().__init__(name)
            self.power+=30 #! Polymorphism change parent attribute
            self.health+=20  #! Polymorphism change parent attribute
            self.rage = 30  #! Polymorphism add new attribute


class Elf(Character):
        def __init__(self, name):
            super().__init__(name)

        # ! Polymorphism 
        def magic_attack(self, target):
            target.health -= self.power
            target.power -= 20
            target.defense -= 20


class Seer:
        def __init__(self) :
            self.hidden_type = Barbarian("SEER") #! Abstraction
            self.see_range = 100


    # class Seer (Barbarian):
    #     def __init__(self, name) :
    #         super().__init__(name)
    #         # self.hidden_type = Barbarian("SEER") #! Abstraction


john = Character("JOHN")
conan = Barbarian("CONAN")
elon = Seer()
elon.hidden_type.attack(john)
print("CONAN Health : ",conan.health)
conan.attack(john)

jane = Character("JANE") 
    