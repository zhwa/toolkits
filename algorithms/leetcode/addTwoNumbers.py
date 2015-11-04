# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        calc = lambda a,b,c: ( (a+b+c)%10, (a+b+c)/10 )
        carry = 0
        res = None
        current = None
        while l1 != None or l2 != None or carry > 0:
            if l1 == None and l2 != None:
                (digit, carry) = calc(0, l2.val, carry)
                l2 = l2.next
            elif l1 != None and l2 == None:
                (digit, carry) = calc(l1.val, 0, carry)
                l1 = l1.next
            elif l2 == None and l2 == None:
                digit = carry
                carry = 0
            else:
                (digit, carry) = calc(l1.val, l2.val, carry)
                l1 = l1.next
                l2 = l2.next
            if res == None:
                res = ListNode(digit)
                current = res
            else:
                current.next = ListNode(digit)
                current = current.next
        return res
