#
# @lc app=leetcode id=1827 lang=python3
#
# [1827] Minimum Operations to Make the Array Increasing
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                continue
            else:
                count += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1] + 1
        print(nums)
        return count
# @lc code=end

