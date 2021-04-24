#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = nums.count(0)
        one = nums.count(1) + zero
        two = nums.count(2) + one
        
        for i in range(len(nums)):
            if i < zero:
                nums[i] = 0
            elif zero <= i < one:
                nums[i] = 1
            elif one <= i < two:
                nums[i] = 2
        
# @lc code=end

