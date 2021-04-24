#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i] >= last:
                last = i
        return last == 0
# @lc code=end

