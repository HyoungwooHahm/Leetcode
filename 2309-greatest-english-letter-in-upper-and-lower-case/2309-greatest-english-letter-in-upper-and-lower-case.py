class Solution:
    def greatestLetter(self, s: str) -> str:
        l=[]
        ans=[]
        check=False
        for i in s:
            l.append((ord(i)))
            if l:
                if ord(i)-32 in l or ord(i)+32 in l: 
                    check=True
                    ans.append(ord(i.upper()))
            
        if check:
            return chr(max(ans))
        
        return ""
            
        