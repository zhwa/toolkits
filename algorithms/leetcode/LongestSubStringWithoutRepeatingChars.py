class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1: return len(s)
        iLeft = 0
        iRight = 1
        currentArray = s[iLeft:iRight]
        check = set([s[iLeft]])
        maxLen = 1
        while iRight < len(s):
            if s[iRight] in check:
                if len(currentArray) > maxLen:
                    maxLen = len(currentArray)
                iLeft = currentArray.index(s[iRight]) + iLeft + 1
            currentArray = s[iLeft:iRight+1]
            check = set(currentArray)
            iRight += 1
        if len(s[iLeft:iRight]) > maxLen: maxLen = len(s[iLeft:iRight])
        return maxLen
