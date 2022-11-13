class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a=0
        z=len(nums)-1
    
        while a <= z:
            mid = (a + z) // 2
\
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                a = mid + 1 
            else:
                z = mid -1
        
        return a
        