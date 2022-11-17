class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        total=(sum(aliceSizes)+sum(bobSizes))//2
        a=total-sum(aliceSizes)
        b=total-sum(bobSizes)
        l=[]
        if a>b:
            for i in bobSizes:
                if i-a in aliceSizes:
                    l.append(i-a)
                    l.append(i)
                    return l
        if b>a:
            for i in aliceSizes:
                if i-b in bobSizes:
                    l.append(i)
                    l.append(i-b)
                    return l

        