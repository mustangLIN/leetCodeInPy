class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        alphabet = {"1" : [""],
                    "0" : [""],
                    "*" : [""],
                    "#" : [""],
                    "2" : ["a", "b", "c"],
                    "3" : ["d", "e", "f"],
                    "4" : ["g", "h", "i"],
                    "5" : ["j", "k", "l"],
                    "6" : ["m", "n", "o"],
                    "7" : ["p", "q", "r", "s"],
                    "8" : ["t", "u", "v"],
                    "9" : ["w", "x", "y", "z"]
        }

        # put in digits[0].alphabet
        ans = alphabet[digits[0]]
        # from digits[1] start
        for i in range(1, len(digits)):
            tmp = []
            # start Combination digits[i].alphabet[k] and ans[j]
            for j in ans:
                for k in alphabet[digits[i]]:
                    tmp.append(j + k)
            
            # update ans, let combination result to next loop, combination next digits[i]
            ans = tmp
        
        return ans