#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        bin='{0:032b}'.format(n)
        return int(bin[::-1],2)
# @lc code=end

