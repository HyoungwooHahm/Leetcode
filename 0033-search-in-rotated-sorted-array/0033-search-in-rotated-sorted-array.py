class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a, z= 0, len(nums)-1
  
        while a<=z:
            mid=(a+z)//2      
            if nums[mid]==target:
                return mid
            elif nums[mid]>=nums[a]:
                if (target>=nums[a] and target<nums[mid]):
                    z=mid-1
                else:
                    a=mid+1
            else:
                if (target<=nums[z] and target>nums[mid]):
                    a=mid+1
                else:
                    z=mid-1
        return -1
