#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2 or n == 3:
            return n - 1
        if n % 3 == 0:
            return 3**(n//3)
        if n % 3 == 1:
            return 3**(n//3 - 1)*4
        if n % 3 == 2:
            return 3**(n//3)*2
# @lc code=end

