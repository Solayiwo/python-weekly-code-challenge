#!/usr/bin/python3

# get input from a user and storing it in a variable
name = input("Enter your name: ")
age = int(input("Enter your age: "))
location = input("Enter your location: ")

# print a message by concatenating string using the "+" Operator
print("Hello " + name + ", you are " + str(age) + " years old and live in " + location + ".")

# print a message by concatenating string using format() Method 
print("Hello {}, you are {} years old and live in {}.".format(name, age, location))

# print a message by concatenating string using f-strings (Formatted String Literals)
print(f"Hello {name}, you are {age} years old and live in {location}.")