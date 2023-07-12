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

def add(a,b):
    return a+b