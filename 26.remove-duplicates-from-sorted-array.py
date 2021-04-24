#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if not n:
            return 0
        i = 0
        for j in range(n):
            if nums[j] != nums[i]:
                i+=1
                nums[i]=nums[j]
        return i+1
# @lc code=end

