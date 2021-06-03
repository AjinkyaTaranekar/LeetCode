#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = sum(int(i) for i in str(num))
        return num
# @lc code=end

