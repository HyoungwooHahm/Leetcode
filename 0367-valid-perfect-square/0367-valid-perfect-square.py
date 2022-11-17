class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a = 1
        z = num
        
        while a <= z:
            mid = ( a + z ) //2
            if mid * mid == num:
                return mid
            elif mid * mid < num:
                a = mid + 1
              
            elif mid * mid > num:
                z = mid - 1
                
        return False
        