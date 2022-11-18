class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        l = []
        for i, n in enumerate(mat):
           l.append([sum(n), i])
        l.sort()
        return [k for j, k in l[0:k]]