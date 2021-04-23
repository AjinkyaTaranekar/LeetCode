#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSym(left,right):
            if left and right and left.val == right.val: 
                return isSym(left.left, right.right) and isSym(left.right, right.left)
            return left == right
        return not root or isSym(root.left, root.right)
# @lc code=end

