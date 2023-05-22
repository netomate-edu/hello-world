"""
OOP stands for Object Oriented Programming

1. Classes and Objects
2. Attributes & Behaviour

Attributes: the data e.g of the students (biodata)
Behaviour: what they can do (submit assignments, etc)

Student:
biodata: first_name, last_name, age, gender, is_first_class (Attributes)
activity: submit_assignment, take_class_quiz, sign_attendance, register_courses (Behaviour)
"""


# student1_first_name = 'Adebayo'
# student1_last_name = 'Tunde'
# student1_age = 20
# student1_gender = 'male'
# student1_is_first_class = True

# student1_first_name = 'Bisi'
# student1_last_name = 'Oluwadara'
# student1_age = 21
# student1_gender = 'female'
# student1_is_first_class = False

class Student:
    def __init__(self, first_name, last_name, age, gender, is_first_class):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.is_first_class = is_first_class

    
    def submit_assignment(self):
        return f'Assignment submitted by {self.first_name}'

    
    def take_class_quiz(self):
        return f'Class quiz taken by {self.first_name}'

    
    def sign_attendance(self):
        return f'Attendance signed by {self.first_name}'

    
    def register_courses(self):
        return f'Courses registered for {self.first_name} {self.last_name}'


# instantiating the class
# creating an instance of the class (an actual implementation)
# creating an object of the class

student1 = Student('Adebayo', 'Tunde', 20, 'male', True)
student2 = Student('Bisi', 'Oluwadare', 21, 'female', False)

print(f'Student 1 full name {student1.first_name} {student1.last_name}')
print('Student 2 age', student2.age)

print(student1.register_courses())
print(student2.sign_attendance())





class Robot:
    def __init__(self, name):
        self.name = name

    
    def say_hi(self):
        return f'Hi there, my name is {self.name}.'

    
    def move(self, x_dist, y_dist):
        return f'{self.name} moved {x_dist}m in the x direction and {y_dist}m in the y direction'

    
    def grab(self, x_dist, y_dist):
        return f'{self.name} grabbed an item {x_dist}m in the x direction and {y_dist}m in the y direction'
    


robot1 = Robot('Alex')

print(robot1.say_hi())
print(robot1.move(3, 4))
print(robot1.grab(10, -2))