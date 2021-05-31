#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        volume = 0
        left, right = 0, len(height) - 1
        l, r = height[left], height[right]
        while left < right:
            l, r = max(height[left], l), max(height[right], r)
            if l <= r:
                volume += l - height[left]
                left += 1
            else:
                volume += r - height[right]
                right -= 1
        return volume
# @lc code=end

