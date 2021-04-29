#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_,t_ = '',''
        map = {}
        rev = {}
        for i,v in enumerate(s):
            map[v] = t[i]
            rev[t[i]] = v

        for i,v in enumerate(s):
            s_+=rev[t[i]]
            t_+=map[v]
        
        return t_ == t and s_ == s
# @lc code=end

