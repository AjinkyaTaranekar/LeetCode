#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(root, tree):
            if not root:
                return
            inorder(root.left,tree)
            tree.append(root.val)
            inorder(root.right,tree)
        tree = []
        inorder(root,tree)
        return tree[k-1]
# @lc code=end

