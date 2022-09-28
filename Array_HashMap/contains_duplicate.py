''' 
    Given an integer array nums, 
    return true if any value appears at least twice in the array, 
    return false if every element is distinct.
    
    Input: nums = [1,2,3,1]
    Output: true
    
    Input: nums = [1,2,3,4]
    Output: false

Thought Process:
    //Create a hash map with key as indexes and values.
    //if the value is appeared in the hash map already, return True
    // Otherwise continue put key and values into the hash map
'''
def contains_duplicate(nums: list[int]) -> bool:
    hash_map = {}
    for index, num in enumerate(nums):
        if num in hash_map:
            return True
        hash_map[num] = index
    return False

my_list = []
print(contains_duplicate(my_list))