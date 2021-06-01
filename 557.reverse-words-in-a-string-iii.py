#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        return ' '.join([i[::-1] for i in s])
# @lc code=end

