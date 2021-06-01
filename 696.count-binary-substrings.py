#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        prev = 0
        curr = 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                count += min(curr, prev)
                prev = curr
                curr = 1
            else:
                curr +=1 
        count += min(curr, prev)
        return count
# @lc code=end

