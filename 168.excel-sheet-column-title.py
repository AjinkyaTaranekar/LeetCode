#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        aplha = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while columnNumber > 0:
            result.append(aplha[(columnNumber - 1) % 26])
            columnNumber = (columnNumber - 1) // 26
        return ''.join(result[::-1])
# @lc code=end

