#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        
        pos = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    pos.append((i,j))   
        
        for i,j in pos:
            matrix[i] = [0]*col
            for k in range(row):
                matrix[k][j] = 0
        
# @lc code=end

