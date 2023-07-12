
"""
In JavaScript
for (var i=0;i<10;i++) {
    console.log(i)
}
"""
# In PYTHON
""" range = function that returns a sequence of numbers 
    start : inclusive has a default value of 0
    stop : exclusive and required 
    step  : not required and default 1 can be + or -
    example : 
        range(0,10) => (0,1,2,3,4,5,6,7,8,9)
"""
# for i in range(0,10):
#     print(i)

# for i in range(0,10,2):
#     print(i)
#     # for j in range(0,i):
#     #     print(j)

# for i in range(10,0,-2):
#     print(i)
#     # for j in range(0,i):
#     #     print(j)
# for i in range(10):
#     print(i)

superheros = ["superman", "batman", "sipderman", "antman", "jedi"]
# for i in range(0, len(superheros)):
#     print(superheros[i])

# for hero in superheros:
#     print(hero)
# my_list = [1,2,3,"45",5, ["yes","no", None]]

# for element in my_list:
#     print(element)

user = {
    'first_name': "John",
    'last_name' : "Smith",
    'age': 41,
    'is_admin': False,
    'marks': [10,9.8,10],
    'friends':{'one':"Alex",'two':"Max"}
}

# for key,value in user.items():
#     print(f"KEY : {key} --- VALUE : {value}")
# for key in user.keys():
#     print(f"KEY {key} *** {user[key]}")
# print(user.items())
# for value in user.values():
#     print(value)

x = 5 
while x>0:
    print(x)
    x-=1
