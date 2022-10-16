class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i=0
        j=0
        while '#' in s :
            if s[i] == '#':
                if i==0:
                    s=s[1:]
                    continue
                s=s[:i-1]+s[i+1:]
                i-=1
                continue
            i+=1
        while '#' in t :
            if t[j] == '#':
                if j==0:
                    t=t[1:]
                    continue
                t=t[:j-1]+t[j+1:]
                j-=1
                continue
            j+=1
       
        
        if s==t :
            return True
        else :
            return False
            
                
        