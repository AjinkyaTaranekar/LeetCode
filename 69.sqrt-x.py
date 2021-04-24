#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        low = 0
        high = x
        
        while low < high:
            mid = low + (high - low)//2
            #print(mid)
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                high = mid - 1
            else:
                low = mid + 1
        return high
        
# @lc code=end

