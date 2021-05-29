#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = [0]*(len(word1)+len(word2))
        i,j,k = 0,0,0
        while i < len(word1) and j < len(word2):
            if k%2:
                res[k] = word2[j]
                j+=1
            else:
                res[k] = word1[i]
                i+=1
            k+=1
        while i < len(word1):
            res[k] = word1[i]
            i+=1
            k+=1
        while j < len(word2):
            res[k] = word2[j]
            j+=1
            k+=1
        return "".join(res)
# @lc code=end

