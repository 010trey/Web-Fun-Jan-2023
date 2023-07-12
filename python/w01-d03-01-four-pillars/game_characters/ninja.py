
class Ninja:
    # Class Attributes
    dojo = "Tokyo"
    all_ninjas = []
    # !Constructor
    def __init__(self, name, age):
        # *- Attributes---Values
        self.name = name
        self.age = age
        # -Attributes with Default Values
        self.health = 50
        self.power = 10
        Ninja.all_ninjas.append(self)


    # !Methods
    def attack(self, target):
        target.health-= self.power
        print(f"[ATTACK] {self.name} attacked {target.name} AND cause Damage equal {self.power}.")
        return self

    def heal(self):
        self.health += 20
        return self

    @classmethod
    def boot_camp(cls):
        for ninja in  cls.all_ninjas :
            ninja.health +=20
            ninja.power +=10
        return None

    # Validation & Utility
    @staticmethod
    def validate_ninja(dict):
        is_valid = True
        if len(dict['name'])<2:
            is_valid =False
        if dict['age']<17:
            is_valid = False
        return is_valid

# Create an Instance (Object) of the Class Ninja
john = Ninja("John",41)
alex = Ninja("Alex",23)
print("Before : ",alex.health)
john.attack(alex)
Ninja.boot_camp()
alex.heal().heal().attack(john)
print("After : ", alex.health)
# print(john.name, john)