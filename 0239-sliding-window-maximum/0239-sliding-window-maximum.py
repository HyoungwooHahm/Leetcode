class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mq=[]
        i = 0
        j = 0
        sol = []
        while j < len(nums):
            while len(mq) > 0 and mq[-1] < nums[j]:
                mq.pop()    
            mq.append(nums[j])
            
            if j < k-1:
                j += 1
            elif j - i + 1 == k:
                sol.append(mq[0])
                if nums[i] == mq[0]:
                    mq.pop(0)
                i += 1
                j += 1
        return sol