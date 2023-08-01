
class Student:
    # Class Attribute 
    school = "MIT"
    # list to store all the students that belong to Student Class
    all_students = []
    # ! CONSTRUCTOR 
    def __init__(self,first_name, last_name, age, marks, fav_number) :
        # iNSTANCE Attributes ---- Values
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.marks = marks
        self.fav_number =fav_number
        Student.all_students.append(self)
        self.car = None

    # !Methods 
    def increase_age(self,amount):
        # print("This is self : ", self,self.first_name, self.age)
        print("BEFORE :", self.age)
        self.age+=amount
        print("AFTER : ", self.age)
        return None
    
    def change_name(self, new_name):
        self.first_name = new_name
        return None
    
    def __repr__(self) :
        return f"STUDENT FIRST NAME : {self.first_name}\nLAST NAME : {self.last_name}"
    
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school
        return None 
    
    @staticmethod
    def validate(dict_data):
        is_valid = True
        if len(dict_data['first_name']) <2:
            is_valid = False
            print("Wrong First Name")
        if len(dict_data['last_name']) <2:
            is_valid = False
            print("Wrong Last Name")

        if dict_data['age'] <17:
            is_valid = False
            print("You are too young")
        return is_valid
class Car:
    # Constructor
    def __init__(self,data_dict) :
        self.make = data_dict['make']
        self.model = data_dict['model']
        self.year = data_dict['year']
        self.color = data_dict['color']
        self.miles = data_dict['miles']

    def drive(self):
        self.miles+=10
        print(f"Your car new millage {self.miles}")
        return self

    def beep(self):
        print("Beeep !!!!")
        return self

honda_data = {
    'make':"Honda",
    'model': "M1",
    'year':2020,
    "color":"RED",
    'miles':100
}
honda  = Car(honda_data)
# golf  = Car("WV", "GOLF 7",2020,"Gray", 100)
# honda.drive().beep().drive().beep().drive().drive()


# print(honda.miles)
# print(golf.miles)

john = Student("John", "Mayer", 40, [12,35,35],23)
alex = Student("Alex", "Max",35, [12,35,35],23)
# sarah = Student("Sarah", "Jones", 22, [12,35,35],23)
# sam = Student("Sam", "Smith", 22, [12,35,35],23)

john.car = honda
john.car.drive().drive().beep().drive()
# fake = Student("", "", 0, [],0)

# print(john.school)
# print(alex.school)
# print(sarah.school)
# print(Student.school)
# print(Student.all_students)

# for student in Student.all_students:
#     print(student.car)
    # print(student.increase_age(2))
    # print("-----------------")

# john.change_name("Jane")
# for student in Student.all_students:
#     print(student.school)
# Student.change_school("New School")
# print(john)
# for student in Student.all_students:
#     print(student.school)
# fake_data = {'first_name': "Steve", 'last_name':"Jones", 'age': 25,'marks': [], 'fav_number':0}
# print(Student.validate(fake_data))

# ! METHODS :
# - Instance Methods
# Instance methods parameter self 
# have access to instance attributes can change them 
# NOTE have no decorator

# -CLASS Methods
# parameter cls
# have access to class attributes can change

# - Static Methods
#  Has no access to any Attribute
# Validations & Utility
