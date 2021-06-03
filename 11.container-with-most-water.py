#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        low, high = 0, len(height) - 1
        water = 0
        while low < high:
            water = max(water, (high - low) * min(height[low], height[high]))
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return water
# @lc code=end

