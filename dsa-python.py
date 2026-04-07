# type(42) # <class 'int'>
# type(3.14) # <class 'float'>
# type("Hello") # <class 'str'>
# type(True) # <class 'bool'>
# type(None) # <class 'NoneType'>


# int("42") # 42
# float("3.14") # 3.14
# str(42) # "42"
# bool(1) # True
# list("abc") # ["a", "b", "c"]


# x, y = 10, 20 # Assign multiple values
# a = b = c = 0 # Give same value to multiple variables

# single = 'Hello'
# double = "World"
# multi = """Multiple
# line string"""


# greeting = "me" + "ow!" # "meow!"
# repeat = "Meow!" * 3 # "Meow!Meow!Meow!"
# length = len("Python") # 6


# "a".upper() # "A"
# "A".lower() # "a"
# " a ".strip() # "a"
# "abc".replace("bc", "ha") # "aha"
# "a b".split() # ["a", "b"]
# "-".join(["a", "b"]) # "a-b"

# text = "Python"
# text[0] # "P" (first)
# text[-1] # "n" (last)
# text[1:4] # "yth" (slice)
# text[:3] # "Pyt" (from start)
# text[3:] # "hon" (to end)
# text[::2] # "Pto" (every 2nd)
# text[::-1] # "nohtyP" (reverse)


# # f-strings
# name = "Aubrey"
# age = 2
# f"Hello, {name}!" # "Hello, Aubrey!"
# f"{name} is {age} years old" # "Aubrey is 2 years old"
# f"Debug: {age=}" # "Debug: age=2"
# # Format method
# template = "Hello, {name}! You're {age}."
# template.format(name="Aubrey", age=2) # "Hello, Aubrey! You're 2."

# # Normal string with an escaped tab
# "This is:\tCool." # "This is: Cool."
# # Raw string with escape sequences
# r"This is:\tCool." # "This is:\tCool."


# 10 + 3 # 13
# 10 - 3 # 7
# 10 * 3 # 30
# 10 / 3 # 3.3333333333333335
# 10 // 3 # 3
# 10 % 3 # 1
# 2 ** 3 # 8


# abs(-5) # 5
# round(3.7) # 4
# round(3.14159, 2) # 3.14
# min(3, 1, 2) # 1
# max(3, 1, 2) # 3
# sum([1, 2, 3]) # 6



# if age < 13:
#     category = "child"
# elif age < 20:
#     category = "teenager"
# else:
#     category = "adult"



# # if age >= 18 and has_car:
# #     print("Roadtrip!")
# # if is_weekend or is_holiday:
# #     print("No work today.")
# # if not is_raining:
# #     print("You can go outside.")


# # Loops

# # range(5) generates 0 through 4
# # Use enumerate() to get index and value
# # break exits the loop, continue skips to next
# # Be careful with while to not create an infinite loop

# # Loop through range
# for i in range(5): # 0, 1, 2, 3, 4
#     print(i)
# # Loop through collection
# fruits = ["apple", "banana"]
# for fruit in fruits:
#     print(fruit)
# # With enumerate for index
# for i, fruit in enumerate(fruits):
#     print(f"{i}: {fruit}")


# while False:
#     user_input = input("Enter 'quit' to exit: ")
#     if user_input == "quit":
#         break
#     print(f"You entered: {user_input}")

def add(x, y=10):
    print(x, y, x+y)  # 2, 10, 12

add(2)

def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3])  # multiple returns like golang

# callable()

# Lambda function
# square = lambda x: x**2
# result = square(5) # 25
# # With map and filter
# numbers = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, numbers))
# evens = list(filter(lambda x: x % 2 == 0, numbers))



class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        return f"{self.name} says Woof!"
# Create instance
my_dog = Dog("Frieda", 3)
print(my_dog.bark()) # Frieda says Woof!


class Cat:
    species = "Felis catus" # Class attribute
    def __init__(self, name):
        self.name = name # Instance attribute
    def meow(self):
        return f"{self.name} says Meow!"
    @classmethod
    def create_kitten(cls, name):
        return cls(f"Baby {name}")
    

try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result: {result}")
finally:
    print("Calculation attempted")

