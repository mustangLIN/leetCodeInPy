# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return lists

        len_ListNode = len(lists)
        index = 1
        # ([0],1),([2],3),([4],5),...      => i = [0,2,4,...], range(0,,2)
        # ([0],     2),   ([4],6),([8],10) => i = [0,4,8,...], range(0,,4)
        # ([0],             4),   ([8],12) => i = [0,8,16,..], range(0,,8)
        while index < len_ListNode:
            for i in range(0, len_ListNode - index, index * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + index])
            
            index *= 2
        
        return  lists[0]
    
    # 21. Merge Two Sorted Lists
    def merge2Lists(self, l1, l2):
        result = ListNode("")
        ans = result
        while l1 and l2:
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