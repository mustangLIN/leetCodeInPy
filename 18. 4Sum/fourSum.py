class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if nums == None or len(nums) < 4:
            return []

        nums=sorted(nums)
        ans = []
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                firstNum = nums[i] + nums[j]
                if i > 0 and nums[i] == nums[i - 1] or j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left = j + 1
                right = len(nums) - 1
                newTarget = target - firstNum
                while left < right:
                    if nums[left] + nums[right] > newTarget:
                        right -= 1
                    elif nums[left] + nums[right] < newTarget:
                        left += 1
                    elif nums[left] + nums[right] == newTarget:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

        return ans