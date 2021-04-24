#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1,2]
        for i in range(2,n):
            dp.append(dp[i-2]+dp[i-1])
        return dp[n-1]
# @lc code=end

