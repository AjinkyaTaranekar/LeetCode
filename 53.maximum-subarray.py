#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        maxi, upto = 0,0
        for i in nums:
            upto += i
            if upto < 0:
                upto = 0
            maxi = max(maxi,upto)
        return maxi
            
# @lc code=end

