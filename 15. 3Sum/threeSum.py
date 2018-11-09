class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == None or len(nums) < 3:
            return []

        nums=sorted(nums)
        # all positive or all negative, no ans
        if nums[0] > 0 or nums[-1] < 0:
            return []
        
        ans = []
        for i in range(len(nums) - 2):
            # same ans[i][0] not do again
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            target = -1 * nums[i]
            while left < right:
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] == target:
                    ans.append([nums[i], nums[left], nums[right]])
                    # continue find another ans
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return ans