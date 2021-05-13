#
# @lc app=leetcode id=1812 lang=python3
#
# [1812] Determine Color of a Chessboard Square
#

# @lc code=start
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x,y = ord(coordinates[0]) - ord('a') + 1, int(coordinates[1])
        x %= 2
        y %= 2

        if (x and y) or (not x and not y):
            return False
        return True

# @lc code=end

