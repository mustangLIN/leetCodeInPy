class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x
        
        ans = 0
        while x != 0:
            pop = x - int(x / 10) * 10
            x = int(x / 10)
            ans = ans * 10 + pop            
        
        if ans > 2**31-1 or ans <= -2**31:
            return 0
        
        return ans