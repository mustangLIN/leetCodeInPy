# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        if not head.next:
            return head
        
        ans = ListNode("")
        ans.next = head
        
        # first lead second 1 step
        first = head
        second = ans
        explore = ans
        while first != None and first.next != None:
            # first at 1, first.next.next == 2.next, 2.next is posittion 3  
            explore = first.next.next
            # 2.next = posittion 1
            first.next.next = first
            # second.next = posittion 2
            second.next = first.next
            # 1.next = posittion 3 
            first.next = explore
            # second goto first posittion
            second = first
            # first goto posittion 3
            first = first.next
        
        return ans.next

        '''
        if not head:
            return None
        
        if not head.next:
            return head
        
        ans = ListNode("")
        ans.next = head
        
        p = ans
        while p.next != None and p.next.next != None:
            # p=""-> 1-> 2-> 3
            # make tmp at 2, tmp=2-> 3
            tmp = p.next.next
            #  use tmp let p jump 2, p=""-> 1-> 3
            p.next.next = tmp.next

            # make tmp=2-> 1
            tmp.next = p.next
            # use tmp let p=""-> 2-> 1-> 3
            p.next = tmp
            
            # update p position, ""-> 2-> p=1-> 3
            p = tmp.next
        
        return ans.next
        '''