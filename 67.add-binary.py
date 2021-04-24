#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = len(a)
        m = len(b)
        diff = abs(n-m)
        if n>m:
            b = '0'*diff+b
        else:
            a = '0'*diff+a
        
        l = len(a)
        res = []
        count = 0
        for i in range(l-1,-1,-1):
            a_i = int(a[i])
            b_i = int(b[i])
            if a_i + b_i + count >= 2:
                res.append((a_i + b_i + count)%2)
                count = 1
            else:
                res.append(a_i + b_i + count)
                count = 0
        if count:
            res.append(1)
        res = res[::-1]
        return ''.join(map(str,res))
# @lc code=end

