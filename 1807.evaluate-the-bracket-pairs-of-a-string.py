#
# @lc app=leetcode id=1807 lang=python3
#
# [1807] Evaluate the Bracket Pairs of a String
#

# @lc code=start
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge = {i[0]:i[1] for i in knowledge}
        res = ''
        start = False
        word = ''
        for i in s:
            #print(i,word,start,res)
            if i == '(':
                start = True
                continue
            if start:
                if i == ')':
                    start = False
                else:
                    word+=i
                    continue
            if word:
                res+=knowledge[word] if word in knowledge else '?'
                word = ''
                continue
            res += i
        return res
# @lc code=end

