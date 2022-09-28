'''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

    Thought Process:
   1. Find the difference between the target and num in the array
   2. If the difference is in hashMap => Return the indexes.
        Otherwise, put key and values to the hash map 
'''
def two_sum(nums: list[int], target: int) -> list[int]:
    hash_map = {}
    for index, num in enumerate(nums):
        difference = target - num
        if difference in hash_map:
            return [hash_map[difference], index]
        hash_map[num] = index

nums = [3, 2, 4]
print(two_sum(nums, 5))