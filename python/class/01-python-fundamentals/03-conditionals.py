age = 9

if 70>age > 18 :
    print("Welcome to The Club")
elif age > 70 :
    print("You need to rest")
else :
    print("Go Home")

user = {
    'first_name': "Sam",
    'last_name' : "Smith",
    'age': age,
    'is_admin': False,
    'marks': [10,9.8,10],
    'friends':{'one':"Alex",'two':"Max"}
}

if  user['is_admin'] :
    print("YES this is the ADMIN")
else :
    print("This is a simple USER")

#  USING if not we will switch conditions

if not user['is_admin'] :
    print("This is a simple USER")
else :
    print("YES this is the ADMIN")

# print(True+True)
