#
# @lc app=leetcode id=1796 lang=python3
#
# [1796] Second Largest Digit in a String
#

# @lc code=start
class Solution:
    def secondHighest(self, s: str) -> int:
        nums = set()
        for i in s:
            if i.isnumeric():
                nums.add(i)
        if len(nums) <= 1:
            return -1
        return sorted(nums, reverse=True)[1]
# @lc code=end

