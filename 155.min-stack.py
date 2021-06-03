#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float('inf')
        

    def push(self, val: int) -> None:
        if self.stack:
            self.min = min([val, self.stack[-1][0], self.min]) 
            self.stack.append((val, self.min))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1][0] == self.stack[-1][1]:
                if len(self.stack) > 1:
                    self.min = self.stack[-2][1]
                else:
                    self.min = float('inf')
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