# Common Exceptions
# ValueError # Invalid value
# TypeError # Wrong type
# IndexError # List index out of range
# KeyError # Dict key not found
# FileNotFoundError # File doesn't exist


# Raising Exceptions
# def validate_age(age):
#   if age < 0:
#       raise ValueError("Age cannot be negative")
#   return age
# Learn More on realpython.com/search:

# exceptions ∙ errors ∙ debugging



# Lists
# Creating lists
empty = []
nums = [5]
mixed = [1, "two", 3.0, True]
# List methods
nums.append("x") # Add to end
nums.insert(0, "y") # Insert at index 0
nums.extend(["z", 5]) # Extend with iterable
nums.remove("x") # Remove first "x"
last = nums.pop() # Pop returns last element
# List indexing and checks
fruits = ["banana", "apple", "orange"]
fruits[0] # "banana"
fruits[-1] # "orange"
"apple" in fruits # True

# Tuples
# Creating tuples
point = (3, 4)
single = (1,) # Note the comma!
empty = ()
# Basic tuple unpacking
point = (3, 4)
x, y = point
x # 3
y # 4
# Extended unpacking
first, *rest = (1, 2, 3, 4)
first # 1
rest # [2, 3, 4]


# Sets
# Creating Sets
a = {1, 2, 3}
b = set([3, 4, 4, 5])
# Set Operations
a | b # {1, 2, 3, 4, 5}
a & b # {3}
a - b # {1, 2}
a ^ b # {1, 2, 4, 5}


#   Dictionaries
# Creating Dictionaries
empty = {}
pet = {"name": "Leo", "age": 42}
# Dictionary Operations
pet["sound"] = "Purr!" # Add key and value
pet["age"] = 7 # Update value
age = pet.get("age", 0) # Get with default
del pet["sound"] # Delete key
pet.pop("age") # Remove and return
# Dictionary Methods
pet = {"name": "Frieda", "sound": "Bark!"}
pet.keys() # dict_keys(['name', 'sound'])
pet.values() # dict_values(['Frieda', 'Bark!'])
pet.items() # dict_items([('name', 'Frieda'), ('sound', 'Bark!')])



# Code: squares = [x**2 for x in range(10)]
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Code: evens = [x for x in range(10) if x % 2 == 0]
# Output: [0, 2, 4, 6, 8]

# Code: labels = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
# Output: ['Even', 'Odd', 'Even', 'Odd', 'Even']

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# new_list = [x.upper() for x in fruits if "a" in x]
# Output: ['APPLE', 'BANANA', 'MANGO']


# matrix = [[1, 2], [3, 4], [5, 6]]
# flat = [num for row in matrix for num in row]
# Output: [1, 2, 3, 4, 5, 6]



word_lengths = {word: len(word) for word in ["hello", "world"]}

print(word_lengths)  # {'hello': 5, 'world': 5}


# File Operations
# Read an entire file
# with open("file.txt", mode="r", encoding="utf-8") as file:
#     content = file.read()
# # Read a file line by line
# with open("file.txt", mode="r", encoding="utf-8") as file:
#     for line in file:
#         print(line.strip())
# # Write a file
# with open("output.txt", mode="w", encoding="utf-8") as file:
#     file.write("Hello, World!\n")
# # Append to a File
# with open("log.txt", mode="a", encoding="utf-8") as file:
#     file.write("New log entry\n")




# Import Styles
# # Import entire module
# import math
# result = math.sqrt(16)
# # Import specific function
# from math import sqrt
# result = sqrt(16)
# # Import with alias
# import numpy as np
# array = np.array([1, 2, 3])
# # Import all (not rec


# Pythonic Constructs
# # Swap variables
# a, b = b, a
# # Flatten a list of lists
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flat = [item for sublist in matrix for item in sublist]
# # Remove duplicates
# unique_unordered = list(set(my_list))
# # Remove duplicates, preserve order
# unique = list(dict.fromkeys(my_list))
# # Count occurrences
# from collections import Counter
# counts = Counter(my_list)









class Student:
    name = ""

    def __init__(self, name):
        self.name = name
    def printName(self):
        print(self.name)


student = Student("vijju")
student.printName()