#
# @lc app=leetcode id=748 lang=python3
#
# [748] Shortest Completing Word
#

# @lc code=start
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        def transform(word):
            map = {}
            for i in word:
                #print(i)
                if not i.isdigit() and i != ' ':
                    i = i.lower()
                    if i in map:
                        map[i] += 1
                    else:
                        map[i] = 1
            return map
        licensePlate = transform(licensePlate)
        words.sort(key=len)
        for orig_word in words:
            word = transform(orig_word)
            flag = True
            for i in licensePlate:
                if i in word and licensePlate[i] <= word[i]:
                    continue
                else:
                    flag = False
                    break
            if flag:
                return orig_word
            
# @lc code=end

