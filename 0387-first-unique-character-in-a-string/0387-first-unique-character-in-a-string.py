class Solution:
    def firstUniqChar(self, s: str) -> int:

        for a in s:
            if s.count(a)==1:
                return s.index(a)
            
        return -1
            
        