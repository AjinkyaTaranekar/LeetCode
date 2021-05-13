#
# @lc app=leetcode id=1805 lang=python3
#
# [1805] Number of Different Integers in a String
#

# @lc code=start
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        import re
        res = re.split('[a-z]', word)
        nums = set()
        for i in res:
            if i:
                nums.add(int(i))
        return len(nums)
# @lc code=end

