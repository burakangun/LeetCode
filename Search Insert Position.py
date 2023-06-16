"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""

def searchInsert(nums, target):
    try:
        ans = nums.index(target)
        return ans
    except:
        for pointer in range(len(nums)):
            if target < nums[pointer] and pointer == 0:
                return 0
            elif pointer != len(nums) - 1:
                if target > nums[pointer] and target < nums[pointer + 1]:
                    ans = pointer + 1
                    return ans
            else:
                if target > nums[pointer]:
                    ans = len(nums)
                    return ans