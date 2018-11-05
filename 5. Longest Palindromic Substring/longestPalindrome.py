class Solution: 
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0 or len(s) == 1:
            return s
        
        start = 0
        end = 0
        for i in range(len(s)):
            def expandAroundCenter(s,l,r):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l = l - 1
                    r = r + 1

                return r - l - 1
            # serch model "aba
            len1 = expandAroundCenter(s,i,i) 
            # serch model "abba
            len2 = expandAroundCenter(s,i,i+1) 
            len3 = max(len1,len2) 
            if len3 > (end - start):
                start = i - int((len3 - 1) / 2)
                end = i + int(len3 / 2)
        
        return s[start:end+1]