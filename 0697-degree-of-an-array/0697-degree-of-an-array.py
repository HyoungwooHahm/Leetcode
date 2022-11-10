class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count={}
        index={}
        h=0
        ans=0
        
        for i in range(len(nums)):
            x=nums[i]
            
            if x not in count:
                count[x]=1
                index[x]=i
            else:
                count[x]+=1
            
            if count[x]>h:
                h=count[x]
                ans=(i-index[x]+1)
            elif count[x]==h:
                ans=min(ans,i-index[x]+1)
            
            
        return ans
        
        
        
        
        
        