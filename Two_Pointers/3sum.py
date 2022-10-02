'''
Given an integer array nums, 
return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: 
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

    =========
    Thought Process 
    [-8, -5, -4, -1, 0, 1, 2, 8]
    0. create a temp_list = [] to store the list of list three sum.
    1. has 1 loop to traverse the list of length - 2 ele
    2. has two pointers: left and right
        2.1 left = index + 1
        2.2 right = len(nums) - 1
        2.3 if threeSum result > 0:
            + right -= 1
        2.4 if threeSum result < 0:
            + left += 1
        2.5 otherwise
            + append to the temp list
            + left += 1
            + Check the case where left index has duplicate num by using loop
'''
def three_sum(nums: list[int]):
    nums.sort()
    temp_list = []
    for index, value in enumerate(nums):
        left = index + 1
        right = len(nums) - 1  
        if value == nums[index - 1] and index > 0: #Skip the iteration if the next val is duplicated
            continue
        while left < right:
            result = value + nums[left] + nums[right]
            if result > 0:
                right -= 1
            elif result < 0:
                left += 1
            else:
                temp_list.append([value, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return temp_list
    
            
nums = [-8, -5, -4, -1, 0, 1, 2, 8]
print(three_sum(nums))
