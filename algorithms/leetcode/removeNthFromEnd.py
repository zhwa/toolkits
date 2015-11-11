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
        current = head
        i = 1
        while current.next != None:
            current = current.next
            i += 1
        L = i + 1
        newHead = ListNode(0)
        newHead.next = head
        current = newHead
        for i in range(L-n-1):
            current = current.next
        temp = current.next.next
        current.next = temp
        return newHead.next
