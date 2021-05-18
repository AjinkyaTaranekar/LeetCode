#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        res = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i in range(len(row)):
                res[i] = row[i] + min(res[i], res[i + 1])
        return res[0]
# @lc code=end

