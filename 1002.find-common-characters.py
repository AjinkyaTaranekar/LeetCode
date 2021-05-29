#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#

# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter
        if len(words) < 2:
            return words
			
        count = Counter(words[0])
        for w in words[1:]:
            count &= Counter(w)
			
        return list(count.elements())    
# @lc code=end

