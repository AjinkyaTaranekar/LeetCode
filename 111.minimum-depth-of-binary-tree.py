#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        return max(l,r) + 1 if None in [root.left, root.right] else min(l,r) + 1 
# @lc code=end

