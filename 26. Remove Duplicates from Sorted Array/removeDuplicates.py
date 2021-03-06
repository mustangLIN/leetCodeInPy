class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1
        
        count = 0
        for i in range(1, len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]

        return count + 1