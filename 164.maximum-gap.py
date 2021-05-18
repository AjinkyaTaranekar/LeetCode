#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#

# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 1:
            return 0
        maxi = 0
        for i in range(len(nums)-1):
            maxi = max(maxi, nums[i+1]-nums[i])
        return maxi
# @lc code=end

