#
# @lc app=leetcode id=1784 lang=python3
#
# [1784] Check if Binary String Has at Most One Segment of Ones
#

# @lc code=start
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return '01' not in s
# @lc code=end

