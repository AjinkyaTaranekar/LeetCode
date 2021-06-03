#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        for i in nums:
            if not ranges or i > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = i,
        return ['->'.join(map(str, r)) for r in ranges]

# @lc code=end

