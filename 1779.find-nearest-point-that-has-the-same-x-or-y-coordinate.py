#
# @lc app=leetcode id=1779 lang=python3
#
# [1779] Find Nearest Point That Has the Same X or Y Coordinate
#

# @lc code=start
class Solution:
    def manhattan_distance(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        p = []
        min_dis = float('inf')
        for i,point in enumerate(points):
            if x == point[0] or y == point[1]:
                p.append((i,point))
                min_dis = min(min_dis,self.manhattan_distance([x,y], point))
        res = []
        for i,point in p:
            if self.manhattan_distance([x,y], point) == min_dis:
                res.append(i)
        print(res, p)
        return min(res) if res else -1
# @lc code=end

