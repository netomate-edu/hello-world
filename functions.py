"""
A piece of code that does a single task and can be reused.

def name_of_function(optional_arguments):
    ....

- Parameter (variables that the function expect when you define it.)
- Argument (variables you pass to the function when invoking it.)

When you invoke a function, it is going to be called.
How to call --> name_of_function(optional_arguments)

A function should always have a return value.
"""

def say_hello():
    print('Hello from a function')

say_hello() # function invocation

def sum_two_numbers(a, b):
    sum = a + b
    return sum


# print('Hello, I can add any two numbers of your choice...')

# first_number = float(input('Enter first number: '))
# second_number = float(input('Enter second number: '))

# result = sum_two_numbers(first_number, second_number)

# print(f'Your total = {result}')

def capitalize_name(name):
    return name.upper()

print('Welcome to your student portal\n')
print('Enter your bio data\n')

first_name = capitalize_name(input('Your first name (First letter in uppercase): '))
last_name = capitalize_name(input('Your last name (First letter in uppercase): '))

print(f'Welcome {first_name} {last_name}')

