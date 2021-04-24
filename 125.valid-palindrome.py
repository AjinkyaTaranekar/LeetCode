#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        preprocess = ''
        for i in s:
            if i.isalnum():
                preprocess+=i.lower()
        return preprocess == preprocess[::-1]
        
# @lc code=end

