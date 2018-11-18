class Solution:    
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 1:
            return 0
        
        stack = [-1]
        maxLen = 0
        length = 0
        for i,c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                if len(stack) == 1:
                    stack[0] = i
                else:
                    del stack[-1]
                    length = i - stack[-1]
                    maxLen = max(maxLen, length)
        
        return maxLen
        
'''
a=Solution()
a.longestValidParentheses(")()(()()")
'''