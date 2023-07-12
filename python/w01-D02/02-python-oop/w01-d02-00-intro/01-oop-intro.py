    # OOP 
    # ? OOP  : Object Oriented Programming
    # - sTUDENT MUST HAVE first_name last_name age marks fav_number
    # ? Class it's blueprint = template = factory to create objects (students , cars , products, employees...)
    # ? Object instance of the class 
    # attributes  & methods
    # Attributes  : what the object (student) can have characteristics (nouns)
    # Methods  : what the object (student) can do (functions inside the class) actions (verbs)

    # D.R.Y  = Don't Repeat Yourself 
    # Model Real Life 
    student_1 = ["John", "Mayer", 40, [9.8,10,10], 25] # List
    student_1 = {
        'first_name': "John", 'last_name': "Mayer",
        'age': 40,'marks': [9.8,10,10], 'fav_number': 25
        } # dict
    student_1 = {
        'first_name': "Alex", 'last_name': "Max",
        'age': 41,'marks': [9.8,9.0,10], 'fav_number': 7
        } # dict
    student_1 = {
        'first_nme': "John", 'last_name': "Mayer",
        'age': 40,'marks': [9.8,10,10], 'favnumber': 25
        } # dict

    # PascalCase
    # snake_case
    # camelCase

    class Student:
        # ! CONSTRUCTOR 
        def __init__(self,first_name, last_name, age, marks, fav_number) :
            # Attributes ---- Values
            self.first_name = first_name
            self.last_name = last_name
            self.age = age
            self.marks = marks
            self.fav_number =fav_number

        # !Methods 
        def increase_age(self,amount):
            # print("This is self : ", self,self.first_name, self.age)
            print("BEFORE :", self.age)
            self.age+=amount
            print("AFTER : ", self.age)
            return None


    john = Student("John", "Mayer", 40, [12,35,35],23) # __init__("John", "Mayer", 40, [12,35,35],23)
    alex = Student("Alex", "Max",35, [12,35,35],23)
    sarah = Student("Sarah", "Jones", 22, [12,35,35],23)
    # print("*******",john,"***********")
    # print("*******",alex,"***********")
    # print("*******",sarah,"***********")
    # student_1.
    # john.
    # print(f"FN: {john.first_name}\nLN : {john.last_name}\nAGE: {john.age}")
    # alex = Student()
    john.increase_age(20)
    alex.increase_age(10)
    sarah.increase_age(23) 
    
    
    
    