#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.tree = []
        def inorder(root, tree):
            if not root:
                return
            inorder(root.left, self.tree)
            self.tree.append(root.val)
            inorder(root.right, self.tree)
        inorder(root, self.tree)
        self.curr = -1

    def next(self) -> int:
        self.curr += 1
        return self.tree[self.curr]

    def hasNext(self) -> bool:
        return self.curr < len(self.tree) - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

