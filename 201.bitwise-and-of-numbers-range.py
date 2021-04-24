#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = left
        if len(bin(left)) != len(bin(right)): 
            return 0
        for i in range(left,right+1):
            res&=i
            if res == 0:
                break
        return res
# @lc code=end

