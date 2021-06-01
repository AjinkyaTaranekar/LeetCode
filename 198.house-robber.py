#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [0 for i in nums] + [0]
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1,len(nums)):
            val = nums[i]
            dp[i+1] = max(dp[i], dp[i-1] + val)
        return dp[len(nums)];
# @lc code=end

