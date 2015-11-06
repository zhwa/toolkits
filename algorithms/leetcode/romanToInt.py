class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
        if s in table: return table[s]
        res = 0
        i = 0
        while i < len(s)-1:
            if s[i:i+2] in ["IV", "IX", "XC", "XL", "CD", "CM"] :
                res += table[s[i+1]] - table[s[i]]
                i += 2
            else:
                res += table[s[i]]
                i += 1
        if i < len(s): res += table[s[-1]]
        return res
