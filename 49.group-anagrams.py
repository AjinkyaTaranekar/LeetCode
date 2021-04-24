#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))  
            if sorted_s in d:
                d[sorted_s] += [s]
            else:
                d[sorted_s] = [s]
        
        return d.values()
# @lc code=end

