class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix),len(matrix[0])
        a,z = 0,r-1
        i = -1
        while a<=z:
            mid = (a+z)//2
            if matrix[mid][0]<=target and matrix[mid][c-1]>=target:
                i = mid
                break
            elif matrix[mid][c-1]>target:
                z = mid-1
            else:
                a = mid+1
           
        a,z = 0,c-1
        while a<=z:
            mid= (a+z)//2
            if matrix[i][mid]==target:
                return 1
            elif matrix[i][mid]>target:
                z = mid-1
            else:
                a = mid+1
        return 0