# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n==1 and isBadVersion(n):
            return 1
        a = 1
        z = n

        while a <= z:
            mid = a + (z-a) // 2
            if isBadVersion(mid):
                if isBadVersion(mid -1) == False:
                    return mid
                else:
                    z = mid-1
            else:
               a = mid + 1 
            
        return 0