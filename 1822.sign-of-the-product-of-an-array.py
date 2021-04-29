#
# @lc app=leetcode id=1822 lang=python3
#
# [1822] Sign of the Product of an Array
#

# @lc code=start
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negative = 0
        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                negative+=1
        return -1 if negative%2 else 1

# @lc code=end

