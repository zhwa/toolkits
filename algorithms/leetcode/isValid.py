class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L = len(s)
        if L % 2 == 1: return False
        if L == 0: return True
        store = stack()
        left = ["(", "[", "{", None]
        right = [")", "]", "}", None]
        check = lambda a,b: left.index(a) == right.index(b) if a in left and b in right else False
        error = lambda a,b: left.index(a) != right.index(b) if a in left and b in right else False
        for ele in s:
            if check(store.last(), ele):
                store.pop()
            elif error(store.last(), ele):
                return False
            else:
                store.push(ele)
        return store.leng() == 1
        
        

class stack(object):
    def __init__(self):
        self.s = [None]
    
    def push(self, ele):
        self.s.append(ele)
    
    def pop(self):
        self.s.pop()
    
    def last(self):
        return self.s[-1]
    
    def leng(self):
        return len(self.s)
