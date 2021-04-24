#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for i in range(n-1):
            let, temp, count = res[0], '', 0
            for l in res:
                if let == l:
                    count += 1
                else:
                    temp += str(count)+let
                    let = l
                    count = 1
            temp += str(count)+let
            res = temp
        return res
# @lc code=end

