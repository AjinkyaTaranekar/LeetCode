#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        if not n:
            return 0
        for i in range(m-n+1):
            for j in range(n):
                if haystack[i+j] != needle[j]:
                    break
                if j == n-1:
                    return i
        return -1

# @lc code=end

