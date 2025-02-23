

#DICTIONARY COMPREHENSION
print("new_dict = {new_key:new_value for item in list}")
#CONDITIONAL DICTIONARY COMPREHENSION
print("new_dict = {new_key:new_value for (key, value) in dict.items() if test}")
import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
students_scores = {student:random.randint(1, 100) for student in names} #assigns random scores to students.
print(students_scores)

passed_students = {key:value for (key, value) in students_scores.items() if value >= 60} #MAKE SURE TO INCLUDE .ITEMS()
print(passed_students)

# EXERCISE 1
#sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {item:len(item) for item in sentence.split()}
#EXERCISE 2
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# weather_f = {key:value * 9/5 + 32 for (key, value) in weather_c.items()}

# print(weather_f)