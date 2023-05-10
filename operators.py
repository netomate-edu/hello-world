"""
Operators in python include:
1. Arithmetic ops
2. Assignment ops
3. Comparison ops
4. Logical ops
5. Membership ops
"""


# 1. Arithmetic operators

a = 5
b = 6
c = a

print(10 / 5) #divide
print(2 * 4) #multiply
print(1 + 59) #addition
print(59 - 19) #subtraction
print(10 % 3) #modulus
print(2 ** 4) #raise-to-power
print(17 / 4) #floor-delete

# 2. Assignment operators
a = 5
a += 4
# a = a + 4

print(a) # 9


# 3. Comparison operators

"""
''  ->  False
0   ->  False

' '      ->  True
1,2,3... ->  True
"""

print(1 == 2) # Is Equal To --> False
print(1 == 1) # Is Equal To  --> True
print('1' == 1) # Is Equal To --> False
print('1' == '1') # Is Equal To --> True

a = 1
b = 3
print(a != b) # Not Equal To --> True

print(b > a) # Greater than --> True
print(a < b) # Less than --> True

c = 3
print(c >= b) # Greater Than or Equal To --> True
print(a <= c) # Less Than or Equal To --> True


# Logical Operator
"""
1. Logical AND
2. Logical OR
3. Logical NOT

True and True   --> True
False and True  --> False
True and False  --> False
False and False --> False

True or True    --> True
False or True   --> True
True or False   --> True
False or False  --> False
"""

a = 2
b = 7
c = 3
d = 2
print(a == b and c == d)
print(c == b or d == a)

print(c == b or not d == a) # False

