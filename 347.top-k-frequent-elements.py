#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
            if i in map:
                map[i] = map[i] +1
            else:
                map[i] = 1
        
        arr = sorted(map, key = map.get, reverse = True)
        return arr[:k]
# @lc code=end

