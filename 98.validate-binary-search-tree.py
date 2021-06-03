#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        tree = []
        self.inOrder(root, tree)
        
        for i in range(1, len(tree)):
            if tree[i-1] >= tree[i]:
                return False
        return True

    def inOrder(self, root, tree):
        if root is None:
            return
        
        self.inOrder(root.left, tree)
        tree.append(root.val)
        self.inOrder(root.right, tree)

# @lc code=end

