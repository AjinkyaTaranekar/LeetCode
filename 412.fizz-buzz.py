#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            char = str(i)
            if i % 3 == 0 and i % 5 == 0:
                char = 'FizzBuzz'
            elif i % 3 == 0:
                char = 'Fizz'
            elif i % 5 == 0:
                char = 'Buzz'
            res.append(char)
        return res
# @lc code=end

