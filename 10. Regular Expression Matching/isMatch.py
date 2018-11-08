class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # i=len(s), j=len(p). i * j result table of boolean, from every Combination
        # '.' Matches any single character.
        # '*' Matches zero or more of the preceding element.

        # Dictionary memo is boolean table, memo[i, j] is dp(i, j) result
        memo = {}
        # use Recursive
        def dp(i, j):
            if (i, j) not in memo:
                # j is finish
                if j == len(p):
                    # ans = boolean, result is check i is or not finish
                    ans = i == len(s)
                else:
                    # first_match = boolean, check p[j] == s[i], check p[j] == char '.'
                    first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
                    # next p[j] is '*'
                    if j + 1 < len(p) and p[j + 1] == '*':
                        #  s:  s[i]  s[i+1]  s[i+2]
                        #  p: #p[j]   '*'    p[j+2]
                        # first_match check #p[j] with s[i]
                        # dp(i + 1, j) check #p0 with s[i+1]
                        # dp(i, j + 2) check ("#p[j] '*' p[j+2]"")
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    # do next Recursive, 
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                # storage ans
                memo[i, j] = ans
            # def END
            return memo[i, j]
        
        # let dp(i, j) return real ans, let dp from (0, 0) satrt Recursive
        return dp(0, 0)