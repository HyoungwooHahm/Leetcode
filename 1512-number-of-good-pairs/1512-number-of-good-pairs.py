import math

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans=0
        for i in set(nums):
            if nums.count(i)>1:
                ans+=math.factorial(nums.count(i))/(math.factorial(nums.count(i)-2)*math.factorial(2))
        
        return int(ans)