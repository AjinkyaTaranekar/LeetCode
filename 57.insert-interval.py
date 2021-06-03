#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals += [newInterval]
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if res[-1][0] <= intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])
        return res
# @lc code=end

