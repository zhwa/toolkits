class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = map(lambda s: [c for c in s], board)
        cols = map(lambda i: [s[i] for s in rows], range(9))
        unit = []
        rBound = [(0,3),(3,6),(6,9)]
        for i in rBound:
            for j in rBound:
                temp = [rows[ix][iy] for ix in range(i[0], i[1]) for iy in range(j[0], j[1])]
                unit.append(temp)
        
        def double(sList):
            ensemble = set()
            for item in sList:
                if item is not ".":
                    if item in ensemble:
                        return False
                    else:
                        ensemble.add(item)
            return True
        
        rRes = map(double, rows)
        cRes = map(double, cols)
        uRes = map(double, unit)
        print rRes, cRes, uRes
        if False in rRes or False in cRes or False in uRes:
            return False
        else:
            return True
