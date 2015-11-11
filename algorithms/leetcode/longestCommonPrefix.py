class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        chr = lambda i: map(lambda s: s[i], strs)
        com = ""
        i = -1
        while True:
            i += 1
            try:
                chrs = chr(i)
            except IndexError:
                break
            if len(chrs) > 0:
                check = reduce(lambda a,b: a if a==b else False, chrs)
            else:
                break
            if check:
                com += chrs[0]
            else:
                break
        return com
