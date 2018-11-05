class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False
        if x == 0:
            return True
        
        rev = 0            
        while x > rev:
            rev = rev * 10 + x % 10
            x=int(x / 10)

        # odd use x == int(rev / 10)
        # source 12321
        # after calculate, x = 12 rev = 123, 3 is center, self == self
        if x == rev or x == int(rev / 10):
            return True
        else:
            return False