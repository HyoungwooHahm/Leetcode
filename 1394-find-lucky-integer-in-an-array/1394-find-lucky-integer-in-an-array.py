class Solution:
    def findLucky(self, arr: List[int]) -> int:
        l=[]
        for i in set(arr):
            if arr.count(i)==i: l.append(i)
        if l:return max(l)
        return -1
        