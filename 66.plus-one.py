#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits[-1] = digits[-1] + 1
        count = 1 if digits[-1] > 9 else 0
        if count:
            digits[-1] = 0
        for i in range(len(digits)-2,-1,-1):
            if digits[i] + count > 9:
                digits[i] = 0
                count = 1
            else:
                digits[i] += count
                count = 0
        if count:
            digits.insert(0,1)
        return digits
            
# @lc code=end

