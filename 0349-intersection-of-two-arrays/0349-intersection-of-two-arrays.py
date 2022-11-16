class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        if len(set(nums1)) <= len(set(nums2)):
            for a in set(nums1):
                if a in nums2:
                        l.append(a)
        else:
            for a in set(nums2):
                if a in nums1:
                        l.append(a)
                        
        return l