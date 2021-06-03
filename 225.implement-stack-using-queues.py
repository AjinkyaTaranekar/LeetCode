#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        self.queue = self.queue[::-1]
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        self.queue = self.queue[::-1]
        return self.queue.pop()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not len(self.queue)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

