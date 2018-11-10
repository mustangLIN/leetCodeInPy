# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # create ListNode, .val is ""
        ans = ListNode("")
        # point to head
        ans.next = head
        
        # pointer explore, remove for new_head
        explore = ans
        remove = ans
        # explore Lead n+1 step than remove
        for i in range(n + 1):
            explore = explore.next
        
        # let explore, remove move next, until first going to END
        while explore != None:
            explore = explore.next
            remove = remove.next
        
        # change address, point to .next.next
        remove.next = remove.next.next
        return ans.next