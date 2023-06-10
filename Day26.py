# List Compression
# numbers = [1, 2, 3]
# new_numbers = [item+1 for item in numbers]
# print(new_numbers)
#
# double = [n*2 for n in range(1, 5)]
# print(double)

# Conditional List Comprehension
# new_list = [new_item for item in list if test]
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)

# Exercise
# numbers = [1, 2, 3, 4, 5, 6]
# squared = [num * num for num in numbers]
# print(squared)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = [n for n in numbers if n % 2 == 0]
# print(even)

# with open("file1.txt") as file1:
#     file_1_data = file1.readlines()
# with open("file2.txt") as file2:
#     file_2_data = file2.readlines()
#
# result = [int(num) for num in file_1_data if num in file_2_data]
#
# print(result)

# Dictionary Comprehension
# Syntax
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#
# scores = {student: random.randint(1, 100) for student in names}
#
# passed_scores = {student: score for (student, score) in scores.items() if score >= 60}
#
# print(passed_scores)

# Exercise

# sentence = "What is the Airspeed velocity of an Unladen Swallow"
# list_sentence = sentence.split()
# dict_sentence = {word: len(word) for word in list_sentence}
# print(dict_sentence)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {Days: value*1.8+32 for (Days, value) in weather_c.items()}
# print(weather_f)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
# Simple looping through dictionaries
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

# using panda
import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# loop through rows of a dataframe
# for (index, row) in student_data_frame.iterrows():
#     print(row.student)
#     print(row.score)
#     if row.student == "Angela":
#         print(row.score)

