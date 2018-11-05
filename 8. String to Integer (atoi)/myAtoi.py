class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """        
        start = 0
        end = 0
        sign = "+"
        num = 0
        
        try:            
            if str[0].isdigit() == False and str[0] != "+" and str[0] != "-" and str[0] != " ":
                return 0

            # find start location, pass "space"
            for i in range(len(str)):
                if str[i] != " ":
                    start = i
                    break

            if str[start] == "-":
                start = start + 1
                sign = "-"
            elif str[start] == "+":
                start = start + 1
                sign = "+"

            for i in range(start, len(str)):
                if str[i].isdigit() == False:
                    break
                
                end = i + 1                    
            
            # maybe some except
            if end == 0:
                return 0

            num = int(str[start:end])
            if sign == "+":
                if num > 2**31 - 1:
                    return 2**31 - 1
                else:
                    return num
            elif sign == "-":
                if num > 2**31:
                    return -1 * (2**31)
                else:
                    return -1 * num
        except:
            return 0