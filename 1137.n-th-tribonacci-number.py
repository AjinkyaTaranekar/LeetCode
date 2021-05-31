#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 1
        if n == 0:
            return 0
        if 0 < n < 3:
            return 1
        d = 0
        for i in range(n-2):
            #print(a,b,c,d)
            d = c + b + a
            a = b
            b = c
            c = d
        return d
# @lc code=end

