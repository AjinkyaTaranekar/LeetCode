#
# @lc app=leetcode id=1823 lang=python3
#
# [1823] Find the Winner of the Circular Game
#

# @lc code=start
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = [i for i in range(1,n+1)]
        k -= 1
        pos = k
        while len(l) > 1:
            l.pop(pos)
            pos = (pos+k) % len(l)
        return l[0]
# @lc code=end

