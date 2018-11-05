class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1 or numRows >= len(s):
            return s
        
        rows = [""] * numRows
        curRow = 0
        step = -1
        
        for c in s:
            rows[curRow] += c
            if curRow == 0:
                step = 1
            elif curRow == numRows - 1:
                step = -1
           
            curRow += step
        
        str = ""
        return str.join(rows)