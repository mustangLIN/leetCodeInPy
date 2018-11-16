# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        if not head.next or k <= 1:
            return head
        
        count = 0
        cur = head
        while cur != None and count < k:
            cur = cur.next            
            count += 1
        
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count > 0:
                temp = head.next
                head.next = cur
                cur = head
                head =temp

                count -= 1
            
            head = cur        
        return head