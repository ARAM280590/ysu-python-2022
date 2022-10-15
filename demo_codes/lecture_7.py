"""
This module is a demo code for lecture 7

At this lecture we cover
    - files, types, extensions
    - I/O in python
    - exceptions : catching/handling and raising, creating

Materials

"""
# files - text and binary
# text files: .txt, .csv, .json
# structured, semi-structured, unstructured

# open - working with .txt files
# print(open) # https://docs.python.org/3/library/functions.html#open
#
# zen = open("../data/zen_of_python.txt", mode='r')
# print(zen)
#
# print(zen.__dir__())
#
# for elem in zen:
#     print(elem)
#
# zen_read = zen.read()
# print(zen_read)

# with open("../data/zen_of_python.txt", mode='r') as file:
#     for line in file.readlines():
#         print(line)
#
#
# with open("../data/zen_of_python.txt", mode='r') as file_read, open("../data/zen_of_python_EDIT.txt", mode='w') as file_write:
#     for line_number, line in enumerate(file_read):
#         file_write.write(f"Line Number:{line_number}, Number of words: {len(line.split())}\n")

# csv
import csv # https://docs.python.org/3/library/csv.html

# writing a csv file
# with open("../data/zen_of_python.txt", mode='r') as file_read, open("../data/zen_of_python_EDIT.csv", mode='w', newline='') as file_write:
#     writer = csv.writer(file_write, delimiter=',')
#     writer.writerow(['line_number', 'wordcount'])
#     for line_number, line in enumerate(file_read):
#         writer.writerow([line_number,len(line.split())])
#
# # reading a csv file
# with open("../data/zen_of_python_EDIT.csv", mode='r', newline='') as file_read:
#     reader = csv.reader(file_read, delimiter=",")
#     reader.__next__()
#     for row in reader:
#         print(row)

# json

# count_ls = []
# with open("../data/zen_of_python.txt", mode='r') as file_read:
#     for line_number, line in enumerate(file_read):
#         count_ls.append({
#             'line_number': line_number,
#             'wordcount': len(line.split())
#         })
# print(count_ls)
#
#
# import json #
# json_string = json.dumps(count_ls) # wrtites to a string object
# print(json_string)
# print(type(json_string))
#
# with open("../data/zen_of_python_EDIT.json", mode='w') as file_write:
#     json.dump(count_ls, file_write) # writes to a file
#
# with open("../data/zen_of_python_EDIT.json", mode="r") as read_file:
#     data = json.load(read_file)
#
# print(type(data))

# next lectures: parsing files, using packages for easier data manipulation

# binary files
# with open("../data/img_ex.jpg", mode='rb') as file_read:
#     file = file_read.read()
#     print(file)

# serialization/deserialization

### Exception handling

import math
# print(math.sqrt(-5))

# try:
#     a = math.sqrt(-5)
# except:
#     print("Invalid operation")
# print('continue program')

# print(math.sqrt('a'))

# number = 'a'
# try:
#     a = math.sqrt(number)
# except ValueError as e:
#     print(f"Invalid value: {e}")
# except TypeError as e:
#     print(f"Invalid type: {e}")
# print('continue program')

# while True:
#     try:
#         x = int(input("Please enter a positive number: "))
#         print(x)
#         if x <= 0:
#             raise Exception
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
#     else:
#         print(f"Square root of your number is {sqrt(x)}")
#         break
#     finally:
#         print("We successfully handled an exception")