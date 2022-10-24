#Conditional List Comprehension
# new_list = [new_item in item in list if test]
#Conditional Dictionary Comprehension
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
import random
from turtle import clear, st

names = ['Habib', 'Angelo', 'Jose', 'Julian', 'Dave', 'David']

student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)
# passed_students = {classmate:student_scores[classmate] for classmate in student_scores if student_scores[classmate] > 60}
passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)