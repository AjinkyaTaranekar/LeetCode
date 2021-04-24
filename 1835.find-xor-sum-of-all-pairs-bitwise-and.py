#
# @lc app=leetcode id=1835 lang=python3
#
# [1835] Find XOR Sum of All Pairs Bitwise AND
#

# @lc code=start
class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        xor = 0
        for i in arr2:
            xor ^= i
        res = 0
        for i in arr1:
            res ^= (i&xor)
        return res
# @lc code=end

