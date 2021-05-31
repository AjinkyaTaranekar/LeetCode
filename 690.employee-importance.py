#
# @lc app=leetcode id=690 lang=python3
#
# [690] Employee Importance
#

# @lc code=start
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def findEmployee(employees, id):
            for employee in employees:
                if id == employee.id:
                    return employee
                    
        employee = findEmployee(employees, id)
        imp = employee.importance
        queue = employee.subordinates
        while queue:
            e = findEmployee(employees, queue.pop())
            imp += e.importance
            queue += e.subordinates
        return imp            
# @lc code=end

