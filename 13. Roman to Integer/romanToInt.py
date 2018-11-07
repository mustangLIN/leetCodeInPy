class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """     
        symbol = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        ans = 0
        cLast = 0
        for c in s:
            ans += symbol[c]
            if cLast < symbol[c]:
                ans = ans - (cLast * 2)
            
            cLast = symbol[c]
        
        return ans