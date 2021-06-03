#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for s in columnTitle:
            res = res * 26 + ord(s) - ord('A') + 1
        return res
# @lc code=end

