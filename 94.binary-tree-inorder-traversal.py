#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(root, tree):
            if not root:
                return
            inorder(root.left,tree)
            tree.append(root.val)
            inorder(root.right,tree)
        tree = []
        inorder(root,tree)
        return tree
# @lc code=end

