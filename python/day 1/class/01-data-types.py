
# This is a comment this line will not be interpreted
# ctrl + /

"""
This is
Multi line comment 
will not be interpreted
DOCSTRING
"""

# How to declare variables
# JavaScript var variableName = value

# python is snake we are going to use snake_case_naming_convention

variable_name = "value"

GLOBAL_VARIABLE = "python"
PORT = 5000
APP_NAME = "WEB_APP"

# - DATA TYPES      

# * PRIMITIVES

# String
first_str = "hello world , nice to have you here"
name = "John"
# Numbers
    # Integers
age = 41
    # Floats
bmi = 2.75

# Boolean
voted = True
is_admin = False

# NoneType
permit = None

# print(name, age, bmi, is_admin)
# Formatted String
# print(f"User name : {name} his age {age} years and his BMI equal to {bmi}")
# print(f"USER : {name} \nBMI : {bmi}")
# print("FORMAT ** User name : {} his age {} years and his BMI equal to {}".format(name,age,bmi))
# console.log(`User name : ${name} his age ${age} years and his BMI equal to ${bmi}`)

# print(f"None : {type(permit)}\nNAME : {type(name)}\nAGE : {type(age)}\nBMI : {type(bmi)}\nADMIN : {type(is_admin)}")

str_age = str(age)
float_age = float(age)
# print(f"AGE : {type(age)}\nSTR_AGE : {type(str_age)} \nFLOAT_AGE{type(float_age)} {float_age}")
# print(len(name), name.upper(), first_str.split(',') )

# * COMPLEX
# LISTS
# Array in JavaScript == List  in python
# INDEX   0                                                     len(list)-1
my_list = [1,2,3,"45",5, name, age, is_admin,bmi, ["yes","no", None]]
#                                                             -1

# print(len(my_list))
# print(my_list[-1])
# print(my_list[-2])
# print(my_list[2:7])
# print(my_list)
my_list.append(first_str)
# print(my_list)
# DELETE last item from the list
# my_list.pop()
my_list.pop(-2)
numbers = [2,0,22,5,-11,100]
numbers.sort(reverse=True)
# print(numbers)

# Objects in JavaScript   =  Dictionaries in python
# key-value pairs
user = {
    'first_name': name,
    'last_name' : "Smith",
    'age': age,
    'is_admin': False,
    'marks': [10,9.8,10],
    'friends':{'one':"Alex",'two':"Max"}
}
# bracket notation
print(user["first_name"])
# .get
# print(user)
user["is_admin"] = True
# print(user)

# Tuples
# similar to lists but immutable  : can not be changed
my_tuple = (1,2,3)
# my_tuple[3] = 7

#SET
list_2 = [1,2,2,3,4,5,5 ,"john", "john"]
my_set = set(list_2) 
# unique elements
print(my_set)
