class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix),len(matrix[0])
        
        for i in range(r):
            if matrix[i][0]<=target and matrix[i][-1]>=target:
                a,z=0,c
                
                while (a<z):
                    mid=(a+z)//2
                    
                    if matrix[i][mid]==target:
                        return True
                    elif matrix[i][mid]<target:
                        a = mid + 1
                    else:
                        z = mid
        return False
                        

        