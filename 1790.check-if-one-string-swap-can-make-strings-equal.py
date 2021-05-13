#
# @lc app=leetcode id=1790 lang=python3
#
# [1790] Check if One String Swap Can Make Strings Equal
#

# @lc code=start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: 
            return True
        allowed = 1
        pair = {}
        for i in range(len(s1)):
            p = (s1[i], s2[i])
            if s1[i] != s2[i]:
                if p in pair:
                    return False
                else:
                    pair[p] = 1
            else:
                continue
        for i in pair:
            #print(i, i[::-1])
            if i[::-1] not in pair:
                return False
        return len(pair) <= 2
# @lc code=end

