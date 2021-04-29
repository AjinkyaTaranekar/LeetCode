#
# @lc app=leetcode id=990 lang=python3
#
# [990] Satisfiability of Equality Equations
#

# @lc code=start
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        lookup = [[] for i in range(26)]

        for equation in equations:
            if equation[1] == '=':
                x = ord(equation[0]) - ord('a')
                y = ord(equation[3]) - ord('a')
                lookup[x].append(y)
                lookup[y].append(x)

        color = [None] * 26
        count = 0
        for start in range(26):
            if color[start] is None:
                count += 1
                stack = [start]
                while stack:
                    node = stack.pop()
                    for neighbour in lookup[node]:
                        if color[neighbour] is None:
                            color[neighbour] = count
                            stack.append(neighbour)

        for equation in equations:
            if equation[1] == '!':
                x = ord(equation[0]) - ord('a')
                y = ord(equation[3]) - ord('a')
                if x == y:
                    return False
                if color[x] is not None and color[x] == color[y]:
                    return False
        return True
# @lc code=end

