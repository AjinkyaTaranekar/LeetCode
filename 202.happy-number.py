#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        memo = set()
        while n not in memo:
            memo.add(n)
            n = sum(int(i)**2 for i in str(n))
        return 1 in memo
# @lc code=end

