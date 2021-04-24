#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        neg = False if x > 0 else True
        if neg:
            x*=-1
        
        rev = 0
        while x:
            p = math.floor(math.log10(x))
            mod = x%10
            #print(p, mod)
            rev+=mod*10**p
            x //= 10
        
        rev = -1*rev if neg else rev
        if -2**31 >= rev or rev >= 2**31:
            return 0
        return int(rev)
# @lc code=end

