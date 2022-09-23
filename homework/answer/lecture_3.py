"""
HW for the following topics
    - built-in data types (lists, tuples)
    - control flows
Fill your from next line after # Answer:
"""

###################
# Task 1: Write a program to sum all the items in a list [1,2,3,4,5,4,3,2,1]
# Answer:
ls = [1, 2, 3, 4, 5, 4, 3, 2, 1]
temp_sum = 0
for elem in ls:
    temp_sum += elem
print(temp_sum)

###################
###################
# Task 2: Write a program to multiply all the items in a list [1,2,3,4,5,4,3,2,1]
# Answer:
ls = [1, 2, 3, 4, 5, 4, 3, 2, 1]
temp_prod = 0
for elem in ls:
    temp_sum *= elem
print(temp_sum)

###################
###################
# Task 3: Write a program to get the largest number from a list [1,2,3,4,5,4,3,2,1]
# Answer:
ls = [1, 2, 3, 4, 5, 4, 3, 2, 1]
temp_max = ls[1]
for elem in ls[1:]:
    if elem > temp_max:
        temp_max = elem
print(temp_max)

###################
###################
# Task 4: Write a program to get the index of the smallest number from a list [1,2,3,4,5,4,3,2,1]
# Answer:
ls = [1, 2, 3, 4, 5, 4, 3, 2, 1]
temp_max = ls[1]
for elem in ls[1:]:
    if elem < temp_max:
        temp_max = elem
print(temp_max)
###################
###################
# Task 5: Write a program to find the even numbers from a list [1,2,3,4,5,4,3,2,1]
# Answer:
ls = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print([elem for elem in ls if elem % 2 == 0])

###################
###################
# Task 6: Write a program to remove the odd numbers from a list [1,2,3,4,5,4,3,2,1]
# Answer:
ls = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print([idx for idx, elem in enumerate(ls) if elem % 2 == 1])

###################
###################
# Task 7: Write a program to remove the odd numbers from a list [1,2,3,4,5,4,3,2,1]
# Answer:
ls = [1, 2, 3, 4, 5, 4, 3, 2, 1]
for elem in ls:
    if elem % 2 == 1:
        ls.remove(elem)
print(ls)

###################
###################
# Task 8: Write a program to find if the input word/sentence is a palindrome, example - racecar, level
# Answer:
a_string, b_string, c_string = "racecar", "motobike", "Was it a car or a cat I saw?"
a_string = a_string.lower() \
    .replace("?", "") \
    .replace(".", "") \
    .replace("!", "") \
    .replace(" ", "") \
    .replace(",", "")
b_string = b_string.lower() \
    .replace("?", "") \
    .replace(".", "") \
    .replace("!", "") \
    .replace(" ", "") \
    .replace(",", "")
c_string = c_string.lower() \
    .replace("?", "") \
    .replace(".", "") \
    .replace("!", "") \
    .replace(" ", "") \
    .replace(",", "")

print(a_string == a_string[::-1])
print(a_string == b_string[::-1])
print(c_string == c_string[::-1])

###################
###################
# Task 9: Create a 3X3 identity matrix using tuples
# Answer:
iden_3 = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
###################
###################
# Task 10: Write a program to check if given square matrix is an identity matrix
# Answer:
id_mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
for i in range(3):
    for j in range(3):
        if i == j and id_mat[i][j] != 1:
            print("not an identity matrix")
            break
        elif i != j and id_mat[i][j] != 0:
            print("not an identity matrix")
            break
    else:
        continue
    break
else:
    print("an identity matrix")
###################
###################
# Task 11: Write a program to return a list with square root of the numbers in list
# Answer:
from math import sqrt

ls = [1, 2, 3, 4, 5, 6]

print([sqrt[elem] for elem in ls])
###################
###################
# Task 12: Write a program to return the number of all possible pairs of elements in the list
# Answer:
ls = [1, 2, 3, 4, 5, 6]
ls_len = len(ls)
print(ls_len * (ls_len - 1) / 2)

###################
###################
# Task 13: Write a program to return the number of all possible pairs of elements in the list (return list of tuples)
# Answer:
ls = [1, 2, 3, 4, 5, 6]
print([(elem1, elem2) for idx, elem1 in enumerate(ls) for elem2 in ls[idx + 1:]])
###################
###################
# Task 14: Write a  program to generate all permutations of a list
# Answer:

# we will discuss the task later

###################
###################
# Task 15: Write a program to convert a list of numbers into a sorted list of unique values
# Answer:
ls = [1, 4, 2, 4, 3, 4, 5, 4, 6, 4, 7]

print(sorted(list(set(ls))))
###################
###################
# Task 16: Write a program to concatenate two lists of strings.
# Example: ["a","b","c"], [1,2,3] -> ["a1","b2" ,"c3"]
# if lengths of the lists differ, add "_" as a suffix/prefix
# Answer:
ls1, ls2 = ["a", "b", "c", "d"], [1, 2, 3]
l1, l2 = len(ls1), len(ls2)
if l1 > l2:
    ls2 += ["_"] * (l1 - l2)
elif l1 < l2:
    ls1 += ["_"] * (l2 - l1)
else:
    pass

print(["".join([str(elem1), str(elem2)]) for elem1, elem2 in zip(ls1, ls2)])

###################
