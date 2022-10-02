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
    0. create a temp_list = []
    1. result = nums[start] + nums[end] + nums[temp_pointer]
    2. if result < 0, then start is still, temp_pointer += 1, end is still.
    3. Then if result == 0, return [nums[start], nums[temp_pointer], nums[end]]
    4. if result > 0, end = end - 1

'''
def three_sum(nums: list(int)):
    nums.sort()
    temp_list = []
    start = 0
    end = len(nums) - 1
    temp_pointer = 1
    while start < end:
        result = nums[start] + nums[temp_pointer] + nums[end]
        if result == 0:
            temp_list.append([nums[start], nums[temp_pointer], nums[end]])
        if result < 0:

        if result > 0:
            end -= 1
        if temp_pointer == end:
            temp_pointer = start + 1
        temp_pointer += 1