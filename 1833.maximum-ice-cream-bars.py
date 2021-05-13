#
# @lc app=leetcode id=1833 lang=python3
#
# [1833] Maximum Ice Cream Bars
#

# @lc code=start
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        if costs[0] > coins:
            return 0
        count = 0
        for i in costs:
            if coins >= i:
                coins -= i
                count += 1
        return count
# @lc code=end

