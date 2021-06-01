#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a = 0
        b = 1
        c = 0
        for i in range(n-1):
            c = a + b
            a = b
            b = c
        return c
# @lc code=end

