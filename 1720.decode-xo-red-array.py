#
# @lc app=leetcode id=1720 lang=python3
#
# [1720] Decode XORed Array
#

# @lc code=start
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for i,v in enumerate(encoded):
            res.append(v^res[-1])
        return res
# @lc code=end

