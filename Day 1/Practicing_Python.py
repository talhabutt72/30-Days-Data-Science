# Q1. FizzBuzz
# Print numbers from 1 to 100.
# For multiples of 3, print "Fizz",
# For multiples of 5, print "Buzz",
# For multiples of both, print "FizzBuzz".

# Code

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0 and i % 5 != 0:
#         print("Fizz")
#     elif i % 3 != 0 and i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# Q2. Prime Numbers in a Range
# Write a function to return all prime numbers between 10 and 50.


# def findPrime():
    
#     for i in range(10, 51):
#         for j in range(1, i - 1):
#             if i % j == 0:
#                 print(i)


# findPrime()

# Q3.
# *
# **
# ***
# ****
# *****

# for i in range(1, 6):
#     print("*" * i)


# Q4.
# List Compression
# Given a list of numbers, return a new list with only even numbers, squared.


# l1 = [5, 6, 78, 9, 10]

# squr = []

# for i in l1:
#     if i % 2 == 0:
#         squr.append(i**2)

# print(squr)
        

# Q5 .        
# Frequency Counter
# Count the frequency of each word in this sentence:
# "data science is fun and data is powerful"
# → Output: {'data': 2, 'science': 1, 'is': 2, 'fun': 1, 'and': 1, 'powerful': 1}

# string = "data science is fun and data is powerful"
# split = string.split(" ")

# output = {}

# for i in split:
#     if i in output:
#         output[i] += 1
#     else:
#         output[i] = 1

# print(output)


# Q6 .
# Custom Sum Function
# Write a function that takes a list and returns the sum of numbers, but skips non-integers.


# def IDK(l1):
#     l = []
    
#     for i in l1:
#         string  = str(i)
#         if string.isnumeric():
#             integer = int(string)
#             l.append(integer)
        
    
#     total  = sum(l)
#     print(total)


# IDK([1, 5, 8, 'u', 935.5])

# Q7 .
# Safe Division
# Write a function that divides two numbers and:
# Returns the result if valid
# Returns "Cannot divide by zero" if denominator is zero
# Returns "Invalid input" if inputs are not numbers


# def SafeDivision(p, q):
    
#     if p.isdigit() and q.isdigit() and q == 0:
#         return "Cannot divide by zero"
    
#     elif p.isdigit() and q.isdigit() and q != 0:
        
#         return int(p) / int(q)
    

#     else:
#         return "Invalid input"
    
# p = input("Enter p: ")
# q = input("Enter q: ")

# print(SafeDivision(p, q))

# Tuple Unpacking
# Given a list of tuples with (name, age), return only names where age > 25.

# k = [("Talha", 5)]
# people = [("Alice", 22), ("Bob", 30), ("Charlie", 28)]
# people = ("Talha", 5)

# # print(k)
# # print(type(k))

# for i in people:
#     # if age > 25:
#     #     print(name)
#     print(i)



# 1. Write a program to print the even numbers from a list.

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# for i in nums:
#     if i % 2 == 0:
#         print(i)


        
# 2. Given a list of strings, print only the strings that have more than 4 characters.


# words = ["data", "science", "AI", "ML", "Python"]

# for word in words:
#     if len(word) > 4:
#         print(word)
        

# 3. Create a new list that contains the square of each number in an existing list using a for loop.

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# squared_list  = []

# for no in nums:
#     squared_list.append(no**2)
#     # print(squared_list)
    
# print(f"The Orignal List {nums}")
# print(f"The Squared List {squared_list}")

# 4. Write a function that takes a number and returns whether it's prime.

# 5. Write a function that accepts a list and returns the sum of all even numbers in it.

# def Even_sum(l1):
    
#     sum = 0
#     for i in l1:
#         if i % 2 == 0:
#             sum += i
    
#     print(sum)
    

# Even_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    
    
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

dict1 = {}

# for item in items:
#     if item in dict1:
#         dict1[item] += 1
#     else:
#         dict1[item] = 1
    
# print(dict1)

# 8. Given a dictionary of students and their marks, print the names of students who scored more than 75.

# scores = {'Alice': 82, 'Bob': 67, 'Charlie': 91, 'David': 70}
# topper = {}

# for key, value in scores.items():
#     # print(key, value)
#     if value > 75:
#         topper[key] = value
        

# print(topper)


# 9. Use a list comprehension to get all the numbers divisible by 3 from 1 to 50.

# l1 = [i for i in range(1,50) if i % 3 == 0]
# print(l1)

# 10. Write a function that takes a string and returns a dictionary with the count of each character.

# def IDK(word):
    
#     dict1 = {}
#     for letter in word:
#         if letter in dict1:
#             dict1[letter] += 1
#         else:
#             dict1[letter] = 1

#     print(dict1)
    
# IDK("data")