# Program that appends student information using student.py class

from cs50 import get_string
# create our own class Student (similar to struct in C)
from student import Student

students = []

for i in range(3):
    name = get_string("Name: ")
    dorm = get_string("Dorm: ")
    s = Student(name, dorm)
    students.append(s)

for student in students:
    print(f"{student.name} lives in {student.dorm}")