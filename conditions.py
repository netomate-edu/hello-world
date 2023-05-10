"""
General syntax for writing conditional statements in python.

if (condition):
    ...
elif (condition):
    ...
else:
    ...

"""

user_pen_color = 'blue'
user_alt_pen_color = 'black'
available_shop_pen_color = 'red'

if available_shop_pen_color == user_pen_color:
    print(f'{user_pen_color} was purchased')
elif available_shop_pen_color == user_alt_pen_color:
    print(f'{user_alt_pen_color} was purchased')
else:
    print('Come back home')



# username = 'fosajeff'
# password = 'password$513)+'

"""
print('Welcome to Python Social Network. \nCreate your account to continue.\n')

username_input = input('Enter your username: ')
user_password_input = input('Enter your password: ')

print(f'Account created successfully.\nLogin to continue\n')

login_username = input('username: ')
login_password = input('password: ')


if (login_username == username_input):
    if (login_password == user_password_input):
        print("Logged in successfully!!")
    else:
        print("Incorrect credentials, try again.")
else:
    print("Incorrect credentials, try again.")
"""




# Database
user2_username = "ifedayo"
user2_password = "1246xyz#&"

print("Welcome back, please login to continue")

input_username = input("username: ")
input_password = input("password: ")

if(input_username == user2_username):
    if(input_password == user2_password):
        print(f'Welcome back {user2_username}')
    else:
        print("Incorrect credentials")
else:
    print("Incorrect credentials")
