# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None: return l2
        if l2 == None: return l1
        p1 = l1
        p2 = l2
        if p1.val < p2.val: 
            res = ListNode(p1.val)
            p1 = p1.next
        else: 
            res = ListNode(p2.val)
            p2 = p2.next
        current = res
        while p1 != None and p2 != None:
            if p1.val < p2.val:
                current.next = ListNode(p1.val)
                p1 = p1.next
            else:
                current.next = ListNode(p2.val)
                p2 = p2.next
            current = current.next
        if p1 != None: 
            p = p1
        elif p2 != None:
            p = p2
        else:
            return res
        while p != None:
            current.next = ListNode(p.val)
            current = current.next
            p = p.next
        return res
