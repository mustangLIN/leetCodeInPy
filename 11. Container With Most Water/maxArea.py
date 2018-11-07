class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        indexL = 0
        indexR = len(height) - 1
        while indexL < indexR:
            width = indexR - indexL
            heightMin = min(height[indexL], height[indexR])
            Area = width * heightMin
            maxArea = max(maxArea, Area)
            if height[indexL] < height[indexR]:
                indexL += 1
            else:
                indexR -= 1
        
        return  maxArea