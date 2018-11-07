class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num <= 0:
            raise ValueError
        
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbol = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        
        s = ""
        for i, j in zip(symbol, value):
            while num >= j:
                s += i
                num -= j
            if num == 0:
                break
        
        return s

        '''
        # = [0,   1,   2,    3,     4,    5,   6,    7,     8,      9  ]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        
        s = ""
        if num >= 1000:
            for i in range(num // 1000):
                s = s + "M"
        
        s += C[(num % 1000) // 100]
        s += X[(num % 100) // 10]
        s += I[num % 10]
        '''