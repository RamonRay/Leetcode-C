# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        x=[]
        pointer=head
        l=0
        while(pointer!=None):
            x.append(pointer)
            pointer=pointer.next
            l+=1
        if n==l:
            return head.next
        if n==1:
            x[l-2].next=None
        else:
            x[l-n-1].next=x[l-n+1]
        return head
