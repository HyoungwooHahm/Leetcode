class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        p=[[1], [1,1]]
        if numRows == 1 :
            return [[1]]
        if numRows == 2 :
            return p
        
        if numRows > 2:
            for i in range (3,numRows+1):
                newline=[1]*i
                p.append(newline)
                for j in range (1,i-1):
                    p[i-1][j]=p[i-2][j-1]+p[i-2][j]
        
        return p
                
        