#!/bin/python3
# Creating a set
fruit_set = {"Apple", "Banana", "Orange"}

# Displaying the set
print("Set:", fruit_set)

# Checking if an element exists
element_to_check = "Banana"
if element_to_check in fruit_set:
    print(element_to_check, "is present in the set.")
else:
    print(element_to_check, "is not present in the set.")
