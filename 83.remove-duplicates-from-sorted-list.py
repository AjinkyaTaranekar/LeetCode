#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = head
        res = head
        while head:
            if prev.val == head.val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        
        return res
        
# @lc code=end

