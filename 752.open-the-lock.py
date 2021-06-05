#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        queue = collections.deque([('0000', 0)])
        visited = set('0000')

        while queue:
            (combi, steps) = queue.popleft()
            if combi == target:
                return steps
            elif combi in deadends:
                continue
            for i in range(4):
                digit = int(combi[i])
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    new_combi = combi[:i] + str(new_digit) + combi[i+1:]
                    if new_combi not in visited:
                        visited.add(new_combi)
                        queue.append((new_combi, steps + 1))
        return -1
# @lc code=end

