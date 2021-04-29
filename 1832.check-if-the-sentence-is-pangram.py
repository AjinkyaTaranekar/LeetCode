#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        map = {i: False for i in range(26)}
        for i in sentence:
            map[ord(i)-ord('a')] = True
        print(map)
        return all(map.values())
# @lc code=end

