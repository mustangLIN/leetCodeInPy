class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        stack = []
        for c in s:
            # check c is right Parentheses 
            if c in dict.values():
                # c is right Parentheses, stack is empty, no pair
                if not stack:
                    return False
                
                if dict[c] == stack[-1]:
                    del stack[-1]
                else:
                    return False

            # c is left, put in stack, wait to compare
            else:
                stack.append(c)

        # stack == empty, True or False
        return not stack