class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index = -1
        L = len(haystack)
        l = len(needle)
        if needle == "": return 0
        if l > L: return -1
        for i in range(0, L-l+1):
            if haystack[i:i+l] == needle:
                index = i
                return index
        return index
