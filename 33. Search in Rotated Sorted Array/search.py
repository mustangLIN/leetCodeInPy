class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            
            # right is sorted
            if nums[mid] <= nums[end]:
                if nums[mid] < target and target <= nums[end]:
                    # go right
                    start = mid + 1
                else:
                    # go left
                    end = mid - 1
            # left is sorted
            else:
                if nums[start] <= target and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        
        return -1
