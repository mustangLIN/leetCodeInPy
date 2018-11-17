class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            nums = nums
        elif len(nums) == 2:
            nums[0], nums[1] = nums[1], nums[0]
        else:
            i = -2
            while i > -1 * len(nums):
                if nums[i] < nums[i+1]:
                    # find swap(i, )
                    break
                
                i -=1
            
            j = -1
            while j > -1 * len(nums):
                if nums[i] < nums[j]:
                    # find swap( , j)
                    break
                
                j -= 1
            
            #swap
            nums[i], nums[j] = nums[j], nums[i]
            if j != i:
                # nums[i+1:-1].reverse()
                i = i + 1
                j = -1
                while i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1                
            elif j == i:
                nums.reverse()