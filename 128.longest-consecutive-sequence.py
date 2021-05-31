#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxi = 0
        while nums:
            curr = nums.pop()
            i = curr + 1
            l1, l2 = 0, 0
            while i in nums:
                nums.remove(i)
                i += 1
                l1 +=1
            i = curr - 1
            while i in nums:
                nums.remove(i)
                i -= 1
                l2 +=1
            maxi = max(maxi, l1 + l2 + 1)
        return maxi
# @lc code=end

