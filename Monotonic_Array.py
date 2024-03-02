#!/usr/bin/python3
"""
Question 2: Monotonic Array - An array is monotonic if it is either monotone increasing or monotone decreasing.
An array is monotone increasing if all its elements from left to right are non-decreasing. 
An array is monotone decreasing if all  its elements from left to right are non-increasing. 
Given an integer array return true if the given array is monotonic, or false otherwise.
example of a monotonic non-increasing array = [5,4,3,2,1]
"""

def monotonic_array(arr):
    # checks is the array is in non-increasing order
    non_increasing = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

    # checks if the array is non-decreasing order
    non_decreasing = all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))

    return non_decreasing or non_increasing

arr1 = [2 ,4 ,6 ,8]
arr2 = [8, 7, 5, 2]
result1 = monotonic_array(arr1)
result2 = monotonic_array(arr2)