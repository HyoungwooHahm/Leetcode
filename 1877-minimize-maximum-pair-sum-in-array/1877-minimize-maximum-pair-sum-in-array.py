
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        s=0
        for i in range(int(len(nums)/2)):
            if nums[i]+nums[len(nums)-i-1] > s :
                s=nums[i]+nums[len(nums)-i-1]
    
        return s
            
        
        