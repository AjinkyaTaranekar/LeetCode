#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre=''
        for x in zip(*strs):
            if len(set(x)) == 1:
                pre+=x[0]
            else:
                break
        return pre    
# @lc code=end

