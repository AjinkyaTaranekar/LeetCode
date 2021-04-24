#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        upto = 0
        for i in nums:
            if i:
                upto+=1
            else:
                maxi = max(maxi, upto)
                upto = 0
        maxi = max(maxi, upto)
        return maxi
# @lc code=end

