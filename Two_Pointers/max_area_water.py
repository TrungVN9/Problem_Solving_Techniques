'''
You are given an integer array height of length n. 
There are n vertical lines drawn 
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.


Input: height = [1,1]
Output: 1

======== THOUGHT PROCESS ========
   Brute Foce Approach
   1. Using two nested loop to calculate the height and the width
   2. Return ans with max area.
   Run time: O(n^2)
   Two Pointers Approach
   1. Create a left and a right pointer
   2. Check the height at the left and the right pointer.
        + If height at left > height at right:
            + Decrement right -= 1
        + Otherwise
            + Increment left += 1
'''


def max_area_brute_force(height: list[int]) -> int:
    ans = 0
    for left in range(len(height) - 1):
        for right in range(left + 1, len(height)):
            temp_height = min(height[left], height[right])
            area = (right - left) * temp_height
            ans = max(ans, area)
    return ans

def max_area_two_pointers(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    ans = 0
    while left < right:
        width = (right - left)
        temp_height = min(height[left], height[right])
        ans = max(ans, width * temp_height)
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return ans
