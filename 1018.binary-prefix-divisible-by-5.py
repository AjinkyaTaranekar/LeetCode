#
# @lc app=leetcode id=1018 lang=python3
#
# [1018] Binary Prefix Divisible By 5
#

# @lc code=start
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        temp = ''
        for i in nums:
            temp += str(i)
            res.append(int(temp,2)%5==0)
        return res
# @lc code=end

