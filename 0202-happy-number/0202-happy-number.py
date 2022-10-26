class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        
        while n not in s :
            hs=0
            for i in str(n):
                hs+=int(i)*int(i)
            if hs==1: return True
            s.add(n)
            n=hs
            
        return False
        