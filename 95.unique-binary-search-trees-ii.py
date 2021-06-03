#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def trees(first, last):
            return [TreeNode(root, left, right)
                    for root in range(first, last+1)
                    for left in trees(first, root-1)
                    for right in trees(root+1, last)] or [None]
        return trees(1, n)  
# @lc code=end

