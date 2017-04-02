# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(first,last):
            prev=last
            while first!=last:
                tmp=first.next
                first.next=prev
                prev=first
                first=tmp
            return prev
        pointer=head
        if pointer==None:
            return None
        for i in range(k-1):
            pointer=pointer.next
            if pointer==None:
                return head
        pointer=pointer.next
        new_head=reverse(head,pointer)
        head.next=self.reverseKGroup(pointer,k)
        return new_head