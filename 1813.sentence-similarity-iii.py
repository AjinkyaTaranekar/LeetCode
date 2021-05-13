#
# @lc app=leetcode id=1813 lang=python3
#
# [1813] Sentence Similarity III
#

# @lc code=start
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()
        if(len(s1)>len(s2)):
            s1,s2 = s2,s1
        while(s1): 
            if s1[0]==s2[0]:
                s1.pop(0)
                s2.pop(0)
            elif s1[-1]==s2[-1]:
                s1.pop()
                s2.pop()
            else:
                return False            
        return True
# @lc code=end

