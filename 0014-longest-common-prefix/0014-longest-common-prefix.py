class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=""
        l=[]
        for i in strs:
            l.append(len(i))
        for i in range(len(strs[l.index(min(l))])):
            b=""
            for word in strs:
                if b and word[i]!=b:
                    b=""
                    break
                b=word[i]
                
            if not b: break
            s+=b
        return s
            
        