#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        res = 0
        for i in range(1,int(num**0.5) + 1):
            if num % i == 0:
                res += i
                res += num//i
        #print(res)
        return num == res - num
# @lc code=end

