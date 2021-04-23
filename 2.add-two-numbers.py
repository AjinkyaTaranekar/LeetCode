#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        count = 0
        head = res
        while l1 and l2:
            res.val = (l1.val+l2.val+count)%10
            if l1.val+l2.val+count > 9:
                count = 1
            else:
                count = 0
            
            l1 = l1.next
            l2 = l2.next
            
            if l1 or l2:
                res.next = ListNode()
                res = res.next
            
        while l1:
            res.val = (l1.val + count)%10
            if l1.val + count > 9:
                count = 1
            else:
                count = 0
            l1 = l1.next
            if l1:
                res.next = ListNode()
                res = res.next
            
        while l2:
            res.val = (l2.val + count)%10
            if l2.val + count > 9:
                count = 1
            else:
                count = 0
            l2 = l2.next
            if l2:
                res.next = ListNode()
                res = res.next
        
        if count:
            res.next = ListNode(1)
        return head
# @lc code=end

