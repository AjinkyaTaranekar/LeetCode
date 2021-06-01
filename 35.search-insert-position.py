#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0 
        high = len(nums)-1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                if nums[mid]== target and nums[mid - 1] != target:
                    return mid
                else:
                    high = mid - 1
        return low
# @lc code=end

