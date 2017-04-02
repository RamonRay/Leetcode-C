# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pointer = dummy
        while pointer.next and pointer.next.next:
            a = pointer.next
            b = pointer.next.next
            a.next = b.next
            b.next = a
            pointer.next = b
            pointer = a
        return dummy.next

