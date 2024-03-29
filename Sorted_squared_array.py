#!/usr/bin/python3
"""

-Array Data Structure Crash Course

Question 1: Sorted Squared Array - You are given an array of Integers in which each subsequent value is not
less than the previous value. 
Write a function that takes this array as an input and returns a new array with the squares of each number
sorted in ascending order.

"""

# def sorted_array(arr):
#     """function that takes in array an sorts it and prints the squares of each number"""
#     squared_arr = [num ** 2 for num in arr]

#     squared_arr.sort()
#     return squared_arr

# input_array = [45, 34, 90, 65]
# result = sorted_array(input_array)
# print(result)

# time complexity 0(nlogn) space complexity 0(n)
def squared_sorted_array(array):
    new_array = [0] * len(array)
    for i in range(len(array)):
        new_array[i] = array[i] ** 2

    new_array.sort()
    return new_array

print(squared_sorted_array([2, 3, -8, 70]))
print(squared_sorted_array([70,4,2,900,50]))
print(squared_sorted_array([]))