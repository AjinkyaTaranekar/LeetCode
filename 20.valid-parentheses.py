#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2:
            return False
        
        stack = []
        for i in range(n):
            if s[i] in '([{':
                stack.append(s[i])
            if stack:
                if s[i] in '([{':
                    continue
                elif stack[-1] == '(' and s[i] == ')':
                    stack.pop(-1)
                elif stack[-1] == '{' and s[i] == '}':
                    stack.pop(-1)
                elif stack[-1] == '[' and s[i] == ']':
                    stack.pop(-1)
                else:
                    return False
            else:
                return False
        return True if not stack else False
# @lc code=end

