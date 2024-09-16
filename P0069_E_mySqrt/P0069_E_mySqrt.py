class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        left = 0
        right = x
        while right >= left:
            mid = (left + right) // 2
            if mid**2 == x:
                return mid
            elif mid**2>x:
                right = mid-1
            else:
                left = mid +1  
        return right