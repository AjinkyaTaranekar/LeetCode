#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers)-1
        while low < high:
            mid = numbers[low] + numbers[high]
            if mid == target:
                return [low + 1, high + 1]
            elif mid < target:
                low += 1
            else:
                high -= 1
# @lc code=end

