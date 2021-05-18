#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.itr(root, 0, res)
        return res
    
    def itr(self, root, level, res):
        if not root:
            return
        if len(res) <= level:
            res.append([])
        res[level].append(root.val)
        self.itr(root.left, level+1, res)
        self.itr(root.right, level+1, res)
# @lc code=end

