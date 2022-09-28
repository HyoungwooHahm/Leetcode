class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums :
            return [-1,-1]
        s=[]
        s2=[]
        l=0
        for a in nums:
            if a==target:
                s.append(l)
            l+=1
        s2.append(s[0])
        s2.append(s[-1])
        return s2
                