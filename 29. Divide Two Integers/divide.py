class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return 2**31 - 1
        
        if divisor == 1:
            return dividend
        
        if divisor == -1:
            if dividend == -1 * 2**31:
                return (2**31 - 1)
            else:
                return -1 * dividend

        if dividend == 0 or abs(dividend) < abs(divisor):
            return 0

        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        
        if dividend < 0:
            dividend = dividend * -1
        
        if divisor < 0:
            divisor = divisor * -1
        
        quotient = 0
        while dividend >= divisor:
            shift = 0
            while dividend >= divisor * (1 << shift):
                shift += 1
            
            quotient += 1 << (shift - 1)
            dividend -= divisor * (1 << shift - 1)
        
        return quotient * sign