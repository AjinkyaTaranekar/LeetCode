#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        res = 0
        i,j = 0,0
        max_upto = 0
        while i < len(s) and j < len(s):
            if s[j] in map:
                map = {}
                res = max(max_upto,res)
                max_upto = 0
                i+=1
                j=i
            else:
                map[s[j]] = 1
                j+=1
                max_upto+=1
        res = max(max_upto,res)
        return res
# @lc code=end

