#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3= len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False

        queue = [(0, 0)] 
        visited = set((0, 0))
        while queue:
            x, y = queue.pop(0)
            if x + y == l3:
                return True
            if x + 1 <= l1 and s1[x] == s3[x + y] and (x + 1, y) not in visited:
                queue.append((x + 1, y))
                visited.add((x + 1, y))
            if y + 1 <= l2 and s2[y] == s3[x + y] and (x, y + 1) not in visited:
                queue.append((x, y + 1))
                visited.add((x, y + 1))
        return False
# @lc code=end

