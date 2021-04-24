#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        palin = '' 
        for i in range(len(s)): 
            for j in range(len(s), i, -1):
                if len(palin) >= j-i:
                    break
                elif s[i:j] == s[i:j][::-1]:
                    palin = s[i:j]
                    break
        return palin
# @lc code=end

