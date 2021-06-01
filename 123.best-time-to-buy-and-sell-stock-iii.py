#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        release1 = float('-inf')
        release2 = float('-inf')
        hold1 = float('inf')    
        hold2 = float('inf')    
        for price in prices:
            hold1 = min(hold1, price)
            release1 = max(release1, price - hold1)
            hold2 = min(hold2, price - release1)
            release2 = max(release2, price - hold2)
        return release2
# @lc code=end

