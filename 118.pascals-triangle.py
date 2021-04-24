#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1 for i in range(j)] for j in range(1,numRows+1)]
        for i in range(2,numRows):
            for j in range(1,i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
            #print(res)
        return res
# @lc code=end

