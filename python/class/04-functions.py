# FUNCTIONS

"""
Function ? => set of instructions
could take arguments
Must return sth even None
"""

# function sayHi() {
#     console.log("Hi")
# }

# def say_hi():
#     print("Hi")
#     return None

# Invoke // Call THE FUNCTION

# say_hi()

# def say_hi(name):
#     print(f"Hi {name}")
#     return None
# say_hi("Alex")

# def multiply(a,b):
#     return a*b
# print(multiply(2,3))

# multiply(1,2,35,3,8,3,)

def multiply(*args):
    print(f"ARGS : {args}")
    result = 1
    for number in args :
        result *=number
    return result
# print(multiply(1,2,35,3,8,3,2,35,3,8,3,2,35,3,8,3,2,35,3,8,3,2,35,3,8,3,2,35,3,8,3))


def say_fullname(**kwargs):
    # print(f"YOUR FULLNAME IS {first_name} {last_name} !")
    # return f"{first_name} {last_name}"
    print(f"KWARGS : {kwargs}")
    print(f"FIRST NAME : {kwargs['first_name']}\nLAST NAME : {kwargs['last_name']}")
    return None

# say_fullname(first_name="BOB", last_name="MARLEY")
# say_fullname("MARLEY", "BOB")

x = [ [5,2,3], [10,8,9] ] 
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

print(students[1]['last_name'])

print(sports_directory['basketball'][2])