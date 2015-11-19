class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s = [c for c in str(secret)]
        g = [c for c in str(guess)]
        bulls = filter(lambda i: s[i] == g[i], range(len(s)))
        other = filter(lambda i: i not in bulls, range(len(s)))
        sFiltered = [s[i] for i in other]
        gFiltered = [g[i] for i in other]
        sFiltered.sort()
        gFiltered.sort()
        n2 = 0
        for ele in sFiltered:
            if ele in gFiltered:
                gFiltered.remove(ele)
                n2 += 1
        n1 = len(bulls)
        return str(n1)+"A"+str(n2)+"B"
