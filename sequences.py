"""
Sequences in python:
1. String
2. List
3. Tuple
4. Dictionary
5. Set
"""

# 1. String
# Order: Yes, Mutable: No

name = 'ifedayo'
len(name) # 7 --> 0 - 6
# print(name[3]) # d

# 2. List
# Order: Yes, Mutable: Yes

shopping_items = ['indomie', 'milk', 'bread', 'egg', 'yoghurt', 
                  'rice', 'bean', 'pasta', 'wheat powder']

# first_name, last_name, age, grade, is_grad_student
student_biodata = [
    'Jamie',
    'Brown',
    20,
    'grade_2',
    False
]

print(shopping_items[7])
# print(student_biodata)
sorted_shopping_items = sorted(shopping_items)

shopping_items[0] = 'sardine'
shopping_items.append('butter')
shopping_items.append('jam')

print(shopping_items)


# 3. Tuple
# Order: Yes, Mutable: No

# PI, gravity, unit constant
mathematical_constants = (3.142, 9.8, 1)
mathematical_constants[0]
# mathematical_constants[2] = 5 # not mutable

print(mathematical_constants)

# 4. Dictionary
# Ordered: No, Mutable: Yes

# { 'key': value }
# first_name, last_name, age, grade, is_grad_student

student_bio_data = {
    'first_name': 'Naomi',
    'last_name': 'Idi',
    'age': 14,
    'grade': 5,
    'is_grad_student': False
}

print(student_bio_data['age'])
print(student_bio_data['grade'])

student_bio_data['age'] = 15

print(student_bio_data)


# 5. Set
# Ordered: No, Mutable: N/A
# can only store value once

set_of_integers = {1, 2, 3, 4, 5, 2, 2, 5}

print(set_of_integers)


# Loops
print('***Loops in python ***')

"""
There are two loops in python:
1. For loop
2. While loop
"""

# 1. For loop
for i in [0,1,2,3,4,5]:
    print(i)


friends = ['mike', 'josh', 'katie', 'pat']

for name in friends:
    if name == 'josh':
        print('skipping one friend')
        continue
    print(f'Hi, {name}')

# 2. While loop
"""
while (condition):
    ...
"""

counter = 0
while (counter < 5):
    counter += 1

    if (counter == 6):
        print('Breaking out of loop')
        break

    if (counter == 3):
        print('Skipping current iteration')
        continue

    print(f'Counter = {counter}')

print(f'Loop ran for {counter} times')
print('Done with while loop')
