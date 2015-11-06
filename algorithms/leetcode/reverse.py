class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        if x % 10 == 0: return self.reverse(x/10)
        if x > 0:
            limit = 2**31 - 1
            sgn = 1
        else:
            limit = 2**31
            sgn = -1
        a = abs(x)
        result = 0
        while a > 0:
            digit = a % 10
            a = a / 10
            if result > (limit - digit) / 10:
                return 0
            else:
                result = result * 10 + digit
        return sgn * result
