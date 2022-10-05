class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        out=[]
        for i in range(len(l)):
            if r[i]-l[i] == 1:
                out.append(True)
                continue
                
            new=nums[l[i]:r[i]+1]
            
            new.sort()
            diff=0
            IsArithmetic=False
            for j in range(len(new)-1):
                if j==0 :
                    diff=new[j+1]-new[j]
                else :
                    if diff != new[j+1]-new[j]:
                        break
                    elif j == len(new)-2:
                        IsArithmetic=True
                        
            if IsArithmetic:
                out.append(IsArithmetic)
                continue
                
            new.reverse()
            for k in range(len(new)-1):
                if k==0 :
                    diff=new[k+1]-new[k]
                else :
                    if diff != new[k+1]-new[k]:
                        break
                    elif k == len(new)-2:
                        IsArithmetic=True
            out.append(IsArithmetic)
        
        return out
            
            
                      
                
                
                    
                