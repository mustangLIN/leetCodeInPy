# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # creat new ListNode
        result = ListNode("")
        # result head position
        ans = result

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                result.next = l1
                l1 = l1.next
            else:
                result.next = l2
                l2 = l2.next
            result = result.next
        
        if l1 != None:
            result.next = l1

        if l2 != None:
            result.next = l2
        
        return ans.next