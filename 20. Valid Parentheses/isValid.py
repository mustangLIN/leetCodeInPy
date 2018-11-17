class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        if len(s) == 1:
            return False
        
        dict = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        stack = []
        for c in s:
            # check c is left Parentheses, put in stack, wait couple
            if c in dict.keys():
                stack.append(c)
            # c is right, is couple
            elif len(stack) > 0 and c == dict[stack[-1]]:
                    del stack[-1]
            # c is right, stack is empty nothing to couple, or couple fail
            else:
                return False

        # stack == empty, True or False
        return not stack