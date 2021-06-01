#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return
        root = TreeNode(preorder[0])
        i = 1
        while i < len(preorder):
            if preorder[i] < preorder[0]: 
                i += 1
            else: 
                break
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root
# @lc code=end

