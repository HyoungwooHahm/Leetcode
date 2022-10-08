class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        left, right = min(nums), max(nums)
        length = right - left + 1
        counts = [0] * length
        L = [0] * len(nums)
        
        for num in nums:
            counts[num - left] += 1
            
        for i in range(1, len(counts)):
            counts[i] += counts[i - 1]
            
        for num in nums:
            L[counts[num - left] - 1] = num
            counts[num - left] -= 1
        return L
