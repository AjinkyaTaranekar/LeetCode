#
# @lc app=leetcode id=1009 lang=python3
#
# [1009] Complement of Base 10 Integer
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = bin(n)[2:]
        res = ''
        for i in b:
            res += '0' if i == '1' else '1'
        return int(res, 2)
# @lc code=end

