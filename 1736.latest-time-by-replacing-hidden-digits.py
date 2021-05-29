#
# @lc app=leetcode id=1736 lang=python3
#
# [1736] Latest Time by Replacing Hidden Digits
#

# @lc code=start
class Solution:
    def maximumTime(self, time: str) -> str:
        max_time = "23:59" if time[0] in "?2" and time[1] in "?0123" else "19:59"
        res = ''
        for i,v in enumerate(time):
            if v == '?':
                res += max_time[i]
            else:
                res += v
        return res
# @lc code=end

