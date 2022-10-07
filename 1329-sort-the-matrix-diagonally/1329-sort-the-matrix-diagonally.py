class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        for n in range(len(mat)-1,-1,-1):
            for i, j in zip(range(n,n+len(mat[0])),range(len(mat[0]))):
                if i+1==len(mat) or j+1==len(mat[0]):
                    break
                while mat[i][j]>mat[i+1][j+1]:
                    temp=mat[i][j]
                    mat[i][j]=mat[i+1][j+1]
                    mat[i+1][j+1]=temp
                    i-=1
                    j-=1
                    if i < 0 or j < 0: break
    
            
        for n in range(1,len(mat[0])):
            for i, j in zip(range(len(mat)),range(n,n+len(mat))):
                if i+1==len(mat) or j+1==len(mat[0]):
                    break
                while mat[i][j]>mat[i+1][j+1]: 
                    temp=mat[i][j]
                    mat[i][j]=mat[i+1][j+1]
                    mat[i+1][j+1]=temp
                    i-=1
                    j-=1
                    if i< 0 or j < 0 : break
                    
        return mat
            
        