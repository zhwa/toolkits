class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        if 0 < x < 10: return True
        n = x
        m = 0
        while n >= 10:
            n = n / 10
            m += 1
        n = 0
        while n < 1.0*m/2:
            if (x / 10**n) % 10 != (x / 10**(m-n)) % 10:
                return False
            else:
                n += 1
        return True 
