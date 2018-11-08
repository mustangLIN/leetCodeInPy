class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == None or len(nums) < 3:
            return []

        nums = sorted(nums)        
        ans = nums[0] + nums[1] + nums[-1]
        min_gap =max((nums[0] + nums[1] + nums[-1]), target)  - min((nums[0] + nums[1] + nums[-1]), target)
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == target:
                    return target
                
                gap = max((nums[i] + nums[left] + nums[right]),target) - min((nums[i] + nums[left] + nums[right]),target)
                if gap < min_gap:
                    min_gap = gap
                    ans = nums[i] + nums[left] + nums[right]
                if nums[left] + nums[right] > target - nums[i]:
                    right -= 1
                elif nums[left] + nums[right] < target - nums[i]:
                    left += 1

        return ans