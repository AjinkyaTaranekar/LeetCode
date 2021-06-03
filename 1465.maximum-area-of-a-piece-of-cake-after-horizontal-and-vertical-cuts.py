#
# @lc app=leetcode id=1465 lang=python3
#
# [1465] Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
#

# @lc code=start
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        horizontalCuts.insert(0, 0)
        horizontalCuts.append(h)
        
        verticalCuts.sort()
        verticalCuts.insert(0, 0)
        verticalCuts.append(w)

        max_hor = float('-inf')
        max_ver = float('-inf')
        for i, j in zip(horizontalCuts, horizontalCuts[1:]):
            max_hor = max(max_hor, j - i)
        for i, j in zip(verticalCuts, verticalCuts[1:]):
            max_ver = max(max_ver, j - i)
        return max_hor * max_ver % 1000000007
# @lc code=end

