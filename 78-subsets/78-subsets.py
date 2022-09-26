from itertools import combinations

class Solution(object):
    def subsets(self, nums):
        self.ss=[[]]
        for i in range(1,len(nums)+1):
            c = list(combinations(nums,i))
            for j in range(len(c)):
                 self.ss.append(list(c[j]))
            
        return self.ss
            
            
            
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        