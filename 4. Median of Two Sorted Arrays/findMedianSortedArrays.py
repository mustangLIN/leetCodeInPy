class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # let len(nums1) < len(nums2)
        if len(nums1) > len(nums2):
            nums1, nums2= nums2, nums1
        
        # Searching i in nums1, from [0, len(nums1)]
        # i cut in nums1, nums1[0]...nums1[i-1] | nums1[i]...nums1[m-1]
        # j cut in nums2, nums2[0]...nums2[j-1] | nums2[j]...nums2[n-1]
        # j = ((m+n+1)/2) - i, i + j = total length left part
        # need nums1[i-1] < nums2[j], L1 < R2
        # need nums2[j-1] < nums1[i], L2 < R1
        m = len(nums1)
        n = len(nums2)
        totalLen_half = (m + n + 1) // 2
        # Searching at [n1_L, n1_R], i cut at middle
        n1_L = 0
        n1_R = m
        while n1_L <= n1_R:
            i = (n1_L + n1_R) // 2
            j = totalLen_half - i
            # L2 > R1, i too small go right, [n1_L + 1, n1_R]
            if i < m and nums2[j - 1] > nums1[i]:
                n1_L = i + 1
            # L1 > R2, i too big go left, [n1_L, n1_R - 1]
            elif i > 0 and nums1[i - 1] > nums2[j] :
                n1_R = i - 1    
            else:
                # i is perfect

                # [nums2] < [nums1], total left part only use nums2 element
                if i == 0:
                    max_of_left = nums2[j-1]
                # [nums1] < [nums2], total left part only use nums1 element
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])
                
                # totol length id odd, only need max_of_left
                if (m + n) % 2 == 1:
                    return max_of_left

                # totol length id even, need min_of_right to calculate average
                # all [nums1] at total left part, rihght part olny use nums2 element
                if i == m:
                    min_of_right = nums2[j]
                # all [nums2] at total left part, rihght part olny use nums2 element
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                 
                return (max_of_left + min_of_right) / 2.0