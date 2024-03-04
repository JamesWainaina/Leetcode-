#!/usr/bin/python3

# time complexity, space complexity is 0(n) 

def Two_sum(nums, target):
    # create a dictionary to store the indices of numbers
    num_indices = {}
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement difference between the two elements
        complement = target - num
        # if complement is in the dictionary
        if complement in num_indices:
            # If found, return the indices of the two numbers
            return [num_indices[complement], i]
        # if  not found , add the current number and its index to the dictionary
        num_indices[num] = i

    # if no solution is found, return an empty list
    return []


nums= [2, 5, 7, 90]
target = 97
result = Two_sum(nums, target)
print(result)