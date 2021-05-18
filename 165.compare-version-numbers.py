#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')

        if len(version1) > len(version2):
            version2 += [0] * (len(version1) - len(version2))
        if len(version1) < len(version2):
            version1 += [0] * (len(version2) - len(version1))

        for i in range(len(version1)):
            if int(version1[i]) > int(version2[i]):
                return 1
            elif int(version1[i]) < int(version2[i]):
                return -1
            else:
                continue
        return 0

# @lc code=end

