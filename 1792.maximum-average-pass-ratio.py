#
# @lc app=leetcode id=1792 lang=python3
#
# [1792] Maximum Average Pass Ratio
#

# @lc code=start
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        impacts = []

        for i in range(n):
            passed,total = classes[i]
            impact = (passed+1)/(total+1) - passed/total
            impacts.append((-impact, passed, total)) 

        heapq.heapify(impacts)

        while(extraStudents > 0):
            impact, passed, total = heapq.heappop(impacts)
            passed, total = passed + 1, total + 1
            impact = (passed+1)/(total+1) - passed/total
            heapq.heappush(impacts, (-impact, passed, total))
            extraStudents -= 1

        result = 0
        for _, passed, total in impacts:
            result += passed/total
        return result/n
# @lc code=end

