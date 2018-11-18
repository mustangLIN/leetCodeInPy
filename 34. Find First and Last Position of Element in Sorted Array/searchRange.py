class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1,-1]
        
        low = 0
        high = len(nums) 
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                start = 0
                end = mid
                high = len(nums) 
                while start < high:
                    start_mid = (start + high) // 2
                    if target == nums[start_mid]:
                        high = start_mid
                    else:
                        start = start_mid + 1

                high = len(nums) 
                while end < high:
                    end_mid = (end + high) // 2
                    if nums[end] > target:
                        high = end_mid
                    else:
                        end = end_mid + 1
                
                return [start, end - 1]

            if nums[mid] < target and target <= nums[high]:
                # go right
                low = mid + 1
            else:
                # go left
                high = mid - 1
        
        return [-1,-1]

'''
a=Solution()
a.searchRange([8,8,8], 8)
'''