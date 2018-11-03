# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = ListNode(0) 
        # Initialize answer to head of curr
        answer = curr
        carry=0
        while l1 != None or l2 != None:
            # Set x to node l1 value. If l1 has reached the end, set x to 0.
            if l1:
                x = l1.val
            else:
                x = 0
            if l2:
                y = l2.val
            else:
                y = 0
            sum = x + y + carry
            carry = int(sum / 10)
            curr.next = ListNode(sum % 10)
            # list to next node
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        # final check, if carry > 0 need add 1 digit to curr
        if carry > 0:
            curr.next = ListNode(carry)
        return answer.next