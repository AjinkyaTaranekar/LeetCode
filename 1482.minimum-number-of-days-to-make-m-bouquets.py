#
# @lc app=leetcode id=1482 lang=python3
#
# [1482] Minimum Number of Days to Make m Bouquets
#

# @lc code=start
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k>n:
            return -1
        elif m*k == n:
            return max(bloomDay)
        
        low,high = 1,max(bloomDay)
        
        def check(days):
            bonquets,flowers = 0,0
            for bloom in bloomDay:
                if bloom > days:
                    flowers = 0
                else:
                    bonquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
            return bonquets >= m

        while low < high:
            mid = low + (high - low)//2
            if check(mid):
                high = mid
            else:
                low = mid + 1
        return low
# @lc code=end

