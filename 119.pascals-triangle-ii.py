#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
import math
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1 for i in range(rowIndex+1)]
        for i in range(1,rowIndex+1):
            res[i] = math.factorial(rowIndex)//(math.factorial(rowIndex-i)*math.factorial(i))
        return res
# @lc code=end

